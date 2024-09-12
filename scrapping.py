import asyncio
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from gpt import GPT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the global driver once
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Function to fetch the page source using Selenium
def convert_to_https(url: str) -> str:
    # Check if the URL already starts with "http:// or https://"
    if url.startswith("http://"):
        # Replace "http://" with "https://"
        return url.replace("http://", "https://", 1)
    elif not url.startswith("https://"):
        # Add "https://" if it is missing
        return "https://" + url
    else:
        # URL already starts with "https://"
        return url
    
def fetch_page_source_selenium(url: str) -> str:
    driver.get(convert_to_https(url))
    
    # Wait until at least one <p> tag is present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'p'))
        )
    except TimeoutException:
        print("Timeout waiting for <p> tags to appear")
    
    page_source = driver.page_source
    return page_source

# Function to extract title and paragraphs from the page source
def extract_data(page_source: str) -> Dict[str, Any]:
    soup = BeautifulSoup(page_source, 'html.parser')

    title = soup.title.text.strip() if soup.title else 'Company'
    paragraphs = [
        p.get_text(strip=True) for p in soup.body.find_all('p') 
        if len(p.get_text(strip=True).split()) >= 3
    ]

    concatenated_paragraphs = ' '.join(paragraphs)

    data = {
        "title": title,
        "paragraphs": concatenated_paragraphs
    }
    print(data)

    return data

# Parallel processing of GPT requests
def process_gpt_requests(title: str, paragraphs: str) -> Dict[str, str]:
    about = GPT("Extract about the company in 150 words using provided data", f"Company Name :{title} Data: {paragraphs}")
    product_and_services = GPT("Extract product and services of company in 150 words using provided data", f"Company Name :{title} Data: {paragraphs}")
    return {
        "about": about,
        "productAndServices": product_and_services
    }

# Main function to fetch the company data using Selenium and parallel processing
async def fetch_company_data(url: str) -> Dict[str, Any]:
    loop = asyncio.get_event_loop()

    # Fetch the page source using Selenium in a separate thread
    page_source = await loop.run_in_executor(None, fetch_page_source_selenium, url)
    data = extract_data(page_source)

    # Use ThreadPoolExecutor for parallel processing of GPT tasks
    with ThreadPoolExecutor() as executor:
        gpt_results = await loop.run_in_executor(executor, process_gpt_requests, data['title'], data['paragraphs'])

    return {
        "title": data['title'],
        "about": gpt_results['about'],
        "productAndServices": gpt_results['productAndServices']
    }

# Close the driver after use
async def close_driver():
    driver.quit()

# Run the main function to fetch data
if __name__ == "__main__":
    url = "diiips.vercel.app/"
    try:
        result = asyncio.run(fetch_company_data(url))
        print(result)
    finally:
        asyncio.run(close_driver())

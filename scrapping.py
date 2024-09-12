import asyncio
import os
from typing import Dict, Any, Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from gpt import GPT

class WebScraper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebScraper, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def initialize_driver(self):
        if not self.driver:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome(options=chrome_options)

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def convert_to_https(self, url: str) -> str:
        if url.startswith("http://"):
            return url.replace("http://", "https://", 1)
        elif not url.startswith("https://"):
            return "https://" + url
        return url

    def fetch_page_source(self, url: str) -> Optional[str]:
        if not self.driver:
            raise ValueError("Driver not initialized. Call initialize_driver() first.")
        
        try:
            self.driver.get(self.convert_to_https(url))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'p'))
            )
            return self.driver.page_source
        except TimeoutException:
            print("Timeout waiting for <p> tags to appear")
        except WebDriverException as e:
            print(f"Error fetching page source: {e}")
        return None

    @staticmethod
    def extract_data(page_source: Optional[str]) -> Dict[str, str]:
        if not page_source:
            return {"title": "", "paragraphs": ""}
        
        soup = BeautifulSoup(page_source, 'html.parser')
        title = soup.title.text.strip() if soup.title else ''
        paragraphs = ' '.join([
            p.get_text(strip=True) for p in soup.find_all('p') 
            if len(p.get_text(strip=True).split()) >= 3
        ])
        
        return {"title": title, "paragraphs": paragraphs}

class GPTProcessor:
    @staticmethod
    def process_requests(title: str, paragraphs: str) -> Dict[str, str]:
        if not title or not paragraphs:
            return {"about": "", "productAndServices": ""}
        
        about = GPT("Extract about the company in 150 words using provided data", 
                    f"Company Name: {title} Data: {paragraphs}")
        product_and_services = GPT("Extract product and services of company in 150 words using provided data", 
                                   f"Company Name: {title} Data: {paragraphs}")
        
        return {
            "about": about,
            "productAndServices": product_and_services
        }

scraper = WebScraper()

async def fetch_company_data(url: str) -> Dict[str, Any]:
    try:
        if not scraper.driver:
            scraper.initialize_driver()
        
        loop = asyncio.get_event_loop()

        page_source = await loop.run_in_executor(None, scraper.fetch_page_source, url)
        data = WebScraper.extract_data(page_source)

        with ThreadPoolExecutor() as executor:
            gpt_results = await loop.run_in_executor(
                executor, 
                GPTProcessor.process_requests, 
                data['title'], 
                data['paragraphs']
            )

        return {
            "title": data['title'],
            "about": gpt_results['about'],
            "productAndServices": gpt_results['productAndServices']
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "title": "",
            "about": "",
            "productAndServices": ""
        }

# Example of how to use this in an API
async def api_fetch_company_data(url: str) -> Dict[str, Any]:
    return await fetch_company_data(url)

if __name__ == "__main__":
    try:
        a = asyncio.run(api_fetch_company_data("zynth.ai"))
        print(a)
    except Exception as e:
        print(f"Error in main execution: {e}")
    finally:
        scraper.close_driver()

import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('GPT_API_KEY')

def GPT(prompt1: str, data: str) -> str:
    """
    Function to make a request to the OpenAI API with a given prompt and data.
    
    Args:
        prompt1 (str): The main prompt for the GPT model.
        data (str): Additional data to append to the prompt.
    
    Returns:
        str: The response from the GPT model, cleaned of extra whitespaces and quotes.
    """
    primary_prompt = [
        {"role": "system", "content": "You are a presentation creator and do not provide any unnecessary content."},
        {"role": "user", "content": f"{prompt1} {data}"}
    ]

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o",
                "messages": primary_prompt,
                "max_tokens": 150,
            }
        )
        
        response.raise_for_status()
        output = response.json()["choices"][0]["message"]["content"].strip()
        
        # Clean up the response by removing extra whitespaces and quotes
        output = ' '.join(output.split())  # Remove extra whitespaces
        output = output.strip('"')  # Remove leading and trailing quotation marks
        return output

    except requests.exceptions.RequestException as e:
        print(f"Error making request to OpenAI API: {e}")
        raise


# print(GPT("Create a presentation outline for", "AI in education"))

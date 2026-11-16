import os
import requests
from langchain_groq import ChatGroq
from tavily import TavilyClient
from bs4 import BeautifulSoup
from langchain.tools import tool
from dotenv import load_dotenv
from rich import print

load_dotenv()

# Initialize Tavily client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_research(query: str) -> str:
    """This tool helps to search queries from the web and gives current and latest news according to the user's query."""
    try:
        result = tavily.search(query=query, max_results=5)
        out = []
        for r in result.get('results', []):
            out.append(f"Title: {r.get('title')}\nURL: {r.get('url')}\nContext: {r.get('content', '')[:300]}\n")
        return f"\n----------\n".join(out)
    except Exception as e:
        return f"Tavily search error: {str(e)}"


@tool
def scraped_data(url: str) -> str:
    """ This tool is made to scrape the exact text content from a specific web page URL using BeautifulSoup."""
   
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    try:
        # Fetch the webpage
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200: 
            return f"Error: Failed to fetch webpage. Status code: {response.status_code}"
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted tags 
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()
            
        # Extract clean text
        text = soup.get_text(separator=' ', strip=True)[:3000]
        
        # Limit text length to avoid token limits for the LLM 
        return text[:4000] if len(text) > 4000 else text

    except Exception as e:
        return f"Scraping error: {str(e)}"





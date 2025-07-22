#!/usr/bin/env python3
"""
Simple script to scrape URLs from a file using Chrome remote debugging.
"""

import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import pandas as pd
import sys

def load_urls_from_file(file_path):
    """Loads URLs from a file, ignoring empty lines and lines starting with #."""
    urls = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                urls.append(line)
    return urls

def main():
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python scrape_from_file.py <urls_file> <output_csv>")
        print("Example: python scrape_from_file.py sample_urls.txt results.csv")
        return
    
    urls_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Load URLs from file
    print(f"📁 Loading URLs from {urls_file}")
    urls = load_urls_from_file(urls_file)
    
    if not urls:
        print("❌ No valid URLs found in file")
        return
        
    print(f"📋 Found {len(urls)} URLs to scrape")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")
    
    # Confirm before starting
    response = input("\nProceed with scraping? (y/n): ")
    if response.lower() != 'y':
        print("Scraping cancelled")
        return
    
    # Start scraping
    print(f"🚀 Starting browser...")
    try:
        results = asyncio.run(scrape_urls_with_playwright(urls))
        save_results_to_csv(results, output_file)
        print(f"✅ Scraping complete, results saved to {output_file}")
    except KeyboardInterrupt:
        print("\n⏹️ Scraping interrupted by user")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

async def scrape_urls_with_playwright(urls):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        for i, url in enumerate(urls, 1):
            print(f"  Scraping {i}/{len(urls)}: {url}")
            try:
                await page.goto(url, wait_until='domcontentloaded')
                content = await page.content()
                
                # Use BeautifulSoup to parse and extract text
                soup = BeautifulSoup(content, 'lxml')
                body_text = soup.body.get_text(separator=' ', strip=True)
                
                results.append({'url': url, 'content': body_text})
                
            except Exception as e:
                print(f"  ❌ Failed to scrape {url}: {e}")
                results.append({'url': url, 'content': f"Failed to scrape: {e}"})
                
        await browser.close()
    return results

def save_results_to_csv(results, output_file):
    if not results:
        print("No data to save.")
        return
    
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main() 
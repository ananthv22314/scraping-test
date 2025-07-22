# Chrome Remote Debugging Web Scraper

This scraper uses Chrome's DevTools Protocol (CDP) to extract content from websites by controlling a real Chrome browser instance. This approach is much less likely to be detected by anti-scraping measures since it uses genuine browser requests and can handle JavaScript-rendered content.

## 🎯 Key Features

- **Stealth Scraping**: Uses real Chrome browser, not detectable as a bot
- **JavaScript Support**: Handles SPAs and dynamic content perfectly
- **No Traditional Scraping Libraries**: Bypasses common anti-scraping measures
- **Local Browser Control**: Actually opens tabs on your local machine
- **CSV Output**: Clean, structured data export
- **Cross-Platform**: Works on macOS, Linux, and Windows

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Activate your virtual environment first
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install required packages
pip install -r requirements.txt
```

### 2. Prepare Your URLs

Edit `sample_urls.txt` with your target URLs (one per line):

```text
https://example.com
https://news.ycombinator.com
https://github.com
```

### 3. Run the Scraper

```bash
# Method 1: Use the simple file-based scraper
python scrape_from_file.py sample_urls.txt results.csv

# Method 2: Use the main script (edit URLs in the code)
python chrome_scraper.py
```

## 📋 How It Works

1. **Chrome Launch**: Launches Chrome with remote debugging enabled
2. **Protocol Connection**: Connects via WebSocket to Chrome's DevTools Protocol
3. **Navigation**: Navigates to each URL in your list
4. **Content Extraction**: Extracts title, meta description, and text content
5. **CSV Export**: Saves all data to a structured CSV file

## 🔧 Configuration Options

### Chrome Scraper Class

```python
scraper = ChromeScraper(debug_port=9222)  # Custom debug port
```

### Extracted Data Fields

- `url`: The scraped URL
- `title`: Page title
- `description`: Meta description
- `content`: Clean text content (limited to 5000 chars)
- `scraped_at`: Timestamp
- `status`: Success/error status

## 📁 File Structure

```
scraper/
├── chrome_scraper.py      # Main scraper class
├── scrape_from_file.py    # Simple file-based usage
├── sample_urls.txt        # Example URLs
├── requirements.txt       # Dependencies
└── results.csv           # Output (generated)
```

## ⚙️ Advanced Usage

### Custom URL Processing

```python
from chrome_scraper import ChromeScraper

# Your URLs
urls = [
    "https://example1.com",
    "https://example2.com"
]

scraper = ChromeScraper()
scraper.scrape_urls(urls, 'my_results.csv')
```

### Loading from Different File Formats

```python
# Load from JSON
import json
with open('urls.json', 'r') as f:
    data = json.load(f)
    urls = data['urls']

# Load from CSV
import csv
urls = []
with open('urls.csv', 'r') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader if row]
```

## 🛡️ Anti-Detection Features

- Uses real Chrome browser instance
- Proper user-agent and headers
- Natural timing between requests
- JavaScript execution capability
- Genuine browser fingerprint

## 🚨 Important Notes

### Chrome Requirements
- Google Chrome must be installed
- Script automatically detects Chrome location on macOS, Linux, Windows
- Creates temporary user profile for scraping

### Rate Limiting
- Built-in delays between requests (2 seconds default)
- Adjust timing in `scrape_urls()` method if needed
- Be respectful of target websites

### Error Handling
- Failed navigations are logged in CSV
- Chrome crashes are handled gracefully
- Keyboard interrupts (Ctrl+C) cleanup properly

## 🔍 Troubleshooting

### "Chrome not found" Error
Update the Chrome path in `chrome_scraper.py`:
```python
chrome_paths = [
    "/your/custom/chrome/path",  # Add your path here
    # ... existing paths
]
```

### Connection Issues
- Make sure no other applications are using port 9222
- Try a different debug port: `ChromeScraper(debug_port=9223)`
- Check if Chrome is already running with debugging enabled

### JavaScript Heavy Sites
- Increase wait time in `navigate_to_url()`: `time.sleep(10)`
- Add specific wait conditions for dynamic content

## 🤝 Contributing

Feel free to enhance this scraper with:
- Better wait conditions (instead of fixed delays)
- Proxy support
- Cookie management
- Screenshot capabilities
- More extraction options

## ⚖️ Legal Notice

This tool is for educational and legitimate research purposes only. Always:
- Respect robots.txt files
- Follow website terms of service
- Implement appropriate rate limiting
- Use responsibly and ethically

## 📄 License

This project is open source. Use responsibly! 🚀 
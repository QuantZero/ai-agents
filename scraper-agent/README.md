# Scraper Agent

A Python CLI tool that scrapes websites and uses OpenAI's GPT-4o-mini to generate intelligent, readable summaries. Perfect for quickly understanding what any website is about without wading through navigation menus, cookie banners, and other clutter.

## Features

- 🌐 **Smart URL Handling**: Accepts URLs in any format (`google.com`, `www.google.com`, `https://google.com`)
- 🧹 **Content Extraction**: Automatically filters out navigation, headers, footers, scripts, and other irrelevant content
- 🤖 **AI-Powered Summaries**: Uses OpenAI GPT-4o-mini to generate clear, concise summaries with a touch of wit
- 📝 **Terminal-Friendly**: Clean, formatted output designed for terminal viewing
- 🔒 **Secure**: API keys stored in `.env` file (gitignored)

## Requirements

- Python 3.12 or higher
- OpenAI API key
- `uv` package manager (or pip)

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd scraper-agent
   ```

2. **Install dependencies using `uv`**:
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   
   Create a `.env` file in the project root:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   
   Or manually create `.env` and add:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

   Get your API key from [OpenAI's website](https://platform.openai.com/api-keys).

## Usage

Run the script:
```bash
python main.py
```

Or with `uv`:
```bash
uv run main.py
```

When prompted, enter any website URL:
```
Which website would you like to check? google.com
```

The script will:
1. Normalize the URL (add `https://` if missing)
2. Fetch and scrape the website content
3. Send it to OpenAI for analysis
4. Display a formatted summary

### Supported URL Formats

All of these formats work:
- `google.com`
- `www.google.com`
- `https://google.com`
- `http://example.com`

## Project Structure

```
scraper-agent/
├── main.py           # Main script with OpenAI integration
├── scraper.py        # Web scraping utilities
├── pyproject.toml    # Project dependencies
├── .env              # API keys (gitignored)
└── README.md         # This file
```

## How It Works

1. **URL Normalization**: The `normalize_url()` function ensures URLs have a protocol (`https://` by default)

2. **Web Scraping**: `scraper.py` uses BeautifulSoup to:
   - Fetch the webpage with proper headers
   - Remove scripts, styles, images, and inputs
   - Extract clean text content
   - Truncate to 2,000 characters for efficiency

3. **AI Analysis**: The scraped content is sent to OpenAI's GPT-4o-mini with instructions to:
   - Focus on core content
   - Ignore navigation and boilerplate
   - Provide clear, accurate summaries
   - Use casual, readable language with light humor

4. **Output**: Results are displayed in a formatted terminal output

## Dependencies

- `beautifulsoup4` - HTML parsing and content extraction
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management
- `requests` - HTTP requests
- `ipython` & `ipykernel` - Optional Jupyter notebook support

## Error Handling

The script includes error handling for:
- Missing API keys
- Invalid URLs
- Network errors
- API failures

Errors are displayed clearly in the terminal output.

## Security

- API keys are stored in `.env` (gitignored)
- Never commit your `.env` file to version control
- The `.gitignore` file includes comprehensive Python and environment file patterns

## License

This project is open source and available for personal and commercial use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.


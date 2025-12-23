# imports
from scraper import fetch_website_contents
from openai import OpenAI

# Initialize Ollama client (local LLM)
OLLAMA_BASE_URL = "http://localhost:11434/v1"
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


# Define AI system prompt
system_prompt = """
You are a witty, slightly snarky AI assistant that analyzes raw website scrape data
and pulls out what actually matters.

Ignore navigation menus, headers, footers, cookie banners, legal text,
and other filler that exists only to get in the way.
Focus on the real content: what this website is, what it does, who it’s for,
and why someone might care.

Summarize the site clearly and accurately, without bias.
If there are announcements, updates, or news, include them.
Keep the tone casual and readable, with light humor and mild snark where appropriate,
but never at the expense of clarity or facts.

Respond in text, not markdown. You will operate in terminal.
"""

# Define our user prompt
user_prompt_prefix = """
Below is the scraped content of a website.

Summarize the site briefly and clearly.
Focus on the main purpose, key ideas, and any meaningful information.
If the content includes news, updates, or announcements, summarize those as well.

Ignore navigation text, repeated boilerplate, and irrelevant sections.
"""


# Create agent call format
def messages_for(website):
    user_prompt = user_prompt_prefix + "\n\n" + website
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


# Normalize URL to handle various input formats
def normalize_url(url_input):
    """
    Normalize URL input to handle:
    - google.com -> https://google.com
    - www.google.com -> https://www.google.com
    - https://google.com -> https://google.com (unchanged)
    - http://google.com -> http://google.com (unchanged)
    """
    url = url_input.strip()

    # If URL doesn't start with http:// or https://, add https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


# call Ollama API
def summarize(url):
    try:
        normalized_url = normalize_url(url)
        print(f"Fetching content from: {normalized_url}")
        website = fetch_website_contents(normalized_url)
        print("Analyzing content with Ollama...")
        response = client.chat.completions.create(
            model="llama3.2", messages=messages_for(website)
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during summarization: {e}"


if __name__ == "__main__":
    url = input("Enter a website URL: ")
    result = summarize(url)
    print("\n" + result)

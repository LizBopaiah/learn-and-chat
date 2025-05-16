import requests
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('GOOGLE_CX')  # Programmable Search Engine ID

def google_search(query):
    if not GOOGLE_API_KEY or not CX:
        return "Google API key or CX is not configured."

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': GOOGLE_API_KEY,
        'cx': CX,
        'q': query,
        'num': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get('items')
        if results:
            snippet = results[0].get('snippet', '')
            link = results[0].get('link', '')
            return f"{snippet}\n\nRead more: {link}"
        else:
            return "No results found."
    else:
        return "Failed to fetch results from Google Search."

# Fallback search handler (added for chat.py compatibility)
def google_search_fallback(query):
    return f"No results found for: {query}"

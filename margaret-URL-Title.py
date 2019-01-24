"""
This script is a super-simple example scraping content from a web page while using
libraries effectively.
This script is provided a URL, and returns the HTML <title> attribute.
"""

# Here at the top we are importing the libraries needed to get this done easily.
# Beautiful Soup is a library that makes it easy to scrape information from web pages.
# https://pypi.org/project/beautifulsoup4/
# Requests is a library for sending and receiving HTTP requests, easily.
# http://docs.python-requests.org/en/master/
from bs4 import BeautifulSoup
import requests

# Here we are defining a URL variable for the webpage we want to analyse.
PAGE_URL = 'https://twitter.com/adamlaz'

# Here we are defining a variable containing the HTTP response from the URL
PAGE_RESPONSE = requests.get(PAGE_URL, timeout=5)

# Here we are taking the HTTP response and using the Beautifulsoup html parser to store the
# structured HTML as a variable
# This step could be eliminated by immediately parsing & printing ONLY the title, however doing
# it this way would allow us in the future to do further extractions or processing more easily.
PAGE_CONTENT = BeautifulSoup(PAGE_RESPONSE.content, "html.parser")

# Here we are using BeautifulSoup's find method to scan the document and return the entire
# Title tag.
# To make this even cleaner, we could munge this to remove the HTML tag, but not for this
# exercise.
PAGE_TITLE = PAGE_CONTENT.find('title')

# This prints the title to the console!
print(PAGE_TITLE)

from bs4 import BeautifulSoup
import requests

page_url = 'https://twitter.com/adamlaz'

page_response = requests.get(page_url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

page_title = page_content.find('title')

print(page_title)

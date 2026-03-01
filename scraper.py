import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: python scraper.py URL")
    sys.exit()
url_to_fix = sys.argv[1]
if not url_to_fix.startswith("http://") and not url_to_fix.startswith("https://"):
    url_to_fix = "https://" + url_to_fix


my_headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url_to_fix, headers=my_headers)

data = BeautifulSoup(page.text, "html.parser") 
if data.title:
    print("Page Title:", data.title.string)

for extra in data(["script", "style"]):
    extra.decompose()

full_body = data.get_text(separator=" ", strip=True)
print("\nBody Content:")
print(full_body)

print("\nList of Links:")
for link in data.find_all('a'):  
    address = link.get('href')
    if address:

        print(address)


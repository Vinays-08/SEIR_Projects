import sys
import requests
from bs4 import BeautifulSoup

#take URL from the user
if len(sys.argv) < 2:
    print("Usage: python scraper.py URL")
    sys.exit()
url_to_fix = sys.argv[1]

#Get the page data
my_headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url_to_fix, headers=my_headers)

#Start the parser
data = BeautifulSoup(page.text, "html.parser")

  # Get Title 
if data.title:
    print("Page Title:", data.title.string)

#Clean and Get Body Text
for extra in data(["script", "style"]):
    extra.decompose()

#Get all text from the body
full_body = data.get_text(separator=" ", strip=True)
print("\nBody Content:")
print(full_body)

#Get All Links
print("\nList of Links:")
for link in data.find_all('a'):  #check if the'a'tag actually has a link (href)
    address = link.get('href')
    if address:
        print(address)
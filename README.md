# Web Scraping & Simhash Project

This is my assignment for Project 1 and Project 2. The goal of this project is to learn how to fetch data from websites and compare two different pages to see how much they are similar using a 64-bit Simhash.

##  What's inside?

1. **scraper.py**: This is my script for Project 1. It takes a URL and prints out the Page Title, the main Body text, and all the Links found on that page.
2. **simhash_compare.py**: This is for Project 2. It takes two URLs, calculates their 64-bit fingerprints, and tells us the "Common Bits" between them.
---
## How it Works
### Part 1: Web Scraper (Project 1)
* **Title:** Uses BeautifulSoup to find the `<title>` tag.
* **Cleaning:** I used the `.decompose()` method to remove `<script>` and `<style>` tags so we don't get junk code in our text output.
* **Links:** It loops through all `<a>` tags and grabs the `href` attribute.

### Part 2: Simhash & Similarity (Project 2)
* **Word Counting:** The script cleans the text and counts how many times each word appears.
* **Hashing:** I used a Polynomial Rolling Hash with a prime number (p=53) to turn words into numbers.
* **64-bit Vector:** It creates a list of 64 zeros and updates them based on the word hash and its frequency.
* **Comparison:** It uses the `XOR` (^) operator to compare the two final fingerprints.
---
##  How to run it on your machine
First, you need to install the libraries:
```bash
pip install requests beautifulsoup4








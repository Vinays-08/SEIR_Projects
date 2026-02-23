import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 3:
    print("Error: Enter two URL to run script")
    sys.exit()

u1 = sys.argv[1]
u2 = sys.argv[2]

def get_page_text(link):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(link, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup.get_text()
        else:
            print("Site is not opening:", link)
            return ""
    except:
        print("Network issue with", link)
        return ""

def get_freq(content):
    counts = {}
    words_list = content.lower().split()
    
    for w in words_list:
        clean_w = ""
        for char in w:
            if char.isalnum():
                clean_w += char
        
        if clean_w:
            if clean_w in counts:
                counts[clean_w] += 1
            else:
                counts[clean_w] = 1
    return counts

def make_hash(word):
    p = 53
    m = 2**64
    val = 0
    pow_val = 1
    
    for s in word:
        val = (val + ord(s) * pow_val) % m
        pow_val = (pow_val * p) % m
    return val

def get_simhash_val(word_counts):
    v = [0] * 64
    
    for word, count in word_counts.items():
        h = make_hash(word)
        for i in range(64):
            if (h >> i) & 1:
                v[i] += count
            else:
                v[i] -= count
    fingerprint = 0
    for i in range(64):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint

txt1 = get_page_text(u1)
txt2 = get_page_text(u2)

f1 = get_freq(txt1)
f2 = get_freq(txt2)

sh1 = get_simhash_val(f1)
sh2 = get_simhash_val(f2)

xor_val = sh1 ^ sh2
diff_bits = bin(xor_val).count('1')
matching = 64 - diff_bits

print("Site 1 Simhash:", sh1)
print("Site 2 Simhash:", sh2)
print("-" * 20)
print("Common Bits Found:", matching)
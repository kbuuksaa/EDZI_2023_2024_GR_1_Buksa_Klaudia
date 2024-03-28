#!/usr/bin/env python
# coding: utf-8

# In[83]:


import requests
from bs4 import BeautifulSoup
import random
from urllib.parse import urljoin

def get_links(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    links = bs.find_all('a', href=True)
    absolutes = [urljoin(url, link['href']) for link in links if link['href'].startswith('http')] #poszerzeone o nieprawidlowelinki typu javascript:void(0);
    
    return absolutes

def main():
    page_number = 1
    website_url = "https://www.onet.pl/"
    print(f"Strona {page_number}: {website_url}")
    
    visited_links = set()
    visited_links.add(website_url)
    
    page_number = 2
    while len(visited_links) < 100:
        current_url = random.choice(list(visited_links))
        links = get_links(current_url)

        if len(links) == 0 or (len(links) == 1 and links[0] == current_url):
            continue
            
        next_url = random.choice(links)
        if next_url not in visited_links:
            visited_links.add(next_url)
            print(f"Strona {page_number}: {next_url}")
            page_number += 1

if __name__ == "__main__":
    main()



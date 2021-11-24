#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Andrija Mićić
# https://www.studiobeograd.com/

import urllib.request
import re

#open web links 
def print_page(url):
  urlopen = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4723.0 Mobile Safari/537.36'
    }
)
  with urllib.request.urlopen(urlopen) as url:
    return url.read().decode('utf8')

#scan and open web links  
def scan_page_link_open(url):
  urlopen = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4723.0 Mobile Safari/537.36'
    }
)
  with urllib.request.urlopen(urlopen) as url:
    res = url.read().decode('utf8')
    regex_num = re.compile('<loc>(https:\/\/.+)<\/loc>')
    i = regex_num.findall(res)
    for x in i:
      if "xml" not in x:
        print (print_page(x))
      continue

def first(url):
  urlfirst = url
  with urllib.request.urlopen(urlfirst) as url:
    res = url.read().decode('utf8')
    regex_num = re.compile('<loc>(https:\/\/.+)<\/loc>')
    i = regex_num.findall(res)
    for x in i:
      if "xml" not in x:
        print (print_page(x))
      else:
        scan_page_link_open(x)
        
def main():
  url1 = "https://www.stadlerform.rs/sitemap_index.xml"

  first(url1)

  
if __name__ == "__main__":
    main()

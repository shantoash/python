# Import MODULES
import os
import requests
from bs4 import BeautifulSoup

# Input declarations

URL = input()
word = ' ' + input() + ' ' or '.' or ','
word1=word.lower()
# Import HTML

source_code = requests.get(URL)

# BeautifulSoup

soup = BeautifulSoup(source_code.text, "html.parser")

# BS4 format to String

string = str(soup)

# Print count 

print (string.count(word1))

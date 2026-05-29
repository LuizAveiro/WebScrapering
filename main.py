import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://example.com")

soup = BeautifulSoup (resposta.text, "html.parser")

print(soup.h1.text)
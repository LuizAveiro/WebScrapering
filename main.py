import requests
from bs4 import BeautifulSoup

# Acessa o site
resposta = requests.get("https://example.com")

# Verifica se funcionou
print("STATUS:")
print(resposta)

print("-" * 30)

# Analisa o HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# Título
print("TITLE:")
print(soup.title.text)

print("-" * 30)

# H1
titulo = soup.find("h1")

print("H1:")
print(titulo.text)

print("-" * 30)

# Parágrafo
paragrafos = soup.find_all("p")
print("PARÁGRAFO:")
print(paragrafos)

print("-" * 30)

for paragrafo in paragrafos:
    print(paragrafo)
    
print("-" * 30)

link = soup.find("a")
print(link.text)

print(link["href"])
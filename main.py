from scraper import (
    acessar_site,
    criar_soup,
    pegar_titulo,
    pegar_h1,
    pegar_paragrafos,
    pegar_link
)
# Acessa o site
resposta = acessar_site("https://example.com")

# Verifica se funcionou
print("STATUS:")
print(resposta)

print("-" * 30)

# Analisa o HTML
soup = criar_soup(resposta)

# Título
print("TITLE:")
print(pegar_titulo(soup))

print("-" * 30)

# H1
print("H1:")
print(pegar_h1(soup))

print("-" * 30)

# Parágrafo
paragrafos = pegar_paragrafos(soup)
print("PARÁGRAFO:")
print(paragrafos)

print("-" * 30)

for paragrafo in paragrafos:
    print(paragrafo)
    
print("-" * 30)

link = pegar_link(soup)
print(link.text)

print(link["href"])
import requests
from bs4 import BeautifulSoup

def acessar_site(url):
    resposta = requests.get(url)
    resposta.encoding = "utf-8"
    return resposta

def criar_soup(resposta):
    soup = BeautifulSoup(resposta.text, "html.parser")
    return soup

def pegar_titulo(soup):
    return soup.title.text

def pegar_h1(soup):
    return soup.find("h1").text

def pegar_paragrafos(soup):
    return soup.find_all("p")

def pegar_link(soup):
    return soup.find("a")

import requests
from bs4 import BeautifulSoup


def acessar_site(url):

    resposta = requests.get(url)

    return resposta


def criar_soup(resposta):

    soup = BeautifulSoup(resposta.text, "html.parser")

    return soup


def pegar_livros(soup):

    livros_html = soup.find_all("article", class_="product_pod")

    livros = []

    for livro in livros_html:

        titulo = livro.h3.a["title"]

        preco = livro.find("p", class_="price_color").text
        
        preco = preco.replace("Â£", "£")

        disponibilidade = livro.find(
            "p",
            class_="instock availability"
        ).text.strip()

        livros.append({
            "Titulo": titulo,
            "Preco": preco,
            "Disponibilidade": disponibilidade
        })

    return livros





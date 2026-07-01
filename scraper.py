import requests
from bs4 import BeautifulSoup

def acessar_site(url):
    resposta = requests.get(url)
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
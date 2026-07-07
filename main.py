import pandas as pd

from scraper import acessar_site, criar_soup, pegar_livros


todos_livros = []


for pagina in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"

    print(f"Coletando página {pagina}...")

    resposta = acessar_site(url)

    if resposta.status_code == 200:

        soup = criar_soup(resposta)

        livros = pegar_livros(soup)

        todos_livros.extend(livros)

    else:

        print(f"Erro ao acessar a página {pagina}")


tabela = pd.DataFrame(todos_livros)

tabela.to_excel("livros.xlsx", index=False)


print("Dados coletados com sucesso!")

print(f"Total de livros coletados: {len(todos_livros)}")
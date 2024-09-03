from utils.banco import dicio

def buscar_por_nome():
    while True:
        try:
            nome = str(input("Digite o nome do livro: "))
            if nome not in dicio:
                print(f"Esse livro não existe nos acervos da biblioteca.")
            else:
                print(f"Livro encontrado: Nome: {nome}, Autor: {dicio[nome]['autor']}, Ano: {dicio[nome]['ano']}")
            break
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")

def buscar_por_autor():
    livros_encontrados = []
    autor = str(input("Digite o nome do autor: "))
    for k, v in dicio.items():
        if v['autor'].lower() == autor.lower():
            livros_encontrados.append(k)
    if livros_encontrados:
        print("Livros encontrados:")
        for k in livros_encontrados:
            print(f"Nome: {k}, Autor: {dicio[k]['autor']}, Ano: {dicio[k]['ano']}")
    else:
        print(f"Nenhum livro do autor '{autor}' foi encontrado.")

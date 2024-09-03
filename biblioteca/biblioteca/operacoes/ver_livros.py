from utils.banco import dicio

def ver_livros():
    if not dicio:
        print("Nenhum livro cadastrado no sistema.")
    else:
        print("Livros cadastrados no sistema:")
        for nome, info in dicio.items():
            print(f"Nome: {nome}, Autor: {info['autor']}, Ano: {info['ano']}")

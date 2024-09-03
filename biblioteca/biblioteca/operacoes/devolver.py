from utils.banco import dicio

def devolver_livro():
    livro = str(input("Digite o nome do livro a ser devolvido: "))
    if livro in dicio:
        print(f"O livro '{livro}' foi devolvido com sucesso.")
    else:
        print(f"O livro '{livro}' não está registrado no acervo.")

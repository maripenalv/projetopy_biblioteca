from menu.menu import exibir_menu
from cadastro.cadastro import cadastrar_livro
from busca.busca import buscar_livro_por_nome, buscar_livro_por_autor
from emprestimo.emprestimo import emprestar_livro, devolver_livro
from visualizar.visualizar import ver_livros

def main():
    dicio = {}
    exibir_menu()

    while True:
        try:
            opera = int(input("Escolha uma das operações abaixo: \n1. Cadastrar livros \n2. Buscar livro por nome \n3. Buscar livro por autor \n4. Emprestar livro \n5. Devolução de livro \n6. Ver livros no sistema \n7. sair\n"))
            print(45 * "=")

            if opera < 1 or opera > 7:
                print("Erro. Escolha apenas o número de uma das operações.")
                print()
            elif opera == 1:
                cadastrar_livro(dicio)
                print(45 * "=")
            elif opera == 2:
                buscar_livro_por_nome(dicio)
                print(45 * "=")
            elif opera == 3:
                buscar_livro_por_autor(dicio)
                print(45 * "=")
            elif opera == 4:
                emprestar_livro(dicio)
                print(45 * "=")
            elif opera == 5:
                devolver_livro(dicio)
                print(45 * "=")
            elif opera == 6:
                ver_livros(dicio)
                print(45 * "=")
            elif opera == 7:
                print("Saindo do sistema.")
                break

        except ValueError:
            print("Erro. Digite um número inteiro.")
            print()

if __name__ == "__main__":
    main()

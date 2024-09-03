from operacoes import cadastrar, buscar, emprestar, devolver, ver_livros

def main():
    print()
    print("Bem vindo ao sistema da Biblioteca da Cidade")
    print(45 * "=")
    print(12 * " ", "O P E R A Ç Õ E S")
    print(45 * "=")

    while True:
        try:
            print()
            opera = int(input(
                "Escolha uma das operações abaixo: \n1. Cadastrar livros \n2. Buscar livro por nome \n3. Buscar livro por autor \n4. Emprestar livro \n5. Devolução de livro \n6. Ver livros no sistema \n7. Sair\n"))
            print(45 * "=")
            if opera < 1 or opera > 7:
                print("Erro. Escolha apenas o número de uma das operações.")
                print()
            elif opera == 1:
                cadastrar.cadastrar_livro()
            elif opera == 2:
                buscar.buscar_por_nome()
            elif opera == 3:
                buscar.buscar_por_autor()
            elif opera == 4:
                emprestar.emprestar_livro()
            elif opera == 5:
                devolver.devolver_livro()
            elif opera == 6:
                ver_livros.ver_livros()
            elif opera == 7:
                print("Saindo do sistema.")
                break

        except ValueError:
            print("Erro. Digite um número inteiro.")
            print()
            continue

if __name__ == "__main__":
    main()

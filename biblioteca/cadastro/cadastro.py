def cadastrar_livro(dicio):
    print("Cadastre o nome do livro, o autor e o ano que foi escrito")
    cad_nome = input("Digite o nome do livro: ")
    cad_autor = str(input("Digite o nome do autor: "))
    cad_ano = int(input("Digite o ano de publicação do livro: "))
    if cad_nome in dicio:
        print("Esse livro já está cadastrado!")
    else:
        dicio[cad_nome] = {"autor": cad_autor, "ano": cad_ano}
        print(f"O livro '{cad_nome}' foi cadastrado com sucesso!")

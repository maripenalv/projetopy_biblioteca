def ver_livros(dicio):
    if not dicio:
        print("Nenhum livro cadastrado no sistema.")
    else:
        print("Livros cadastrados no sistema:")
        for nome, info in dicio.items():
            print(f"Nome: {nome}, Autor: {info['autor']}, Ano: {info['ano']}")

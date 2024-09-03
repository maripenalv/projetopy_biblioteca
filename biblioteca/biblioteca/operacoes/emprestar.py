from datetime import datetime
from utils.banco import dicio

def emprestar_livro():
    while True:
        try:
            livro = str(input("Digite o nome do livro a ser emprestado: "))
            if livro in dicio:
                pessoa = str(input("Por favor, escreva o nome e sobrenome da pessoa que ficará com o livro: "))
                hoje = datetime.now()
                hoje_str = hoje.strftime("%d/%m/%Y")
                print(f"Data de hoje: {hoje_str}")
                data = input(f"Digite a data de devolução do livro (formato dd/mm/aaaa): ")
                data_devolucao = datetime.strptime(data, "%d/%m/%Y")
                if data_devolucao < hoje:
                    print("Erro. A data de devolução não pode ser anterior à data de hoje.")
                else:
                    print(f"Nome: {pessoa}. Livro: {livro}. Data de devolução: {data_devolucao.strftime('%d/%m/%Y')}.")
                    break
            else:
                print(f"O livro '{livro}' não está disponível no acervo.")
                break
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")

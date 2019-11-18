

def adicionar():
    nome_atividade = input("Escolha um nome para a atividade: ")
    data_atividade = input("Insira uma data de entrega para a atividade: ")
    descricao_atividade = input("Insira uma descrição para a sua atividade: ")

    print(nome_atividade)
    print(data_atividade)
    print(descricao_atividade)


def main():
    adicionar()

if __name__ == "__main__":
    main()
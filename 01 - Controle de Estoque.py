estoque = {}
opcao = 0

while opcao != 3:
    print("MENU:")
    print("1 - Adicionar Produto")
    print("2 - Consultar Produto")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        if nome_produto in estoque:
            estoque[nome_produto] += quantidade
            print("Quantidade atualizada!")
        else:
            estoque[nome_produto] = quantidade
            print("Produto adicionado!")

    elif opcao == 2:
        nome_produto = input("Digite o nome do produto para consulta: ")
        if nome_produto in estoque:
            print("Quantidade disponível:", estoque[nome_produto])
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Opção inválida! Tente novamente.")
pessoas = {}
while True:
    nome = input("\nInforme o primeiro nome da pessoa: ")
    idade_str = input(f"Idade de {nome}: ")
    if idade_str.isdigit():
        pessoas[nome] = int(idade_str)
    else:
        print("Idade inválida.")
        
    maiores = {n: i for n, i in pessoas.items() if i >= 18}

    if maiores:
        print("\nPessoas maiores de idade:")
        for nome, idade in maiores.items():
            print(f"- {nome}: {idade}")
    else:
        print("Não há pessoas maiores de idade.")
import random

numero_escolhido = random.randint(1, 10)

print('''
------ Jogo da Adivinhação ------
      
Escolhi um número entre 1 e 10. 
      
Tente adivinhar qual é!
      
---------------------------------''')

while True:
    palpite_inicial = input("\nDigite seu palpite: ")

    if palpite_inicial.isdigit():
        palpite_do_jogador = int(palpite_inicial)

        if palpite_do_jogador == numero_escolhido:
            print(f"\nParabéns! Você acertou! O número escolhido é {numero_escolhido}.\n")
            break
        else:
            print("\nNão foi desta vez. Tente novamente...")
    else:
        print("\nPor favor, digite um número inteiro.")
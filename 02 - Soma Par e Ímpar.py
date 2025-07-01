soma_pares = 0
soma_impares = 0

numero = int(input("Digite um número positivo (ou negativo para sair): "))

while numero >= 0:
    if numero % 2 == 0:
        soma_pares += numero
        print("Número", numero, "é PAR.")
    else:
        soma_impares += numero
        print("Número", numero, "é ÍMPAR.")
    
    numero = int(input("Digite outro número (ou negativo para sair): "))

print("Processo encerrado.")
print("Soma total dos números PARES:", soma_pares)
print("Soma total dos números ÍMPARES:", soma_impares)

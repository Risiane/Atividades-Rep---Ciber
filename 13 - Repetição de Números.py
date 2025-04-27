lista = [3, 7, 1, 9, 5, 2, 8, 3, 6, 4, 1, 7, 9, 2, 5, 8, 6, 3, 4, 1]
numero_solicitado = int(input("Digite o número que você quer contar: "))

quantidade = 0
for numeros in lista:
  if numeros == numero_solicitado:
    quantidade += 1

print(f"O número {numero_solicitado} aparece {quantidade} vezes na lista.")
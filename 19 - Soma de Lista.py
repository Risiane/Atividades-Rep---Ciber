def somar_lista(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma

lista_informada = (input("Informe os números da lista separando por espaço: "))
lista_antepenultima = lista_informada.split()
lista_penultima = [int(numero) for numero in lista_antepenultima]
lista_final = somar_lista(lista_penultima)
print(f"A soma dos números informados é: {lista_final}")
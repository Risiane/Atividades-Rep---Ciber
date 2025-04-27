numeros = []
for informado in range(5):
  informado = float(input("Informe um número: "))
  numeros.append(informado)

print(f"O maior número é o {max(numeros)}")
print(f"O menor número é o {min(numeros)}")

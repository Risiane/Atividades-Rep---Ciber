valor = int(input("Digite o valor: "))

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

notas1 = valor

print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 20:", notas20)
print("Notas de 10:", notas10)
print("Notas de 1:", notas1)

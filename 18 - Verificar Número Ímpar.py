def verificar_primo (n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

numero = int(input("Informe um número: "))

if verificar_primo(numero) == 0:
  print(f"O número {numero} é par.")
else:
  print(f"O número {numero} é ímpar.")
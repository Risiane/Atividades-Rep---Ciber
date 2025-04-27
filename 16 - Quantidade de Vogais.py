frase = input("Informe uma frase: ").lower()
vogais = "aeiou"
quantidade_vogais = 0

for letra in frase:
  if letra in vogais:
    quantidade_vogais += 1

print(f"A frase '{frase}' tem {quantidade_vogais} vogais.")
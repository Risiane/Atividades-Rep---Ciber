def calcular_media(num1, num2):
  media = (num1 + num2) / 2
  return media

num1 = float(input("Informe a primeira nota: "))
num2 = float(input("Informe a segunda nota: "))

media_final = calcular_media (num1, num2)
print(f"Sua média final é {media_final}.")
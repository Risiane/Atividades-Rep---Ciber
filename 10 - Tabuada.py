numero = int(input("Informe qual tabuada deseja visualizar: \n"))

for calculo in range (11):
    resultado = numero * calculo
    print(f"{numero} x {calculo} = {resultado}")

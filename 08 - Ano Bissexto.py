ano = int(input("Informe o ano:\n"))
calculo = ano % 4

if calculo == 0:
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto.")
import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ""

for i in range(12):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)

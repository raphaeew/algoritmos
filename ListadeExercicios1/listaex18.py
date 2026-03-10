soma = 0

numero = int(input("Digite um número: "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro número: "))

print("A soma é:", soma)
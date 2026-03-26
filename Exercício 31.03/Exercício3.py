try:
    numero = int(input("Digite um número: "))
    if numero > 10:
        print ("O número é válido.")
except ValueError:
    print ("Erro: digite um número válido.")
else:
    print ("Programa executado com sucesso!")
finally:
    print ("Programa encerrado!")
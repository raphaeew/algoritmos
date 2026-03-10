# 39. Crie um menu interativo simples usando while.

opcao = 0

while opcao != 3:

    print("1 - Oi")
    print("2 - Data")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá!")

    elif opcao == 2:
        print("hoje é dia de flamengo")

print("saindo...")
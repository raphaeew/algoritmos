try:
    saldo = float(input("Digite o saldo da conta: "))
    valor = float(input("Digite o valor que será transferido: "))
    if valor > saldo:
        raise ValueError ("Saldo insuficiente.")
    saldo -= valor
    print ("Transferência realizada com sucesso!")
    print ("Saldo restante:", saldo)
except ValueError as erro:
    print ("Erro:", erro)
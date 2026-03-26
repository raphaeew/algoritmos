try:
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite outro número inteiro: "))
    resultado = x/y 
    print (resultado)
except ZeroDivisionError:
    print ("Não foi possível concluir a ação, tente novamente!")
except:
    print ("Novamente, não foi possível!")
finally:
    print ("Ação encerrada!")
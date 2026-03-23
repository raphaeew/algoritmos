import random 
import time 

inicio = time.time()
lista = []

for i in range(100):
    lista.append(random.randint(1,100))

print(lista)
fim = time.time()

tempo_exec = fim - inicio 
print("O tempo de exec foi de: ")

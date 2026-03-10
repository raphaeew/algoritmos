# 22. Conte o número de vogais em uma string.

p = input("Digite uma palavra: ")

vogais = 0  

for letras in p: 
    if letras in "aeiouAEIOU":
        vogais = vogais + 1

print("quantidade de vogais: ",vogais)
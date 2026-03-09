a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a >= b and a >= c:
    print("O numero", a, "é maior.")
elif b >= a and b >= c:
   print("O numero", b, "é maior.")
else: 
    print("O numero", c, "é maior.")
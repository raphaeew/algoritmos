cores = {
    "vermelho": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255)
}
try:
    cor = input("Digite uma cor: ").lower()
    print ("RGB: ", cores[cor])
except KeyError:
    print ("Erro: essa cor não foi encontrada.")
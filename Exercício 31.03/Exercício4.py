class SenhaInvalida (Exception):
    pass
def verificar_senha (senha):
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
    if len (senha) < 8 or not tem_numero:
        raise SenhaInvalida ("A senha deve ter no mínimo 8 caracteres e 1 número.")
try:
    senha = input ("Digite uma senha: ")
    verificar_senha (senha)
    print ("Senha válida!")
except SenhaInvalida as erro:
    print ("Erro:", erro)
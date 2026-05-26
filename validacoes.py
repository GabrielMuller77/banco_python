def validar_nome(nome):
    if nome.isalpha():
        return True
    else:
        print("Digite um nome válido.")
        return False
    
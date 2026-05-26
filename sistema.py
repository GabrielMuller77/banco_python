import conta_corrente
import conta_poupanca
import menu
import validacoes
def iniciar():
    contas = {}
    while True:
        escolha = menu.opcoes()
        if escolha == "1":
            nome = input("Nome do titular: ")
            if validacoes.validar_nome(nome):
                contas[nome] = conta_corrente.ContaCorrente(nome)
                print(f"Conta Corrente criada para {nome}")
        elif escolha == "2":
            nome = input("Nome do titular: ")
            if validacoes.validar_nome(nome):
                contas[nome] = conta_poupanca.ContaPoupanca(nome)
                print(f"Conta Poupanca criada para {nome}")
        elif escolha == "3":
            nome = input("Nome do titular: ")
            if nome not in contas:
                print("Conta não encontrada!")
            else:
                try:
                    valor = float(input("Valor: "))
                    if valor <= 0:
                        print("Por favor digite um valor válido.")
                    else:
                        contas[nome].depositar(valor)
                except ValueError:
                    print("Por favor digite um valor válido.")
                except Exception as e:
                    print("Ocorreu um erro inesperado.")
        elif escolha == "4":
            nome = input("Nome do titular: ")
            if nome not in contas:
                print("Conta não encontrada.")
            else:
                try:
                    valor = float(input("Valor: "))
                    if valor <= 0:
                        print("Por favor digite um valor válido.")
                    else:
                        contas[nome].sacar(valor)
                except ValueError:
                    print("Por favor insira um valor válido.")
                except Exception as e:
                    print("Ocorreu um erro inesperado.")
        elif escolha == "5":
            nome = input("Nome do titular: ")
            if nome not in contas:
                print("Conta não encontrada.")
            else:
                contas[nome].ver_extrato()
        elif escolha == "6":
            nome = input("Nome do titular: ")
            if nome not in contas:
                print("Conta não encontrada!")
            else:
                if isinstance(contas[nome], conta_poupanca.ContaPoupanca):
                    contas[nome].render_juros()
                else:
                    print("Não é possível render juros nessa conta.")
        elif escolha == "0":
            print("Obrigado por utilizar o Banco.")
            break
        else:
            print("Tente novamente, opção inválida.")



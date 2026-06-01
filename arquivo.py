import json
import conta_corrente
import conta_poupanca
def salvar_arquivo(contas):
    dados = {}
    for nome, conta in contas.items():
        dados[nome] = {
            "Tipo": conta.tipo(),
            "Saldo": conta._saldo,
            "Extrato": conta._extrato
        }
    with open("contas.json", "w") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


        
def carregar_arquivo():
    try:
        with open("contas.json", "r") as f:
            dados = json.load(f)
            contas = {}
            for nome, info in dados.items():
                if info["Tipo"] == "Conta Corrente":
                    conta = conta_corrente.ContaCorrente(nome)
                else:
                    conta = conta_poupanca.ContaPoupanca(nome)
                conta._extrato = info["Extrato"]
                contas[nome] = conta
            return contas
    except FileNotFoundError:
        return {}
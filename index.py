menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
depositos = []
saques = []
numero_saques = 0
LIMITE_SAQUES = 3

def exibir_extrato():
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("\n============== Histórico de transações ==============")
        print(f"Limite diário de saque: {LIMITE_SAQUES}")
        print(f"Limite diário para saque de: R$ {limite:.2f}")
        print("======================== ### ========================")

        for deposito in depositos:
            print(f"Depósito : -----------------------  + R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque : --------------------------  - R$ {saque:.2f}")

    print(f"Saldo em conta :                      R$ {saldo:.2f}")
    print("======================= ### =========================")

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo += valor
        depositos.append(valor)
        print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso")
        print(f"Saldo atual R$ {saldo:.2f}")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))

        if saque > limite:
            print(f"Valor de R$ {saque:.2f} é superior ao seu limite diário de R$ {limite:.2f} para saque")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu seu limite diário de 3 saques")
            
        elif saldo >= saque:
            saldo -= saque
            saques.append(saque)
            numero_saques += 1
            print(f"Saque no valor de R$ {saque:.2f} realizado com sucesso")
            print(f"Saldo atual R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente para saque!")   

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada")



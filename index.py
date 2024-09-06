# menu = """

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# depositos = []
# saques = []
# LIMITE_SAQUES = 3

# extrato = f"""

# ============== Histórico de transações =============

# Limite diário de saque : {LIMITE_SAQUES}

# Limite diário para saque de : {limite}

# ======================= ### ========================

# Deposito : -----------------------  + {depositos[0]}
# Deposito : -----------------------  + {depositos[1]}
# Deposito : -----------------------  + {depositos[2]}
# Saque : --------------------------  - {saques[0]}
# Deposito : -----------------------  + {depositos[3]}

# Saldo em conta : R$ {saldo}

# ======================= ### ========================

# """

# while True:

#     opcao = input(menu)
    
#     if opcao == "d":
#         valor = float(input("Informe o valor do deposito: "))
#         saldo += valor
#         print(f"Deposito no valor de R$: {valor:.2f} reais realizado com sucesso")
#         print(f"Saldo atual R$ {saldo:.2f}")

#     elif opcao == "s":
#         saque = float(input("Informe o valor do saque:"))

#         if saque > limite:
#              print(f"Valor de R$ {saque:.2f} é superior ao seu limite diário de R$ {limite:.2f} para saque")
        
#         elif numero_saques >= LIMITE_SAQUES:
#             print("Você atingiu seu limite diário de 3 saques")
            
#         elif saldo >= saque:
#             saldo -= saque
#             print(f"Saque no valor de R$: {saque:.2f} reais realizado com sucesso")
#             print(f'Saldo atual R$ {saldo:.2f}')
#             numero_saques += 1
#         else:
#             print("Saldo insuficiente para saque!")   

#     elif opcao == "e":
#         print(f"{extrato}")

#     elif opcao == "q":
#         break

#     else:
#         print("Operacao inválida, por favor selecione a operacao desejada")

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



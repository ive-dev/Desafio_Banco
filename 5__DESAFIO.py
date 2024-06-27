menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

total_sacado = 0
depositos = []
saques = []
saldo = 0.0
limite = 500.0
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 1500.0

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        try:
            deposito = float(input("Valor do depósito: "))
            if deposito > 0:
                depositos.append(deposito)
                saldo += deposito
                print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
            else:
                print("Valor do depósito deve ser positivo.")
        except ValueError:
            print("Valor inválido, por favor digite um número.")
    
    elif opcao == "s":
        print("Saque")
        try:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque > 0:
                if saque <= saldo and numero_saques < LIMITE_SAQUES and saque <= limite and total_sacado + saque <= LIMITE_VALOR_SAQUE:
                    saldo -= saque
                    saques.append(saque)
                    total_sacado += saque
                    numero_saques += 1
                    print(f"Saque de R${saque:.2f} realizado com sucesso!")
                elif saque > saldo:
                    print("Saldo insuficiente.")
                elif numero_saques >= LIMITE_SAQUES:
                    print("Você atingiu o número máximo de saques no dia.")
                elif saque > limite:
                    print(f"Não é permitido realizar saque acima de R${limite:.2f}.")
                elif total_sacado + saque > LIMITE_VALOR_SAQUE:
                    print(f"Você atingiu o total diário de R${LIMITE_VALOR_SAQUE:.2f} para saques.")
            else:
                print("Valor do saque deve ser positivo.")
        except ValueError:
            print("Valor inválido, por favor digite um número.")
    
    elif opcao == "e":
        print("Extrato")
        print("Saques:")
        for saque in saques:
            print(f"R${saque:.2f}")
        print("Depósitos:")
        for deposito in depositos:
            print(f"R${deposito:.2f}")
        print(f"Saldo: R${saldo:.2f}")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
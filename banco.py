menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair


==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        
        menu_deposito = """Digite o valor a ser depositado:
        """
        
        valor_deposito = float(input(menu_deposito))
    
        def deposito (valor_deposito):
            global saldo
            global extrato
            if valor_deposito <= 0:
                print(f"Não foi possivel realizar a operação, não é permitido saldos negativos!")
            else:
                saldo+=valor_deposito
                extrato += f"O depósito de R${valor_deposito:.2f} \n"
                print(f"O depósito de R${valor_deposito:.2f} foi realizado com sucesso, seu novo saldo é de R${saldo:.2f}")
        
        deposito(valor_deposito)
        
        
        
    elif opcao == "s":
        menu_deposito_saque = """
        Digite o valor que deseja sacar 
        """
        valor_saque = float(input(menu_deposito_saque))
        
        
        def sacar (valor_saque):
            global saldo
            global extrato
            global numero_saques
            global LIMITE_SAQUES
            if valor_saque > saldo:
                print(f"Saldo insuficiente para realizar a operação, seu saldo é de R${saldo:.2f}")
            elif valor_saque > limite:
                print(f"O saque não pode ser superior a R${limite:.2f}")
            elif numero_saques >= LIMITE_SAQUES:
                print (f"Você antingiu o limite de saques diários")
            else: 
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque de R${valor_saque:.2f} \n"
                print(f"Seu saque de R${valor_saque:.2f} foi realizado com sucesso!")
                
        
        sacar(valor_saque)
                         
    elif opcao == "e":
        extrato_escopo = f"""
       ===============EXTRATO===============
        
{extrato}
        
        
Seu saldo atual é R${saldo:.2f}
        

        ====================================
        """
        print(extrato_escopo)

    elif opcao == "q":
        
        print("Obrigado por ser nosso cliente, até a próxima! ")
        
        break
    
    else: 
        print("Opção inválida, tente novamente!")

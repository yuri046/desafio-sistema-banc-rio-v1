saldo = 0.0
depositos = []
saques = []
LIMITE_SAQUE = 3
limite = 500.0

'''
    Exibe o menu e chama as outras funções do sistema
'''
def menu():
    while True:
        print('Menu\
            \n\n1. Depósito\
            \n2. Saque\
            \n3. Extrato\
            \n4. Sair\n')
        
        opcao = input('O que deseja fazer: ').upper()
        if opcao == '1' or opcao == 'DEPÓSITO':
            deposita_dinheiro(depositos)
        elif opcao == '2' or opcao == 'SAQUE':
            saca_dinheiro(saques)
        elif opcao == '3' or opcao == 'EXTRATO':
            exibe_extrato(depositos, saques)
        elif opcao == '4' or opcao == 'SAIR':
            print('\nSaindo...\n')
            break
        else:
            print('\nDigite uma opção válida\n')


'''
    Função para o depósito de dinheiro
'''

def deposita_dinheiro(depositos):
    global saldo
    while True:
        print('\nDepósito\
            \n\n1. Depositar\
            \n2. Sair')
        opcao = input('O que deseja fazer: ').upper()

        if opcao == '1' or opcao == 'DEPOSITAR':
            print(f'Saldo: {saldo:.2f}')
            deposito = float(input('Quanto você deseja depositar: R$ '))
            if deposito > 0:
                saldo += deposito
                depositos.append(deposito)
                print('\nDepósito feito com sucesso!\n')
            else:
                print('\nInsira um valor válido maior que 0\n')
        elif opcao == '2' or opcao == 'SAIR':
            print('\nSaindo...\n')
            break
        else:
            print('\nInsira uma opção válida')


'''
    Função para o saque de dinheiro
'''

def saca_dinheiro(saques):
    global saldo, limite
    while True:
        print('\nSaque\
              \n\n1. Sacar\
              \n2. Sair')
        opcao = input('O que deseja fazer: ').upper()

        if opcao == '1' or opcao == 'SACAR':
            print(f'Saldo: {saldo:.2f}')
            if len(saques) < LIMITE_SAQUE: 
                saque = float(input('Quanto você deseja sacar: R$ '))
                if saque > saldo:
                    print('Você não tem saldo suficiente')
                elif saque > limite:
                    print(f'Limite de saque excedido, o valor máximo é de R$ {limite:.2f}')
                elif saque <= saldo and saque > 0:
                    saldo -= saque
                    saques.append(saque)
                    print('\nSaque feito com sucesso!\n')
                else:
                    print('Insira um valor válido')
            else:
                print('Limite de saques do dia atingido\
                      \nSaindo...')
                break
        elif opcao == '2' or opcao == 'Sair':
                print('\nSaindo...\n')
                break
        else:
            print('Insira uma opção válida')


'''
    Função para o extrato bancário
'''
def exibe_extrato( depositos, saques):
    while True:
        print('\nExtrato\
              \n\n1. Exibir extrato\
              \n2. Sair')
        opcao = input('O que deseja fazer: ').upper()

        if opcao == '1' or opcao == 'EXIBIR EXTRATO':
            if len(depositos) > 0 or len(saques) > 0:
                print('\nEXTRATO\n')
                for deposito in depositos:
                    print(f'Depósito: {deposito:.2f}')
                for saque in saques:
                    print(f'Saque: {saque:.2f}')
                print(f'Saldo: {saldo:.2f}')
            else:
                print('Sua conta não possui movimentações')
        elif opcao == '2' or opcao == 'SAIR':
            print('\nSaindo...\n')
            break
        else:
            print('Insira uma opção válida')
                         

'''
    Chama a função menu
'''
menu()
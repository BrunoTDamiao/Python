# menu que irá ser vizualizado em tela.
print('~~'*20)
print('Seja Bem-Vindo ao Python Bancario!')
print('~~'*20)

menu = """

Selecione uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


"""
# variaveis definidas para o funcioanamento do loop
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
opcao = ''
confirm = ''
extrato = {}


while opcao != '4':
    opcao = (input(menu))
    # Primeira opção é a de deposito.
    if opcao == '1':
        print('Opção de depósito selecionada.')
        deposito = input('Digite quanto o valor que será depositado: R$ ')
        # logica feita para caso seja digitado algum dado invalido.
        while not deposito.isdigit():
            print('-'*20)
            print('Quantia Invalida. Digite apenas numeros.')
            print('-'*20)
            print('')
            deposito = input('Digite quanto o valor que será depositado: R$ ')
        else:
            deposito = float(deposito)
            # logica feita para caso não seja digitado "SIM" ou "NAO".
            confirm = input(f'Será depositado um valor total de R$ {deposito:.2f} reais.\n' 'Digite "SIM" para confirmar\n' 'Digite "NAO" para cancelar.\n' '->').upper()
            while True:
                if confirm == 'NAO':
                    print('Depósito cancelado.\n'
                        'Voltando ao menu principal.')
                    break
                elif confirm == 'SIM':
                    saldo += deposito
                    print('-'*20)
                    print(f'Depósito de R$ {deposito:.2f} Realizado com Sucesso!')
                    print('-'*20)
                    print('')
                    if 'depósitos' in extrato:
                        extrato['depósitos'].append(deposito)
                    else:
                        extrato['depósitos'] = [deposito]
                    break
                print('Digite apenas "SIM" ou "Não"')
                confirm = input('->').upper()
    # opção de saque
    elif opcao == '2':
        print('Opção de saque selecionada.')
        # condicional para verificar se o limite de saques foi atingido.
        if numero_saques == LIMITE_SAQUES:
            print('lIMITE DE SAQUE DIÁRIO ATINGIDA.')
            print('Voltando ao menu.')
        elif saldo > 0:
            print(f'Seu saldo: R$ {saldo:.2f}')
            saque = input('Digite o valor a ser sacado: R$ ')
        # logica feita para caso seja digitado algum dado invalido.
            while not saque.isdigit():
                print('-'*20)
                print('Quantia Invalida. Digite apenas numeros.')
                print('-'*20)
                print('')
                saque = input('Digite quanto o valor que será sacado: R$ ')
            saque = float(saque)
            # condicional feita para caso o valor do saque seja maior que o limite disponivel
            if saque > limite:
                print('Saque maior que o limite de R$ 500,00 reais.')
                print('Voltando ao menu...')
            # condicional feita para caso o valor seja maior que o saldo.
            elif saque > saldo:
                print('Saldo insuficiente.')
                print('Voltando ao menu...')
            else:
            # logica feita para caso não seja digitado "SIM" ou "NAO".
                confirm = input(f'Será sacado um valor total de R$ {saque:.2f} reais.\n' 'Digite "SIM" para confirmar\n' 'Digite "NAO" para cancelar.\n' '->').upper()
                while True:
                    if confirm == 'NAO':
                        print('-'*20)
                        print('Saque cancelado.\n'
                            'Voltando ao menu principal.')
                        print('-'*20)
                        print('')
                        break
                    elif confirm == 'SIM':
                        if 'saques' in extrato:
                            extrato['saques'].append(saque)
                        else:
                            extrato['saques'] = [saque]
                        saldo -= saque
                        print('-'*20)
                        print(f'Saque de R$ {saque:.2f} Realizado com Sucesso!')
                        print('-'*20)
                        print('')
                        numero_saques += 1
                        break
                    print('Digite apenas "SIM" ou "Não"')
                    confirm = input('->').upper()
        else:
            print('Saldo insuficiente.')
            print('Voltando ao menu...')
    #opção de mostrar o extrato.
    elif opcao == '3':
        # se nao tiver ocorrido nenhum deposito ou saque
        if len(extrato) == 0:
            print('-'*20)
            print('Extrato indisponivel.')
            print('Voltando ao menu...')
            print('-'*20)
        #mostra os saques e depositos que foram feitos.
        else:
            print('-'*20)
            print(f'Seus depositos: {extrato["depósitos"]}')
            print('-'*20)
            print(f'Seus saques: {extrato["saques"]}')
            print('-'*20)
            print(f'Saldo: R$ {saldo:.2f}')
    #encerra o programa.
    elif opcao == '4':
        print('-'*20)
        print('Saindo...\n'
              'Volte sempre!')
        print('-'*20)
    #repete o menu caso tenha sido inserido algum dado invalido.
    else:
        print('opção invalida.')

         






# MAIOR_IDADE = 18

# idade = int(input('Informe sua Idade: '))

# if idade >= 18:
#     print('Maior de Idade por tirar a CNH.')

# if idade < MAIOR_IDADE:
#     print('nao pode tirar CNH')

# if idade >= MAIOR_IDADE:
#     print('Pode tirar CNH')
# else:
#     print('Ainda não pode tirar cnh')

saldo = 0
saque = 500

status = "sucesso" if saldo >= saque else "falha"

print(f'{status} ao realizar o saque')
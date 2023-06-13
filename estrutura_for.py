texto = ''
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end='')
else:
    print()


for numero in range(0, 91, 9):
    print(numero)
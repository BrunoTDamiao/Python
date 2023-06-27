# C = int(input())
# for i in range(C):
#     i = int(input())
#     print('inseto') if i <= 8000 else print('Mais de 8000')

# T = int(input())

# for i in range(T): N, K = input().split()

# N = int(N)
# K = int(K)

# garrafas = int((N / K) + (N % K ))

# print(garrafas)1

a = input() 
b = input() 
c = input() 

def animal(a,b,c):
  animais = {
    'vertebrado':{
        'ave':{'carnivoro': 'aguia', 'onivoro':'pomba'},
        'mamifero':{'onivoro': 'homem', 'herbivoro':'vaca'}
    },
    'invertebrado':{
        'inseto':{'hematofago': 'pulga', 'herbivoro':'lagarta'},
        'anelideo':{'hematofago': 'sanguessuga', 'onivoro':'minhoca'}
    }
}
  return print(animais[a][b][c])

animal(a,b,c)
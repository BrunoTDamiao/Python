# T = input()


# print("TWEET") if len(T) >= 1 and len(T) == 140 else print("menor")

# for i in range(1, 140):
#     print(i, end='')

# month = int(input())

# months_dict = {
#     1:'January',
#     2:'February',
#     3:'March',
#     4:'April',
#     5:'May',
#     6:'June',
#     7:'July',
#     8:'August',
#     9:'September',
#     10:'October',
#     11:'November',
#     12:'December'
# }

# print(months_dict[month])

# N = int(input())

# while(N > 0):
#     A = input()
#     B = input()
#     A = str(A)
#     B = str(B)

#     if B == A[0:4]:
#         print('encaixa')
#     elif B == '':
#         print('encaixa')
#     else:
#         print('não encaixa')
#     N -= 1

N = int(input())

for _ in range(N):
    A, B = input().split()

    if A[-len(B):] == B:
        print('encaixa')
    else:
        print('nao encaixa')
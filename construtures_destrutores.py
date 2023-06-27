class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('removendo instancia da claase')

    def latir(self):
        print('au au')

def criar_cachorro():
    c = Cachorro('Kratos', 'Branco e bravo', False)
    print(c.nome)

c = Cachorro('sansao', 'preto')

c.latir()
criar_cachorro()
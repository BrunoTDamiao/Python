class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('ligando motor...')


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"sim" if self.carregado else "não"} estou carregado')

moto = Motocicleta('preta', 'abc-1234', 2)
moto.ligar_motor()

carro = Carro('branco', 'xde-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'gfd-3423', 8, 'sim')
caminhao.esta_carregado()
caminhao.ligar_motor()
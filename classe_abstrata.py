from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligar tv')
        print('ligado')

    def desligar(self):
        print('desligar tv')
        print('desligado')

    @property
    def marca(self):
        return 'LG'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('ligando ar condicionado')
        print('ligado')

    def desligar(self):
        print('desligando ar condicionado')
        print('ligado')
        
    @property
    def marca(self):
        return 'LG'


controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
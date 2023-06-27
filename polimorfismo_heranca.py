class Passaro:
    def voar(self):
        print('voando')

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print('avestruz não voa')

# FIXME: exemplo ruim do uso de herança para "ganhar" o metodo voar  
class Aviao(Passaro):
    def voar(self):
        print("Aviao voa")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())
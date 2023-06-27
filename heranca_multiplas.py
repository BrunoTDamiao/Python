class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)






class Gato(Mamifero):
    pass




class ornitorrinco(Mamifero, ave):
    pass

gato = Gato(nro_patas=4, cor_pelo='preto')

print(gato)

ornitorrinco = ornitorrinco(nro_patas=4, cor_pelo='verde', cor_bico='laranja')

print(ornitorrinco)
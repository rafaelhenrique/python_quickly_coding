class Foo(object):
    def __init__(self, valor):
        self.valor = valor
    def __call__(self):
        return self.trata()

f = Foo(56)

def trata(self):
    return self.valor * 2
Foo.trata = trata
print f()

def trata(self):
    return self.valor / 2.0
Foo.trata = trata
print f()

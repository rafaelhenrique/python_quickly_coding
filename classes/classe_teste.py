#!/usr/bin/python
class Pessoa(object):
    orelhas = 2 # Essa variavel eh comum a todas as instancias
    def __init__(self):
        """Essa funcao eh executada na inicializacao da classe"""
    def anda(self, para):
        print "Indo para %s"%(para)

pessoa = Pessoa()
pessoa.anda("Cubatao")
Pessoa.orelhas = 3
print pessoa.orelhas

#!/usr/bin/python
# -*- encoding: utf-8 -*-
class Pessoa(object):
    orelhas = 2 # Essa variavel é comum a todas as instancias
    def __init__(self, nome):
        """Essa funcao é executada na inicialização da classe"""
        self.nome = nome
    def __str__(self):
        return '%s tem %s orelhas'%(self.nome, self.orelhas)

    def anda(self, para):
        print "Indo para %s"%(para)


pessoa = Pessoa("Rafael")
pessoa.anda("Cubatão")
Pessoa.orelhas = 3
print pessoa

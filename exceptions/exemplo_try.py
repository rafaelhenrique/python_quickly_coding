#!/usr/bin/python
try:
    numero = int(raw_input("Digite um numero: "))
except ValueError,e:
    print 'Voce digitou um numero invalido: %s'%(e)

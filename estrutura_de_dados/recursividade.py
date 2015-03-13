#!/usr/bin/python

def numero( cont ) :
    print cont
    cont = cont + 1
    if ( cont < 10 ) :
        return numero(cont)

numero(3)

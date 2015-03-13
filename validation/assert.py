#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exemplo de uso do comando assert
# esta função testa se recebeu numero inteiro
# se não for cai em um erro

def teste(parametro):
    assert isinstance(parametro, int), "Erro: função recebe inteiros"

teste(1)
teste('a')

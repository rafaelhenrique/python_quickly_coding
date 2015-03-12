import os.path
# inspect: módulo de introspecção "amigável"
import inspect
print('Objeto:', inspect.getmodule(os.path))
print('Classe?', inspect.isclass(str))
# Lista todas as funções que existem em "os.path"
print('Membros:', end='')
for name, struct in inspect.getmembers(os.path):
    if inspect.isfunction(struct):
        print(name, end=' ')

import os
from time import time


def find_smart(path='.'):
    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in find_smart(fn):
                yield f
        else:
            yield fn


def find_burro(path='.'):
    arquivos = []
    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in find_smart(fn):
                arquivos.append(f)
        else:
            arquivos.append(f)
    return arquivos

tempo = time()
arquivos = find_burro('.')
for arquivo in arquivos:
    print(arquivo)
print("find_burro: ", time()-tempo)

print("="*5)

tempo = time()
arquivos = find_smart('.')
for arquivo in arquivos:
    print(arquivo)
print("find_smart: ", time()-tempo)

print("\nConclusão: Nem sempre compensa usar geradores.")

#print(globals()) # prints global namespace
#print(locals()) # prints local namespace

glob = 1
loc = 1


def foo():
    print("="*10, "foo", "="*10)
    loc = 5
    test = 6
    print("Locals: ", locals())
    print("Globals: ", globals())
    print('Verification loc in foo():', 'loc' in locals())
    print('Verification test in foo():', 'test' in locals())

if __name__ == "__main__":
    foo()
    print("="*10, "main", "="*10)
    print("Globals: ", globals())
    print('Verificarion loc in global:', 'loc' in globals())
    print('Verification test in globals:', 'test' in globals())
    print('Verification glob in global:', 'foo' in globals())

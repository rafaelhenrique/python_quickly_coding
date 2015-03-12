# Rule: Local/Enclosed/Global/Built-in

a_var = 'global value'


def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()

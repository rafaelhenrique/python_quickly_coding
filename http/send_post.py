import sys

try:
    import requests
except ImportError:
    print('Modulo requests nao instalado!')
    print('instale pelo pip: pip install requests')
    sys.exit(1)
except NameError:
    print('Modulo requests nao instalado!')
    print('instale pelo pip: pip install requests')
    sys.exit(1)

requests.post(
    'http://127.0.0.1:5000/product-create',
    data={'name': 'iPhone 5S', 'price': '549.0'})

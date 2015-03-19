prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

price_min = min(zip(prices.values(), prices.keys()))
price_max = max(zip(prices.values(), prices.keys()))

print(price_min)
print(price_max)

# Explicacao do zip
zipped = zip(prices.values(), prices.keys())
import ipdb; ipdb.set_trace()  # breakpoint
print(list(zipped))
print(list(zipped))  # somente podemos usar uma iteracao
                     # com o zip neste print o valor ja era

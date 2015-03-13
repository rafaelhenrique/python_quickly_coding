class Integer(int):
    def mult_two(self):
        return self * 2
    def exp(self):
        return self * self

numero = Integer(34)
print numero.mult_two()
print numero.exp()

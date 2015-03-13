class Foo:
     bar = []
 
f1 = Foo()
f2 = Foo()
f1.bar.append(1)
f2.bar.append(2)
f3 = Foo()
f3.bar
#>>> class Foo:
#...     bar = []
#... 
#>>> 
#>>> f1 = Foo()
#>>> f2 = Foo()
#>>> f1.bar.append(1)
#>>> f2.bar.append(2)
#>>> f3 = Foo()
#>>> f3.bar
#[1, 2]
#>>> 

#oposicão ao método de listas na classe
#>>> class Foo:
#...     bar = 1
#... 
#>>> f1 = Foo()
#>>> f2 = Foo()
#>>> f1.bar = 2
#>>> f2.bar+= 3
#>>> f3 = Foo()
#>>> f1.bar
#2
#>>> f2.bar
#4
#>>> f3.bar
#1
#>>> 

import functions as f
import math as m
import stack
import cola

c = cola.Cola()
p = stack.Stack()
p.meter("99")
p.meter("88")
p.meter("77")

print(p.s)
c.Poner("11")
c.Poner("22")
c.Poner("33")

print(c.s)
print("")
x = 0
aux = ""
while not p.vacia():
    aux = p.sacar(aux)
    c.Poner(aux)
    x += 1
for i in range(1, x+1):
    aux = c.Sacar(aux)
    p.meter(aux)

print(p.s)  
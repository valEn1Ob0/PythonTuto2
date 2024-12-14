# creamos un conjunto con "set()"
conjunto1 = set(["dato1","dato2"])

print("\n",conjunto1)

# creamos una tupla dentro de un conjunto
conjunto2 = set(["dato",("dato dentro de dato1")])

print("\n",conjunto2)

# creamos un conjunto dentro de otro conjunto con "frozenset()"
conjunto_in = frozenset(["datoin1","Datoin2"])
conjunto_on = {conjunto_in,"datoon1","dato2"}

print("\n",conjunto_on)

# teoria de conjuntos
super_conjunto = {1,3,5,7}
mini_conjunto = {1,3,7}

# preguntamos si "mini_conjunto" es subconjunto de "super_conjunto" con "issubset()"
result = mini_conjunto.issubset(super_conjunto)
print("\n",result)

# preguntamos quien es el miniconjunto con <= o >=
result2 = mini_conjunto <= super_conjunto
print("\n",result2) 

result3 = super_conjunto > mini_conjunto
print("\n",result3)

# lo mismo que en el caso anterior pero con diferentes perspectivas
result4 = super_conjunto.issuperset(mini_conjunto)
print("\n",result4)

# preguntamos si hay algun común con "isdisjoint()" si lo hay da "False" y si no los hay da "True"
result5 = super_conjunto.isdisjoint(mini_conjunto)
print("\n",result5)

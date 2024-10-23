
# Int dentro del rango precargado
a = 4
b = 4

print(id(a),id(b))
print(a is b)

# Ints fuera del rango precargado
c = 1000
d = 1000

print(id(c), id(d))
print(c is d)

# Bool
e = True
f = True
print('e es f (bool)', e is f)

# string

g = "hola como estas yo estoy bien"
h = "hola como estas yo estoy bien"

print('g es h(string)', g is h)

print(4, 5)
print((4, 5))

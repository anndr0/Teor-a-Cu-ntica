
def nomoduloClpx(c1):
    # Saca el modulo de un complejo representado como una tupla
    module = ((c1[0]) ** 2 + (c1[1]) ** 2)
    return module

def normaVector(v):
    suma = []
    for i in range(len(v)):
        mod = nomoduloClpx(v[i])
        suma.append(mod)
    return sum(list(map(int,suma)))

def superposition(vec, pos):
    c = nomoduloClpx(vec[pos])
    norma = normaVector(vec)
    super = c / norma
    return round(super, 7)

vec = [(-3, -1), (0, -2), (0, 1), (2, 0)]

print(superposition(vec, 2))
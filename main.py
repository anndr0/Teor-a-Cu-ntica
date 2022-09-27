import math

import numpy

"""1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular."""
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

"""2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo. """
def complejo(c):
    mod = abs(c)**2
    return mod

def normaVector2(v):
    suma = 0
    for i in range(len(v)):
        suma += complejo(v[i])
    return math.sqrt(suma)

def transition(vec1, vec2):
    productoInterno = numpy.inner(vec1, vec2)
    normaVec1 = normaVector2(vec1)
    normaVec2 = normaVector2(vec2)
    ket = productoInterno /( (normaVec1)*(normaVec2))
    return numpy.round(ket)

vec1 = [(-1j), (1)]
vec2 = [(1), (-1j)]
print(transition(vec1, vec2))



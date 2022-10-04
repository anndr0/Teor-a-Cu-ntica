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


""" 1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad
 de transitar de el uno al otro después de hacer la observación. """

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

"""2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea 
hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado. """


def tranpuestaMatriz(mat):
    # 7. Transpuesta de una matriz/vector
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j < i:
                nueva = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = nueva
    print(mat)


def conjugadaMatriz(mat):
    # 8. Conjugada de una matriz/vector
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = mat[i][j][0], (-1) * mat[i][j][1]
    print(mat)


def adjuntaMatriz(mat):
    # 9. Adjunta (daga) de una matriz/vector
    matriz = conjugadaMatriz(mat)
    matriz = tranpuestaMatriz(mat)
    print(matriz)


def probarHermitiana(mat):
    adjunta = adjuntaMatriz(mat)
    if mat == adjunta:
        return True
    else:
        return False

def accionMatrizVector(v, mat):
    # 11. Función para calcular la "acción" de una matriz sobre un vector.
    mat0 = [0 for i in range(len(v))]
    for i in range(len(v)):
        res = 0
        for j in range(len(v)):
            c1 = mat[i][j]
            c2 = v[j]
            res = sumaCplx(res, producto(c1, c2))
        mat0[i] = res
    print(mat0)

def sumaCplx(c1, c2):
    res = c1+c2
    return res

def producto(c1, c2):
    res = c1 * c2
    return res

def media(observable, vectorEstado):
    ishermitiana = probarHermitiana(observable)
    if ishermitiana == True:
        prod = accionMatrizVector(observable, vectorEstado)
        media = numpy.inner(prod, vectorEstado)
    return media

obs = [[1,-1j], [1j, 2]]
vecEstado = [math.sqrt(2)/2+0j, 0+math.sqrt(2j)/2]
print(media(obs, vecEstado))

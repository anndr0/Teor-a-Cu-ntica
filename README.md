# LABORATORIO # 3. TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
En esta librería podrás encontrar las simulaciones de algunos sistemas cuanticos descritos en la seccion 4.1 del libro ”Quantum Computing for Computer Scientist”, además de retos de programación del capítulo 4.

## Instalacion

Para comenzar a hacer uso de esta libreria, es necesario hacer la instalacion de la librería numpy. Digitando lo siguiente por medio de la terminal.

```python
pip install numpy
```

## CONTENIDO

En la primera parte, se encuentra un simulador que permite especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

Esta simulacion se divide en dos funciones. 

```python

def superposition(vec, pos):
    """
        Retorna la probabilidad de posicion dado un vector
        (list) -> float
    """
    c = sumaCuadrados(vec[pos])
    norma = normaVector(vec)
    super = c / norma ** 2
    return round(super, 4)

```

Que nos permite calcular la probabilidad de encontrarlo en una posicion en particular, y 

```python

def transition(vec1, vec2):
    """ Retorna la amplitud de una transición
        (list), (list) -> complex"""
    productoInterno = numpy.inner(vec1, vec2)
    normaVec1 = normaVector(vec1)
    normaVec2 = normaVector(vec2)
    ket = productoInterno / (normaVec1 * normaVec2)
    return numpy.round(ket)

```

en donde el sistema si se le da otro vector Ket, debe buscar la probabilidad de transitar del primer vector al segundo.

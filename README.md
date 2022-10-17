# LABORATORIO # 3. TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
En esta librería podrás encontrar las simulaciones de algunos sistemas cuanticos descritos en la seccion 4.1 del libro ”Quantum Computing for Computer Scientist”, además de retos de programación del capítulo 4.

## Instalación

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

Ahora bien,
### Los retos de programación.

1. ***Amplitud de transición.*** El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación.
    
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
    
2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, ***calcula la media y la varianza del observable en el estado dado.***
    1. Esta función llama a las funciones necesarias para comprobar si el observable es una matriz hermitiana, y de ser hacer, procede a hallar la media y la varianza.

    ```python
    def media(observable, vecEstado):
        media = 0
        ishermitiana = proobarHermitiana(observable)
        if ishermitiana == True:
            prod = accionMatrizVector(observable, vecEstado)
            media = innerProduct(prod, vecEstado)
        return media

    # print("La media es: ", media(obs, vecEstado))

    def varianza(observable, vecEstado):
        mediaC = media(observable, vecEstado)
        newMat = numpy.identity(len(observable))
        for i in range(len(newMat)):
            for j in range(len(newMat)):
                newMat[i][j] = newMat[i][j] * mediaC
        resta = numpy.matrix(observable) - numpy.matrix(newMat)
        resta = np.array(resta)
        producto = np.dot(resta, resta)
        var = media(producto, vecEstado)
        return var

    # print("La varianza es: ", varianza(obs, vecEstado))

    ```
### Problemas capítulo 4
En esta seccion se modelan los problemas 4.3.1, 4.3.2, 4.4.1, 4.4.2

#### Ejercicio 4.3.1

“Encuentre todos los estados posibles a los que puede pasar el sistema descrito en el ejercicio 4.2.2 después de que se haya llevado a cabo una medición.”
```python
def ejercicio_431(observable):
""" Find all the possible states the system described in Exercise 4.2.2
    can transition into after a measurement has been carried out.

    (list) -> float """
    spinX = [1, 0]
    spinX = numpy.array(spinX)
    prod = accionMatrizVector(observable, spinX)
    probabilidad = superposition(prod, 0)
    return probabilidad
```
#### Ejercicio 4.3.2

“Realice los mismos cálculos que en el último ejemplo, usando el Ejercicio 4.3.1. Luego dibuje la distribución de probabilidad de los valores propios como en el ejemplo anterior.”

```python
def ejercicio_431(observable):
""" Find all the possible states the system described in Exercise 4.2.2
    can transition into after a measurement has been carried out.

    (list) -> float """
    spinX = [1, 0]
    spinX = numpy.array(spinX)
    prod = accionMatrizVector(observable, spinX)
    probabilidad = superposition(prod, 0)
    return probabilidad
```

#### Ejercicio 4.4.1

“Comprueba que son matrices unitarias. Multiplíquelos y comprueba que su producto también es unitario.”

```python
def ejercicio_441(u1, u2):
    """Verify that are unitary matrices. Multiply them and verify that their product is also unitary.
    (list), (list) -> boolean, boolean, boolean"""
    
    u1 = numpy.matrix(u1)
    u2 = numpy.matrix(u2)
    isU1 = unitaria(u1)
    isU2 = unitaria(u2)
    producto = numpy.dot(u1, u2)
    productoUni = unitaria(producto)
    return isU1, isU2, productoUni
```

#### Ejercicio 4.4.2

“Regrese al Ejemplo 3.3.2 (bola de billar cuántica), mantenga el mismo vector de estado inicial [1, 0, 0, 0]T, pero cambie el mapa unitario a”

```python
def ejercicio_442(estadoInicial, mat):
    """Go back to Example 3.3.2 (quantum billiard ball), keep the same
    initial state vector [1, 0, 0, 0]T, but change the unitary map to """
    matriz = numpy.matrix(mat)
    estado = accionMatrizVector(estadoInicial, matriz)
    probabilidad = probabilidadTransicion(estado, 3)
    return probabilidad
```
## Ejecutando las pruebas
```python
In[0]: print("Probabilidad: ", superposition(vec=[(-3 - 1j), (-2j), 1j, 2], pos=2))
Out[1]: Probabilidad:  0.0526
```
```python
In[0]: print("Amplitud de transición: ", transition(vec1=[(-1j), 1], vec2=[1, (-1j)]))
Out[1]: Amplitud de transición:  -1j
```
```python
In[0]: obs = [[1, -1j], [1j, 2]]
In[1]: vecEstado = [math.sqrt(2) / 2 + 0j, (math.sqrt(2) / 2) * 1j]
In[2]: print("La media es: ", media(obs, vecEstado))
Out[3]: La media es:  (0.5+0j)
```
```python
In[0]: obs = [[1, -1j], [1j, 2]]
In[1]: vecEstado = [math.sqrt(2) / 2 + 0j, (math.sqrt(2) / 2) * 1j]
In[2]: print("La varianza es: ", varianza(obs, vecEstado))
Out[3]: La varianza es:  (0.25+0j)
```
```python
In[0]: obs = [[1, -1j], [1j, 2]]
In[1]: print("Los valores propios son: ", valPropio(obs), "y la probabilidad es ", probabilidadTransicion(obs, 2) )
```
```python
In[0]: observable = [[0, 1/2], [1/2, 0]]
In[1]: print(ejercicio431(observable))
Out[2]: [[2.5+0.j 0. +0.j]
        [0. +0.j 2.5+0.j]]
        (0.25+0j)
        0.0
```
```python
In[0]: observable = [[0, 1/2], [1/2, 0]]
In[1]: print(ejercicio431(observable))
Out[2]: [[2.5+0.j 0. +0.j]
        [0. +0.j 2.5+0.j]]
        (0.25+0j)
        0.0
```
```python
In[0]: u1 = [[0, 1], [1, 0]]
In[1]: u2 = [[math.sqrt(2) / 2, math.sqrt(2) / 2], [math.sqrt(2) / 2, (math.sqrt(2) / 2) * -1]]
In[2]: print(ejercicio_441(u1, u2))
Out[3]: (True, True, True)
```
```python
In[0]: unitaryMap = [[0, 1 / math.sqrt(2), 1 / math.sqrt(2), 0], [(1 / math.sqrt(2)) * 1j, 0, 0, 1 / math.sqrt(2)],
              [1 / math.sqrt(2), 0, 0, (1 / math.sqrt(2)) * 1j], [0, 1 / math.sqrt(2), (1 / math.sqrt(2)) * -1, 0]]
In[1]: initialVector = [1, 0, 0, 0]
In[2]: print(ejercicio_442(initialVector, unitaryMap))
Out[3]: 0.0
```
## Autor ✒️

* **Ana María Durán Burgos** - *Librería Operaciones con Números Complejos* - [anndr0](https://github.com/anndr0)

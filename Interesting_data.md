## Cadenas de documentación

Aquí hay algunas convenciones sobre el contenido y el formato de las cadenas de documentación.

La primera línea siempre debe ser un resumen breve y conciso del propósito del objeto. Por brevedad, no debe indicar explícitamente el nombre o tipo del objeto, ya que están disponibles por otros medios (excepto si el nombre es un verbo que describe la operación de una función). Esta línea debe comenzar con una letra mayúscula y terminar con un punto.

Si hay más líneas en la cadena de documentación, la segunda línea debe estar en blanco, separando visualmente el resumen del resto de la descripción. Las siguientes líneas deben ser uno o más párrafos que describan las convenciones de llamada del objeto, sus efectos secundarios, etc.

El analizador Python no elimina la sangría de los literales de cadena de varias líneas en Python, por lo que las herramientas que procesan la documentación deben eliminar la sangría si lo desean. Esto se hace usando la siguiente convención. La primera línea no en blanco después de la primera línea de la cadena determina la cantidad de sangría para toda la cadena de documentación. (No podemos usar la primera línea ya que generalmente es adyacente a las comillas de apertura de la cadena, por lo que su sangría no es aparente en el literal de la cadena). El espacio en blanco "equivalente" a esta sangría se elimina del principio de todas las líneas de la cadena . Las líneas con menos sangría no deben aparecer, pero si aparecen, se deben eliminar todos los espacios en blanco iniciales. La equivalencia del espacio en blanco debe probarse después de la expansión de las pestañas (a 8 espacios, normalmente).

**Existen herramientas que usan cadenas de documentos para producir automáticamente documentación en línea o impresa, o para permitir al usuario navegar interactivamente a través del código; es una buena práctica incluir cadenas de documentos en el código que escriba, así que hágalo.**

Aquí hay un ejemplo de una cadena de documentos de varias líneas:

```python
>>> def my_function():
        """Do nothing, but document it.

        No, really, it doesn't do anything.
        """
        pass

>>> print(my_function.__doc__)
    Do nothing, but document it.

        No, really, it doesn't do anything.
```

## Valores de argumento predeterminados

La forma más útil es especificar un valor predeterminado para uno o más argumentos.

**Advertencia importante**: el valor predeterminado se evalúa solo una vez. Esto marca la diferencia cuando el valor predeterminado es un objeto mutable, como una lista, diccionario o instancias de la mayoría de las clases. Por ejemplo, la siguiente función acumula los argumentos que se le pasan en llamadas posteriores:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```
Esto imprimirá:
```python
[1]
[1, 2]
[1, 2, 3]
```
Si no desea que el valor predeterminado se comparta entre llamadas posteriores, puede escribir la función de esta manera:
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

## Argumento de palabra clave

Argumento precedido por un identificador (p name=. ej. ) en una llamada a función o pasado como un valor en un diccionario precedido por **.Por ejemplo:
```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

Especifica un argumento que solo puede ser proporcionado por palabra clave. Los parámetros de solo palabras clave se pueden definir mediante la inclusión de un único parámetro de posición var o desnudo *en la lista de parámetros de la definición de función antes de ellos, por ejemplo kw_only1 y kw_only2 en lo siguiente:
```python
def func(arg, *, kw_only1, kw_only2):
```

**var-keyword**: especifica que arbitrariamente se pueden proporcionar muchos argumentos de palabras clave (además de cualquier argumento de palabras clave ya aceptado por otros parámetros). Dicho parámetro se puede definir anteponiendo el nombre del parámetro con **, por ejemplo, kwargs en el ejemplo siguiente:
```python
def func(**kwargs):
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
```
Se podría llamar así:
```python
func(shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")
```
## Argumento posicional

Un argumento que no es un argumento de palabra clave. Los argumentos posicionales pueden aparecer al comienzo de una lista de argumentos y / o pasarse como elementos de un iterativo precedido por *. Por ejemplo:
```python
complex(3, 5)
complex(*(3, 5))
```

Especifica un argumento que solo puede proporcionarse por posición. Los parámetros solo posicionales se pueden definir incluyendo un `/`carácter en la lista de parámetros de la definición de función después de ellos, por ejemplo posonly1 y posonly2 en lo siguiente:
```python
def func(posonly1, posonly2, /, positional_or_keyword):
```

**var-positional** : especifica que se puede proporcionar una secuencia arbitraria de argumentos posicionales (además de cualquier argumento posicional ya aceptado por otros parámetros). Dicho parámetro se puede definir anteponiendo el nombre del parámetro con *, por ejemplo, argumentos en lo siguiente:
```python
def func(*args)
```

## replace( * [, nombre] [, tipo] [, predeterminado] [, anotación] ) 

Cree una nueva instancia de parámetro basada en la instancia reemplazada en la que se invocó. Para anular un Parameteratributo, pase el argumento correspondiente. Para eliminar un valor predeterminado o una anotación de un parámetro, pase Parameter.empty.

```python
>>> from inspect import Parameter
>>> param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)
>>> str(param)
'foo=42'

>>> str(param.replace()) # Will create a shallow copy of 'param'
'foo=42'

>>> str(param.replace(default=Parameter.empty, annotation='spam'))
"foo:'spam'"
```
Modificado en la versión 3.4: en Python 3.3, los objetos de parámetro podían nameestablecerse en Nonesi kindse configuraron en POSITIONAL_ONLY. Esto ya no está permitido.


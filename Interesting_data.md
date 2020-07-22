## Cadenas de documentación

Aquí hay algunas convenciones sobre el contenido y el formato de las cadenas de documentación.

La primera línea siempre debe ser un resumen breve y conciso del propósito del objeto. Por brevedad, no debe indicar explícitamente el nombre o tipo del objeto, ya que están disponibles por otros medios (excepto si el nombre es un verbo que describe la operación de una función). Esta línea debe comenzar con una letra mayúscula y terminar con un punto.

Si hay más líneas en la cadena de documentación, la segunda línea debe estar en blanco, separando visualmente el resumen del resto de la descripción. Las siguientes líneas deben ser uno o más párrafos que describan las convenciones de llamada del objeto, sus efectos secundarios, etc.

El analizador Python no elimina la sangría de los literales de cadena de varias líneas en Python, por lo que las herramientas que procesan la documentación deben eliminar la sangría si lo desean. Esto se hace usando la siguiente convención. La primera línea no en blanco después de la primera línea de la cadena determina la cantidad de sangría para toda la cadena de documentación. (No podemos usar la primera línea ya que generalmente es adyacente a las comillas de apertura de la cadena, por lo que su sangría no es aparente en el literal de la cadena). El espacio en blanco "equivalente" a esta sangría se elimina del principio de todas las líneas de la cadena . Las líneas con menos sangría no deben aparecer, pero si aparecen, se deben eliminar todos los espacios en blanco iniciales. La equivalencia del espacio en blanco debe probarse después de la expansión de las pestañas (a 8 espacios, normalmente).

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

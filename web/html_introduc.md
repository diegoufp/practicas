# HTML

## Etiquetas

Hay etiquetas para todo.

- `<!DOCTYPE html>` : Esta etiqueta indica que se usara la ultima version de html y siempre se pondra en la primera lineal del codigo de html

- `<html></html>` : Esta etiqueta indica que lo que este dentro sera lo que este en la pagina web(tanto lo que podmeos ver como lo que no podemos ver). podemos poner un atributo `lang=""` para inticarle el lenguaje. Ejemplo: `<html lang="en">`

### Head
- `<head></head>` : En esta etiqueta pondremos todo lo que no podmeos ver en la pagina.

- `<link rel="icon" href="">` : nos permite poner un icono en la pesta;a del buscador, en `href` ira la ruta del archivo y es importante de la imagen tenga formato `.ico`

- `<title></title>` : Esta es la etiqueta de titulo en la pesta;a del navegador, esta etiqueta se pone dentro del `<head>`. Ejemplo: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
</html>
```
-  `<meta charset="UTF-8">` : Para trabajar metadatos con html lo hacemos con la etiqueta `meta`. El atributos `charset` nos permite cambiar la codificacion de la pagina. Otros metodos que se pueden poner en `meta` son `name="keywords"` y `content`, en `content` lo que se hace es poner todas las palabras clave que estan relacionadas con la pagina esto puede ayudar un poco es posicionamiento en buscadores.Ejemplo:

Cuando es `name="description"` en `content` tenemos que poner euna descripcion de la pagina de 70 a 140 caracteres. Cuando es `name="author"` en `content` tenemos que escribir quien es el autor de la pagina. Cuando es `name="conpyright"` en `content` tenemos que escribir el nombre de la empresa registrada due;a de los derechos de dicha empresa. `name="robots"` es para decirle a nuestra pagina si tiene que ser indexada o no endexada, en `content` tenemos que escribir `index` o `noindex`.Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title> <!-- > Se recomienda menos de 55 caracteres <-->
    <meta charset="UTF-8">
    <meta name="keywords" content="harina,leche,huevos">`
    <meta name="description" content="descripcion de la pagina"> <!-- > Se recomienda menos de 160 caracteres <-->
    <meta name="author" content="nombre del autor"> 
    <meta name="copyright" content="nombre de la empresa">
    <meta name="robots" content="index">
</head>
</html>
```
### Body
- `<body></body>` :  En esta etiqueta podemos podo lo que si se va a poder ver en la pagina.

- `<center></center>` centra todo lo que este dentro de la etiqueta. no se recomienda usarlo, se recomiendo usar css.

- `<h1></h1>` :  Esta etiqueta sirve para poser titulos y se pondra dentro del `<body>`.Esta etiqueta demas posiciona en buscadores(google por ejemplo). Existen del h1 al h6. Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>El h1 lo ideal es que solo lo pongamos una vez en toda la pagina</h1>
    <h2>h2 lo podemos ver varias veces</h2>
    <h3>h3 lo podmeos poner varias veces</h3>
    <h4>h4 lo podemos poner ilimitadamente</h4>
    <h5>h5 lo podemos poner ilimitadamente</h5>
    <h6>h6 lo podemos poner ilimitadamente</h6>
</body>
</html>
```

- `<p></p>` : Etiqueta de parrafo.

- `<b></b>` : Etiqueta de letras negritas. No compreta la linea.

- `<i></i>` : Etiqueta de estilo de letra italica. No completa la linea.

- `<strike></strike>` : Etiqueta para tachar las letras. No completa la linea

- `<small></small>` :  Etiqueta de tipo de letra chiquita. No completa la linea.

- `<div></div>` : Etiqueta de divisor. Para escribir un html correcto es buno trabajar con `div`, lo que hace es separar y agrupar contenido. 

- `<a href=""></a>` : La etiqueta `'a'` contendra un atributo que nos redirigira a otra ruta. Existen rutas internas y externas. Las internas son las que estan en nuestra carpeta y las externas son las que no se estan enlazando de manera local. Tambien puede contener otro atibuto para que se pueda abrir en una paesta;a aparte. Ejemplo: `<a href="" target="_BLANCK"></a>`. `<a href="#id"></a>` nos permite buscar dentro de la misma pagina una etiqueta con un `id` especifico.

- `<br>` : Esta etiqueta se cierra sola e indica un salto en linea. Esta etiqueta se abre pero no se cierra.

- `<ul></ul>` : Etiquetas listas desordenadas.

- `<ol></ol>` : Etiqueta lista ordena. Orneda las listas numericamente.

- `<li></li>` : Etiquela para enlistar. ESta etiqueta debe encontarse dentro de la etiqueta `<ul>` o `<ol>`. Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <ul>
        <li></li>
    </ul>
    <ol>
        <li></li>
    </ol>
</body>
</html>
```

- `<img src="" alt="">` : Esta etiqueta es para mostrar imagenes. No es necesario que se cierre la etiqueta. EL atributo `alt` nos va a ayudar para el ceo y en caso de que la imagen no se pueda buscar se va a escribir lo que ponemos en el `alt`. Tambien podemos poner ede atributo `title` que nos permite poner titulo a la imagen.

- `<video src=""></video>` : Esta etiqueta es para moestrar un video. Esta etiqueta ademas puede contener un atributo llamda `controls` que cuando lo dejamos vacio le estamos diciendo al navegador que ponga un control predeterminado para manejar el video. Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <video src="" controls></video>
</body>
</html>
```

- `<audio src="" controls></audio>` : Esta etiqueta es para moestrar un audio. Es vital que contenga el atributo `controls`.

#### Formularios
La etiqueta de formulario se debe encontrar dentro de la etiqueta body.

- `<form></form>` : Etiqueta de formularios

- `<input type="" name="">` : La etiqueta input se refiere a la entrada de datos, en el atributo `type` debemos escribir el tipo de dato que queremos.Esta etiqueta puede esta dentro de una etiqueta `form`. Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <form>
        <input type="text">
        <input type="password">
        <input type="number">
        <input type="email">
        <input type="color">
        <input type="range" min="1" max="5">
        <input type="date">
        <input type="button" value="boton">
        <input type="submit" value="">
        <input type="time">
    </form>
</body>
</html>
```
Tambien ewxisten otros tributos para las `input` los cuales son los `required`, este atributo dice que tenemos que completar el campo obligatoriamente para completar el formulario.El metodo `post` es enviar al servidor.Ejempplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <form metod="post">
        <input type="text" requered="" value="">
        <input type="password">
        <input type="number">
        <input type="email">
        <input type="color">
        <input type="range" min="1" max="5">
        <input type="date">
        <input type="button" value="boton">
        <input type="submit" value="">
        <input type="time">
    </form>
</body>
</html>
```

- `<textarea></textarea>` etiqueta que tambien funciona como un `input` pero tambien nos permite tener un campo se puede expandir. Se le puede agregar el atributo `readonly` la cual va a permitir solo leer y no se va a poder modificar.En css le puedes poner `resize: none` para que no se estire la caja.Ejemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <form metod="post">
        <textarea readonly="escribe algo"></textarea>
    </form>
</body>
</html>
```

## html semantico
Dentro del body lo ideal es que el `header` vaya en primer lugar el cual sera el encabezado y el cual incluira la barra de busqueda`nav`. El header siempre se mantiene igual para todas las paginas que creees.Ejemplo:
```html
<body>
    <header>
        <nav>
            <ul>
                <li>
                    <a href="index.html">Inicio</a>
                    <a href="micuenta.html">mi cuenta</a>
                    <a href="nosotros.html">sobre nosotros</a>
                </li>
            </ul>
        </nav>
    </header>
</body>
```
En segundo lugar estara el articulo`article` donde se dividira por secciones`section` si tiene mas de un artuclo.Ejmplo:
```html
<body>
    <header>
        <nav>
            <ul>
                <li>
                    <a href="index.html">Inicio</a>
                    <a href="micuenta.html">mi cuenta</a>
                    <a href="nosotros.html">sobre nosotros</a>
                </li>
            </ul>
        </nav>
    </header>
    <article>
        <section>
            <h1>
                Un titulo sorprendente
            </h1>
            <h2>
                Otro titulo sorprendente
            </h2>
            <p>
                Informacion del articulo
            </p>
        </section>
    </article>
</body>
```
En tercer lugar estara la barra de navegacion, el cual sera como un articulo secundario `aside`.Ejemplo:
```html
<body>
    <header>
        <nav>
            <ul>
                <li>
                    <a href="index.html">Inicio</a>
                    <a href="micuenta.html">mi cuenta</a>
                    <a href="nosotros.html">sobre nosotros</a>
                </li>
            </ul>
        </nav>
    </header>
    <article>
        <section>
            <h1>
                Un titulo sorprendente
            </h1>
            <h2>
                Otro titulo sorprendente
            </h2>
            <p>
                Informacion del articulo
            </p>
        </section>
    </article>
    <aside>
        <h2>Contenido extra</h2>
        <p>Informacion de los articulos</p>
    </aside>
</body>
```
Y por ultimo estara el `fooder` o pie de pagina el cual podria incluir informacion como informacion de contacto, copyright.Ejemplo:
```html
<body>
    <header>
        <nav>
            <ul>
                <li>
                    <a href="index.html">Inicio</a>
                    <a href="micuenta.html">mi cuenta</a>
                    <a href="nosotros.html">sobre nosotros</a>
                </li>
            </ul>
        </nav>
    </header>
    <article>
        <section>
            <h1>
                Un titulo sorprendente
            </h1>
            <h2>
                Otro titulo sorprendente
            </h2>
            <p>
                Informacion del articulo
            </p>
        </section>
    </article>
    <aside>
        <h2>Contenido extra</h2>
        <p>Informacion de los articulos</p>
    </aside>
    <footer>
        <h4>Copyright - Todos los derechos reservados</h4>
        <p>Siguenos en nuestras redes</p>
        <a href="instagram">instagram</a>
        <a href="facebook">facebook</a>
    </footer>
</body>
```

## Tablas
Hacer tablas con html, tienen filas y columnas.
Se inicializa con la etiqueta `<table></table>` y dentro de estas `<tr></tr>` nos ayudara a definir las filas, para definir los camplos por filas entonces tenemos que poner un `<td></td>` dentro de `tr`.Ejemplo:
```html
<body>
    <table>
        <tr>
            <td><b>Nombre</b></td>
            <td><b>Apellido</b></td>
        </tr>
        <tr>
            <td>Raul</td>
            <td>Gonzales</td>
        </tr>
    </table>
</body>
```

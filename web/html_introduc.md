# HTML

## Etiquetas

Hay etiquetas para todo.

- `<!DOCTYPE html>` : Esta etiqueta indica que se usara la ultima version de html y siempre se pondra en la primera lineal del codigo de html

- `<html></html>` : Esta etiqueta indica que lo que este dentro sera lo que este en la pagina web(tanto lo que podmeos ver como lo que no podemos ver). podemos poner un atributo `lang=""` para inticarle el lenguaje. Ejemplo: `<html lang="en">`

### Head
- `<head></head>` : En esta etiqueta pondremos todo lo que no podmeos ver en la pagina.

- `<title></title>` : Esta es la etiqueta de titulo en la pesta;a del navegador, esta etiqueta se pone dentro del `<head>`. Ejemplo: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
</html>
```
### Body
- `<body></body>` :  En esta etiqueta podemos podo lo que si se va a poder ver en la pagina.

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

- `<a href=""></a>` : La etiqueta `'a'` contendra un atributo que nos redirigira a otra ruta. Existen rutas internas y externas. Las internas son las que estan en nuestra carpeta y las externas son las que no se estan enlazando de manera local. Tambien puede contener otro atibuto para que se pueda abrir en una paesta;a aparte. Ejemplo: `<a href="" target="_BLANCK"></a>`

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

- `<img src="">` : Esta etiqueta es para mostrar imagenes. No es necesario que se cierre la etiqueta.

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

### Formularios
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
        <input type="range">
        <input type="date">
        <input type="button">
        <input type="submit">
        <input type="time">
    </form>
</body>
</html>
```
# Responsive Desing
Nosotros vamos a generar un analisis y ese analisis va  avenir desde una herramienta que se llama [Figma], esta es una herramienta que ocupan los dise;adores para sus wile frames. Una vez que ellos ya lo tengan listo te van a pasar a ti una url para que veas cietas especificaciones que te puedan ayudar a ti a comenzar con la arquitectura de tu proyecto.

## Estructura inicial de html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@300;500&display=swap" rel="stylesheet"> 
    <title>Document</title>
</head>
<body>
    <header></header>
    <main>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
    </main>
    <footer></footer>
</body>
</html>
```

## Estructura inicial de css
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
html{
    font-size: 62.5%; /* Esto para poder usar el rem */
    font-family: 'DM Sans', sans-serif;
}
```
## Imagenes

Es importante agrega imagenes e iconos, de ser posible en formato svg para que no se pixelien.

## Fuentes
Por recomendacion no agregar mas de dos fuentes.
Puedes buscar las fuentes en [google fonts](https://fonts.google.com "google fonts"). En esta ocacion usaremos las fuentes `'DM Sans'` y `'Inter'`.
No es recomendable agregar fuentes por `@import` y menos cuando son mas de una.

## Estilos base
Vamos a empezar a generar esos estilos base, vamos  autilizar varias variables que nos van a servir para tener una consistencia como el tipo de letra y el color. En esta ocacion usaremos estos colores:
```css
:root {
    /* Colores */
    --bitcoin-orange : #F7931A ;
    --soft-orange : #ffe9d5 ;
    --secundary-blue: #1a9af7 ;
    --soft-blue: #e7f5ff;
    --warm-back: #201e1c;
    --back: #282623;
    --grey: #bababa;
    --off-white: #faf8f7;
    --just-white: #fff;
}
```

## Estructura del header
Por buenas practicas una pagina web solo puede tener un `h1` por temas de seo.
la etiqueta `<span></span>` nos puede servir como una etiqueta comodin para cuando tengamos que poner iconos al lado de un texto.

Avance de la estrucutra basica del header:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        <img src="" alt="">
        <div>
            <h1>La próxima revolución en el intercambio de criptomonedas</h1>
            <p>Batatabit te ayuda a navegar entre los diferentes precios y tendencias</p>
            <a href=""> Conoce Nuestros Planes <span>i</span></a>
        </div>
    </header>
    <main>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
    </main>
    <footer></footer>
</body>
</html>
```

## Implementando BEM
No se recomienda poner una clase a las etiquetas que solo se usan una vez como `<header>`, `<footer>`, `<main>`, etc.
Las etiquetas `<div>` son muy comunes en un proyecto asi que son las que tiene mas comunmente las clases.La etiqueta`<div>` es un comodin que utilizamos cuando ya no exista una etiqueta que semanticamnete nos indique donde estamos, no se tienen que convertir en las etiquetas iniciales, son etiquetas de apoyo nadamas.

En la metodologia BEM se pone primero el bloque principal y despues el nombre del bloque:
```html
<header>
    <div class="header--title-container">
    </div>
</header>
```

Avances:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css">
    <title>Document</title>
</head>
<body>
    <header>
        <img src="./batata-bit/assets/img/logo.svg" alt="">
        <div class="header--title-container">
            <h1>La próxima revolución en el intercambio de criptomonedas</h1>
            <p>Batatabit te ayuda a navegar entre los diferentes precios y tendencias</p>
            <a href="" class="header--button"> Conoce Nuestros Planes <span>i</span></a>
        </div>
    </header>
    <main>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
    </main>
    <footer></footer>
</body>
</html>
```
```css
/*
1. Posicionamiento
2. Modelo caja (Box model)
3. Tipografia
4. Visuales
5. Otros
*/

:root {
    /* Colores */
    --bitcoin-orange : #F7931A ;
    --soft-orange : #ffe9d5 ;
    --secundary-blue: #1a9af7 ;
    --soft-blue: #e7f5ff;
    --warm-back: #201e1c;
    --back: #282623;
    --grey: #bababa;
    --off-white: #faf8f7;
    --just-white: #fff;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
html{
    font-size: 62.5%; /* Esto para poder usar el rem */
    font-family: 'DM Sans', sans-serif;
}

header {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    min-width: 320px;
    height: 334px;
    text-align: center;
}

header img {
    width: 150px;
    height: 240px;
    align-self: center;
    margin-top: 40px;
}

.header--title-container {
    width: 90%;
    min-height: 288px;
    max-width: 900px;
    height: 218px;
    text-align: center;
    align-self: center;
}
```

## Uso de linear-gradient

```css
background: linear-gradient(207.8deg, #201e1c 16.69%, #f7931a 100%);
```
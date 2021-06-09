# Webpack
## ¿Qué es Webpack?
<h4>Ideas/conceptos claves</h4>

Module bundlers son herramientas de frontend que nos permiten usar archivos con módulos JavaScript, entre otras características y convertiros a un JavaScript el cual el navegador pueda entender
<h4>Apuntes</h4>

- Webpack es una herramienta que nos permite preparar nuestro código para llevarlo a producción (module bundler)
- Webpack nos permite trabajar con:
    - HTML
    - CSS
    - JavaScript
    - Archivos estáticos
    - Imágenes
    - Fuentes
- Tambien nos permite tener un modo en desarrollo para nuestros proyectos para hacer pruebas
- Nacio en el 2012, desde ese entonces varias empresas lo usan como ser:
    - Twitter
    - Instagram
    - PayPal
- También nos permite
    - Gestionar dependencias
    - Ejecutar tareas
    - Conversión de archivos
- Nos permite trabajar en módulos
- Permitiéndonos tener un código separado en desarrollo, pero en producción en una fuente
- Webpack permite tener módulos de JS en formato
    - AMD
    - Common JS
    - ES15

RESUMEN: Webpack es un module bundler que nos permite trabajar con una variedad de tecnologías web empezando desde HTML y terminando con JS. Además de tener soporte para archivos estáticos

## Conceptos básicos
<h4>Ideas/conceptos claves</h4>

Webpack es un paquete de módulos estáticos para aplicaciones de JS modernas

Loader Te permite hacer un bundle de cualquier recurso estático más allá de JavaScript

Plugins Extienden recursos para añadir configuraciones y particularidades de recursos externos
<h4>Apuntes</h4>

    Webpack construye un gráfico de dependencias que mapea cada módulo para con verlo en uno o más módulos
    Desde webpack 4 ya no dependemos de tener un archivo de configuración, pero si debemos tener un punto de entrada
    Tambien tendremos que tener un punto de salida
        En este punto se creará nuestro proyecto una vez esté preparado
        Normalmente es la carpeta dist ⇒ Distribution
    Tambien contamos con diferentes modos
        Modo de desarrollo
        Modo de producción
        Modos de performance
            Donde tu añades
                Configuraciones de minificación
                Donde se va enviar
                Carpeta de destino
        Modos de desarrollo local
            Donde puedes
                Crear puertos específicos para tu proyecto
                Ver cambios en tiempo real
    Dispone de loader y plugins permitiéndonos preparar particularidades de nuestro proyecto


## Tu primer build con Webpack
Creamos una carpeta como le quieras llamar
(Bueno no! si eres de Windows te dejo este articulo cortito de los nombres de carpetas PROHIBIDOS )
La creamos desde la terminal con mkdir y luego entramos a ella con cd
```
mkdir curso-webpack
cd curso-webpack
```
una vez que entres a la carpeta inicializamos nuestro repositorio con git
```
git init
```
El paso que sigue es inicializar nuestro proyecto con npm y si no sabes de npm aqui esta el curso del profesor
```
npm init -y
```
o si les da error “Invalid Name” usen para personalizar la configuración
```
npm init
```
y para abrir el proyecto como flash es poner en la terminal y les abre el editor ( si usas VS CODE)
```
code .
```
La carpeta SRC es el source de todo el proyecto ( index.js , imágenes, utils, assets, helpers, database, etc).

** Instalación de Webpack**
si no quieres escribir ese comando también puedes usar este
la i de install
```
npm i webpack webpack-cli -D
```
o si usas yarn usa
```
yarn add webpack webpack-cli -D
```
Y luego ejecutamos webpack
npx lo que hace es ejecutar paquetes directamente de npm, este viene instalado de npm
```
npx webpack
```
Al hacer esto webpack creo una carpeta llamada dist, esto lo hace por defecto webpack sin preguntarnos.
Modo de desarrollo
Por defecto webpack al compilar nuestro proyecto setea el modo “production” implícitamente pero podemos definirle el modo explícitamente corriendo:
```
npx webpack --mode production
npx webpack --mode development
```
La diferencia radica que el modo development deja el código mas legible para los desarrolladores pero con comentarios, el modo production deja el código comprimido y mas limpio para usarse.

## Pasos de la clase

    Clonar el proyecto

    git clone https://github.com/gndx/js-portfolio.git

    Instalar webpack
    con npm

    npm install webpack webpack-cli -D 

    con Yarn

    yarn add webpack webpack-cli -D 

## Configuración de webpack.config.js
<h4>Apuntes</h4>

    El archivo de configuración nos va ayudar a poder establecer la configuración y elementos que vamos a utilizar
    Para poder crear el archivo de configuración en la raíz del proyecto creamos un archivo llamado webpack.config.js
    En el mismo debemos decir
        El punto de entrada
        Hacia a donde a enviar la configuración de nuestro proyecto
        Las extensiones que vamos usar

const path = require('path');

module.exports = {
  // Entry nos permite decir el punto de entrada de nuestra aplicación
  entry: "./src/index.js",
  // Output nos permite decir hacia dónde va enviar lo que va a preparar webpacks
  output: {
    // path es donde estará la carpeta donde se guardará los archivos
    // Con path.resolve podemos decir dónde va estar la carpeta y la ubicación del mismo
    path: path.resolve(__dirname, "dist"),
    // filename le pone el nombre al archivo final
    filename: "main.js"
  },
  resolve: {
    // Aqui ponemos las extensiones que tendremos en nuestro proyecto para webpack los lea
    extensions: [".js"]
  },
}

    El flag —config indica donde estará nuestro archivo de configuración
```
npx webpack --mode production --config webpack.config.js
```
o
```
npx webpack --mode production
```

    Para poder hacerlo más amigable el comando puedes crear un script en package.json

"scripts": {
		...
    "build": "webpack --mode production --config webpack.config.js"
  },

RESUMEN: Puedes crear un archivo webpack.config.js en el cual estarán las configuraciones con las cuales webpack trabajara, entre ellas están los puntos de entrada y salida, extensiones de archivos, entre otras características que se verán próximamente en él curso.

## Babel Loader para JavaScript
<h4>Apuntes</h4>

    Babel te permite hacer que tu código JavaScript sea compatible con todos los navegadores
    Debes agregar a tu proyecto las siguientes dependencias

NPM

npm install -D babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime

Yarn

yarn add -D babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime

    babel-loader nos permite usar babel con webpack
    @babel/core es babel en general
    @babel/preset-env trae y te permite usar las ultimas características de JavaScript
    @babel/plugin-transform-runtime te permite trabajar con todo el tema de asincronismo como ser async y await
    Debes crear el archivo de configuración de babel el cual tiene como nombre .babelrc

{
  "presets": [
    "@babel/preset-env"
  ],
  "plugins": [
    "@babel/plugin-transform-runtime"
  ]
}

    Para comenzar a utilizar webpack debemos agregar la siguiente configuración en webpack.config.js

{
...,
module: {
    rules: [
      {
        // Test declara que extensión de archivos aplicara el loader
        test: /\.js$/,
        // Use es un arreglo u objeto donde dices que loader aplicaras
        use: {
          loader: "babel-loader"
        },
        // Exclude permite omitir archivos o carpetas especificas
        exclude: /node_modules/
      }
    ]
  }
}

RESUMEN: Babel te ayuda a transpilar el código JavaScript, a un resultado el cual todos los navegadores lo puedan entender y ejecutar. Trae “extensiones” o plugins las cuales nos permiten tener características más allá del JavaScript común
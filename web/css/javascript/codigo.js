class Animal{
    contructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} y soy de color ${this.color}`;
    }
    verInfo(){
        document.write(this.info + "<br>")
    }
}

class Perro extends Animal {
    constructor(especie,edad,color,raza){
        super(especie,edad,color);
        this.raza = null;
    }
    // el setter es para para modificarlo o definirlo.
    // este es un metodo que se convierte a propiedad:
    set setRaza(newName){
        this.raza = newName;
    }
    // El getter es para obtener informacion.
    get getRaza(){
        return this.raza;
    }
}

const perro = new Perro("perro", 5, "marron", "doberman")
const gato = new Animal("gato", 2 , "negro")
const pajaro = new Animal("pajaro", 1, "verde")
// Raramente los Getters y Setters funcionan como propiedades. Entonces esta seria la forma erronea de hacerlo:
// perro.modificarRaza("pedro");
// la forma correcta seria:
perro.setRaza = "Pedro";
document.write(perro.getRaza)
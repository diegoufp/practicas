const cards = document.getElementById('cards');
const items = document.getElementById('items'); // se seleccionan los nuevos elementos d ela tabla
const footer = document.getElementById('footer'); // se seleccionan los nuevos elementos d ela tabla
const templateCard = document.getElementById('template-card').content;
const templateFooter = document.getElementById('template-footer').content;// se seleccionan los nuevos templates
const templateCarrito = document.getElementById('template-carrito').content;// se seleccionan los nuevos templates
const fragment = document.createDocumentFragment();
let carrito = {};

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
});

cards.addEventListener('click', e => {
    addCarrito(e);
})


const fetchData = async () => {
    try {
        
        const res = await fetch('api.json');
        const data = await res.json();
        pintarCards(data);

    } catch (error) {
        console.log(error);
    }
};

const pintarCards = data => {
    data.forEach(producto => {
        templateCard.querySelector('h5').textContent = producto.title;
        templateCard.querySelector('p').textContent = producto.precio;
        templateCard.querySelector('img').setAttribute("src", producto.thumbnailUrl);
        templateCard.querySelector('.btn-dark').dataset.id = producto.id; 
        const clone = templateCard.cloneNode(true);
        fragment.appendChild(clone)
    });
    cards.appendChild(fragment);
};

const addCarrito = e => {
    if(e.target.classList.contains('btn-dark')){
        setCarrito(e.target.parentElement);
    };
    e.stopPropagation();
};

const setCarrito = objeto => {
    
    const producto = {
        
        id: objeto.querySelector('.btn-dark').dataset.id,
        title: objeto.querySelector('h5').textContent,
        precio: objeto.querySelector('p').textContent,
        cantidad: 1
    };

    
    if(carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1;
    }
    
    carrito[producto.id] = { ...producto };
    pintarCarrito();
};

// ahora pintaremos lo del carrito en el dom
const pintarCarrito = () => {
    
    // para que no ocurra un error en el carrito que se dibujen duplicados vamos a partir de un innerHTM vacio
    items.innerHTML = ''

    // podemos hacer un forEach pero antes tenemos que usar un Object.values por que estamos trabajando con un objeto y no se pueden usar las funciones de los array
    Object.values(carrito).forEach(producto => {
        //este producto tenemos que pintarlo
        templateCarrito.querySelector('th').textContent = producto.id;
        templateCarrito.querySelectorAll('td')[0].textContent = producto.title;
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad;
        templateCarrito.querySelector('.btn-info').dataset.id = producto.id;
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.id;
        templateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio;

        const clone =  templateCarrito.cloneNode(true);
        fragment.appendChild(clone);
    })

    // ahora si lo estariamos pintando
    items.appendChild(fragment);
};
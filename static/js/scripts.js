function calcularTotal(){
    var precio_producto = document.getElementById('producto').value
    var cantidad = document.getElementById('cantidad').value

    document.getElementById('resultado').value = precio_producto*cantidad
}

function calcularUnidadTotal(){
    var precio_producto = document.getElementById('producto').value
    var cantidad = document.getElementById('cantidad').value

    document.getElementById('Precio/Unidad').value = precio_producto
    document.getElementById('Precio/Total').value = precio_producto*cantidad
}

function crearLinea(){
    var capa = document.getElementById("ordenes");
    var div = document.createElement("div");
    div.classList.add("row", "m-1")
    div.innerHTML = '<div class="col-2"><input class="form-control" id="cantidad" type="number" min="1" placeholder="0""></div><div class="col-4"><select name="producto" class="form-select texto-oscuro" id="producto"><option value=""></option></select></div><div class="col-3"><input class="form-control" id="Precio/Unidad" type="number" placeholder="0"></div><div class="col-3"><input class="form-control" id="Precio/Total" type="number" placeholder="0"></div>';
    // capa.appendChild(div);
    capa.insertBefore(div, ordenes.firstChild);
}

//<div class="col-2"><input class="form-control" id="cantidad" type="number" min="1" placeholder="0" onchange="calcularUnidadTotal()"></div><div class="col-4"><select name="producto" class="form-select texto-oscuro" id="producto" onchange="calcularUnidadTotal()">{% for producto in datos["productos"] %}<option value="{{ producto[2] }}">{{ producto[1] }}</option>{% endfor %}</select></div><div class="col-3"><input class="form-control" id="Precio/Unidad" type="number" placeholder="0"></div><div class="col-3"><input class="form-control" id="Precio/Total" type="number" placeholder="0"></div>

// document.body.onload = addElement;

// function addElement() {
// // crea un nuevo div
// // y añade contenido

// var newDiv = document.createElement("div");
// var newContent = document.createTextNode("Hola! ¿Qué tal?");
// newDiv.appendChild(newContent); //añade texto al div creado.

// // añade el elemento creado y su contenido al DOM
// var currentDiv = document.getElementById("div1");
// // document.body.insertBefore(newDiv, currentDiv);
// currentDiv.parentNode.insertBefore(newDiv, currentDiv);
// }
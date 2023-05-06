function calcularTotal(){
    var precio_producto = document.getElementById('producto').value
    var cantidad = document.getElementById('cantidad').value

    document.getElementById('resultado').value = precio_producto*cantidad
}



// function crearLinea() {
//     // Create a new row div
//     const newRow = document.createElement("div");
//     newRow.className = "row m-1";
  
//     // Create the cantidad div and input
//     const cantidadDiv = document.createElement("div");
//     cantidadDiv.className = "col-2";
//     const cantidadInput = document.createElement("input");
//     cantidadInput.id = "cantidad";
//     cantidadInput.name = "cantidad";
//     cantidadInput.className = "form-control";
//     cantidadInput.type = "number";
//     cantidadInput.min = "0";
//     cantidadInput.placeholder = "0";
//     cantidadDiv.appendChild(cantidadInput);
//     newRow.appendChild(cantidadDiv);
  
//     // Create the producto div and select element
//     const productoDiv = document.createElement("div");
//     productoDiv.className = "col-4";
//     const productoSelect = document.createElement("select");
//     productoSelect.id = "producto";
//     productoSelect.name = "producto";
//     productoSelect.className = "form-select texto-oscuro";
  
//     // Create the product options using a loop
//     const products = [
//       ["Juego de Cuellos Acrílico", "3800"],
//       ["Solo Cuello Acrílico", "2000"],
//       ["Solo Tira Acrílico", "2000"],
//       ["Juego de Cuello Letras", "5000"],
//       ["Cuello y Puño Letras", "6000"],
//       ["Solo Cuello Letras", "3500"],
//       ["Juego de Cuello Hilo", "4000"],
//       ["Solo Cuello Hilo", "2200"],
//       ["Juego Fajas Completo", "12000"],
//       ["Solo Faja Dobles", "6000"],
//       ["Cuello Redondo Doble", "4000"],
//     ];
//     for (let i = 0; i < products.length; i++) {
//       const productOption = document.createElement("option");
//       productOption.value = products[i][1];
//       productOption.textContent = products[i][0];
//       productoSelect.appendChild(productOption);
//     }
  
//     productoDiv.appendChild(productoSelect);
//     newRow.appendChild(productoDiv);
  
//     // Create the Precio/Unidad div and input
//     const precioUnidadDiv = document.createElement("div");
//     precioUnidadDiv.className = "col-3";
//     const precioUnidadInput = document.createElement("input");
//     precioUnidadInput.id = "Precio/Unidad";
//     precioUnidadInput.name = "Precio/Unidad";
//     precioUnidadInput.className = "form-control";
//     precioUnidadInput.type = "number";
//     precioUnidadInput.min = "0";
//     precioUnidadInput.placeholder = "0";
//     precioUnidadInput.value = productoSelect.value;
//     precioUnidadDiv.appendChild(precioUnidadInput);
//     newRow.appendChild(precioUnidadDiv);
  
//     // Create the Precio/Total div and input
//     const precioTotalDiv = document.createElement("div");
//     precioTotalDiv.className = "col-3";
//     const precioTotalInput = document.createElement("input");
//     precioTotalInput.id = "Precio/Total";
//     precioTotalInput.name = "Precio/Total";
//     precioTotalInput.className = "form-control";
//     precioTotalInput.type = "number";
//     precioTotalInput.min = "0";
//     precioTotalInput.placeholder = "0";
//     precioTotalInput.value = productoSelect.value * cantidadInput.value;
//     precioTotalDiv.appendChild(precioTotalInput);
//     newRow.appendChild(precioTotalDiv);
  
//     // Get the ordenes div and add the new row
//     const ordenesDiv = document.getElementById("ordenes");
//     ordenesDiv.appendChild(newRow);
  
//     // Event listeners to update the "Precio/Unidad" and "Precio/Total" input values
//     productoSelect.addEventListener("change", () => {
//       precioUnidadInput.value = productoSelect.value;
//       precioTotalInput.value = productoSelect.value * cantidadInput.value;
//     });
  
//     cantidadInput.addEventListener("change", () => {
//       precioTotalInput.value = productoSelect.value * cantidadInput.value;
//     });
//   }


  function crearLinea() {
    // Create a new row div
    const newRow = document.createElement("div");
    newRow.className = "row m-1";
  
    // Create the cantidad div and input
    const cantidadDiv = document.createElement("div");
    cantidadDiv.className = "col-1";
    const cantidadInput = document.createElement("input");
    cantidadInput.id = "cantidad";
    cantidadInput.name = "cantidad";
    cantidadInput.className = "form-control";
    cantidadInput.type = "number";
    cantidadInput.min = "0";
    cantidadInput.placeholder = "0";
    cantidadDiv.appendChild(cantidadInput);
    newRow.appendChild(cantidadDiv);
  
    // Create the producto div and select element
    const productoDiv = document.createElement("div");
    productoDiv.className = "col-4";
    const productoSelect = document.createElement("select");
    productoSelect.id = "producto";
    productoSelect.name = "producto";
    productoSelect.className = "form-select texto-oscuro";
  
    // Create the product options using a loop
    const products = [
      ["Juego de Cuellos Acrílico", "3800"],
      ["Solo Cuello Acrílico", "2000"],
      ["Solo Tira Acrílico", "2000"],
      ["Juego de Cuello Letras", "5000"],
      ["Cuello y Puño Letras", "6000"],
      ["Solo Cuello Letras", "3500"],
      ["Juego de Cuello Hilo", "4000"],
      ["Solo Cuello Hilo", "2200"],
      ["Juego Fajas Completo", "12000"],
      ["Solo Faja Dobles", "6000"],
      ["Cuello Redondo Doble", "4000"],
    ];
    for (let i = 0; i < products.length; i++) {
      const productOption = document.createElement("option");
      productOption.value = products[i][1];
      productOption.textContent = products[i][0];
      productoSelect.appendChild(productOption);
    }
  
    productoDiv.appendChild(productoSelect);
    newRow.appendChild(productoDiv);
  
    // Create the Precio/Unidad div and input
    const precioUnidadDiv = document.createElement("div");
    precioUnidadDiv.className = "col-3";
    const precioUnidadInput = document.createElement("input");
    precioUnidadInput.id = "Precio/Unidad";
    precioUnidadInput.name = "Precio/Unidad";
    precioUnidadInput.className = "form-control";
    precioUnidadInput.type = "number";
    precioUnidadInput.min = "0";
    precioUnidadInput.placeholder = "0";
    precioUnidadInput.value = productoSelect.value;
    precioUnidadDiv.appendChild(precioUnidadInput);
    newRow.appendChild(precioUnidadDiv);
  
    // Create the Precio/Total div and input
    const precioTotalDiv = document.createElement("div");
    precioTotalDiv.className = "col-3";
    const precioTotalInput = document.createElement("input");
    precioTotalInput.id = "Precio/Total";
    precioTotalInput.name = "Precio/Total";
    precioTotalInput.className = "form-control";
    precioTotalInput.type = "number";
    precioTotalInput.min = "0";
    precioTotalInput.placeholder = "0";
    precioTotalInput.value = productoSelect.value * cantidadInput.value;
    precioTotalDiv.appendChild(precioTotalInput);
    newRow.appendChild(precioTotalDiv);
  
    // Create a delete button and attach an event listener to it
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "col-1 btn btn-danger";
    deleteButton.addEventListener("click", () => {
      newRow.remove(); // remove the current row when the button is clicked
    });
    newRow.appendChild(deleteButton);
  
    // Get the ordenes div and add the new row
    const ordenesDiv = document.getElementById("ordenes");
    ordenesDiv.appendChild(newRow);
  
    // Event listeners to update the "Precio/Unidad" and "Precio/Total" input values
    productoSelect.addEventListener("change", () => {
      precioUnidadInput.value = productoSelect.value;
      precioTotalInput.value = productoSelect.value * cantidadInput.value;
    });
  
    cantidadInput.addEventListener("change", () => {
      precioTotalInput.value = productoSelect.value * cantidadInput.value;
    });
  }



// function calcularUnidadTotal(){
//     var precio_producto = document.getElementById('producto').value
//     var cantidad = document.getElementById('cantidad').value

//     document.getElementById('Precio/Unidad').value = precio_producto
//     document.getElementById('Precio/Total').value = precio_producto*cantidad
// }

// // function crearLinea(){
// //     var capa = document.getElementById("ordenes");
// //     var div = document.createElement("div");
// //     div.classList.add("row", "m-1")
// //     div.innerHTML = '<div class="col-2"><input class="form-control" id="cantidad" type="number" min="1" placeholder="0""></div><div class="col-4"><select name="producto" class="form-select texto-oscuro" id="producto"><option value=""></option></select></div><div class="col-3"><input class="form-control" id="Precio/Unidad" type="number" placeholder="0"></div><div class="col-3"><input class="form-control" id="Precio/Total" type="number" placeholder="0"></div>';
// //     // capa.appendChild(div);
// //     capa.insertBefore(div, ordenes.firstChild);
// // }


// function crearLinea() { // Función que crea un div con todos los formatos para registrar los tipos de habitaciones
//     var capa = document.getElementById("ordenes"); // Se obtiene el div donde van todos los divs las líneas
//     var div = document.createElement("div"); // Se crea un div para la nueva linea
//     div.classList.add("row", "m-1") // Añade la clase borrable al div creado
//     div.innerHTML = '<div class="col-2"><input class="form-control" id="cantidad" type="number" min="1" placeholder="0""></div><div class="col-4"><select name="producto" class="form-select texto-oscuro" id="producto"><option value=""></option></select></div><div class="col-3"><input class="form-control" id="Precio/Unidad" type="number" placeholder="0"></div><div class="col-3"><input class="form-control" id="Precio/Total" type="number" placeholder="0"></div>'; // Se rellena el div de la linea con el html que contiene los formatos
//     capa.appendChild(div); // Se ingresa el div de la linea actual al final del div que contiene todas las lineas

//     // Add event listener to the new select element
//     addEventListenerToSelect(div); // Se añade un listener al div creado
// }

// function addEventListenerToSelect(div) { // Función que recibe el div de una linea como argumento y añade un listener
//     const productos = div.querySelector("#producto"); // Obtiene todos selects con tipo_habitación
//     const acomodacionSelect = div.querySelector(".acomodación"); // Obtiene todos selects con acomodación

//     tipoHabitacionSelect.addEventListener("change", () => { // Listener que cambia los valores disponibles del select acomodación dependiendo del valor del select tipo_habitación
//         if (tipoHabitacionSelect.value === "Estándar") { // Sí el valor del select tipo_habitación es Estándar, las opciones disponibles son Sencilla, Doble.
//             acomodacionSelect.innerHTML = `
//         <option value="Sencilla">Sencilla</option>
//         <option value="Doble">Doble</option>
//         `;
//         } else if (tipoHabitacionSelect.value === "Junior") { // Sí el valor del select tipo_habitación es Estándar, las opciones disponibles son Triple, Cuádruple.
//             acomodacionSelect.innerHTML = `
//         <option value="Triple">Triple</option>
//         <option value="Cuádruple">Cuádruple</option>
//         `;
//         } else if (tipoHabitacionSelect.value === "Suite") { // Sí el valor del select tipo_habitación es Estándar, las opciones disponibles son Sencilla, Doble, Triple.
//             acomodacionSelect.innerHTML = `
//         <option value="Sencilla">Sencilla</option>
//         <option value="Doble">Doble</option>
//         <option value="Triple">Triple</option>
//         `;
//         } else { // Sí el valor del select tipo_habitación no es ninguno de los anteriores, las opciones disponibles son todas.
//             acomodacionSelect.innerHTML = `
//         <option value="Sencilla">Sencilla</option>
//         <option value="Doble">Doble</option>
//         <option value="Triple">Triple</option>
//         <option value="Cuádruple">Cuádruple</option>
//         `;
//         }
//     });
// }
// addEventListenerToSelect(document); // Agrega un listener de eventos al elemento select existente

// function checkHabitaciones() { // Revisa que la suma de todas las cantidades de habitaciones no sobrepase a la indicada como número de habitaciones del hotel
//     var cantidadElems = document.getElementsByClassName("cantidad_int"); // Obtiene todas las cantidades de habitaciones por linea
//     var totalCantidad = 0; // Variable para sumar la cantidad de habitaciones
//     for (var i = 0; i < cantidadElems.length; i++) { // Recorre la cantidad de inputs donde se indican la cantidad de habitaciones
//         totalCantidad += parseInt(cantidadElems[i].value); // Obtiene el valor de esos inputs y los suma a la variable para sumar la cantidad de habitaciones
//     }
//     var maxHabitaciones = parseInt(document.getElementById("max_habitaciones").value); // Define una variable que obtiene el máximo de habitaciones del hotel a traves del valor del input que lo muestra en pantala.
//     if (totalCantidad > maxHabitaciones) { // Sí el número es mayor a la cantidad máxima de habitaciones
//         alert("La cantidad de habitaciones indicadas supera la capacidad máxima."); // Muestra un alert

//         var container = document.getElementById("datos_habitaciones"); // Obtiene el div que contiene los divs de lineas 
//         let borrables = Array.prototype.slice.call(document.getElementsByClassName("borrable"), 0); // Obtiene todos los divs que tienen la clase borrable

//         for(element of borrables){ // Itera sobre todos los divs borrables
//             element.remove(); // Los borra
//         } 

//         for (var j = 0; j < cantidadElems.length; j++) { // Todos los inputs que indican la cantidad de habitaciones vuelven a ""
//             cantidadElems[j].value = ""; // Cambia el valor del elemento a ""
//         }
//     }
// }

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
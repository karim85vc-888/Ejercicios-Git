// JavaScript
// console.log(10 + "2");
// console.log("3" * 2);
// La función prompt() pide un valor y LO DEVUELVE COMO STRING
let edad_str = prompt("Por favor, introduce tu edad:"); // Retorna, por ejemplo, "33"

// Es necesario convertir la cadena a número para la suma
let resultado = 10 + Number(edad_str); 

console.log(resultado); // Si el usuario escribió 33, la salida es 43 (suma numérica)
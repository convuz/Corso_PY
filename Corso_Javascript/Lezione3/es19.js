// # Esercizio 19

// - Date le variabili `name` e  `surname`, crea un costrutto if else per stampare in console la variabile `fullname`, 
// che conterrà le due variabili precedenti.
// - La variabile `fullname` dovrà essere stampata solo se `name` e `surname` sono truthy, 
// in caso contrario stampa il messaggio `Fullname is invalid`

let name = "Mario";
let surname = "Rossi";
let fullname;

if (name && surname){
    fullname = name + " " + surname;
    console.log(fullname);
} else {
    console.log("Fullname is invalid");
}


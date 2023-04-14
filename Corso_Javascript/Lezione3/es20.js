// # Esercizio 20
 
// - Crea una variabile `primitive` e assegnale un valore che potrà essere di tipo numero, stringa o booleano.
// - Crea un controllo per verificare il tipo della variabile e stamparlo in console.

let primitive = "ciao";

if (typeof(primitive) == "boolean"){
    console.log("il tipo della variabile è booleano");
} else if (typeof(primitive) == "number"){
    console.log("il tipo della variabile è un numero");
} else if (typeof(primitive) == "string"){
    console.log("il tipo della variabile è una stringa");
} else {
    console.log("il tipo della variabile NON è nessuno dei precedenti");
}



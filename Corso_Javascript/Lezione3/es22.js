// # Esercizio 22

// - Modifica il costrutto if creato nell'esercizio 20, trasformandolo in un costrutto switch

let primitive = "ciao";

// if (typeof(primitive) == "boolean"){
//     console.log("il tipo della variabile è booleano");
// } else if (typeof(primitive) == "number"){
//     console.log("il tipo della variabile è un numero");
// } else if (typeof(primitive) == "string"){
//     console.log("il tipo della variabile è una stringa");
// } else {
//     console.log("il tipo della variabile NON è nessuno dei precedenti");
// }

switch (typeof(primitive)){
    case "boolean":
        console.log("il tipo della variabile è booleano");
        break;
    case "number":
        console.log("il tipo della variabile è booleano");
        break;
    case "string":
        console.log("il tipo della variabile è booleano");
        break;
    default: 
        console.log("il tipo della variabile NON è nessuno dei precedenti");
}
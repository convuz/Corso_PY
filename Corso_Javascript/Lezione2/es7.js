// # Esercizio 7

// - Esegui la conversione (casting) delle variabili al tipo di dato presente nei commmenti del file exercise.js e stampa il risultato dell'operazione.
// - Spiega il casting della variabile `hello`

let hello = 'Ciao';     // number
let age = 18;       // boolean
let isGraduated = false;     // string

console.log(Number(hello)); // esce NaN perché "Ciao" non è trasmutabile in un numero
console.log(Boolean(age));
console.log(String(isGraduated));

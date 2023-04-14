// # Esercizio 23

// - Crea, tramite costrutto switch, un controllo che stampi in console il prezzo di una camera d'albergo in base alle seguenti tariffe:

// Tariffa BB --> 50€
// Tariffa HB --> 80€
// Tariffa FB --> 100€

let costo = "BB";

switch (costo){
    case "BB":
        console.log("il prezzo è 50€");
        break;
    case "HB":
        console.log("il prezzo è 80€");
        break;
    case "FB":
        console.log("il prezzo è 100€");
        break;
    default:
        console.log("inserito una tariffa inesistente");
}
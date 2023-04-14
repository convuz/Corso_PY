// # Esercizio 42

// Scrivere un funzione di nome `Smartphone` che prenda come parametro i seguenti elementi: `brand`,`name`, `price`. 
// Questa funzione, ogni volta che viene chiamata con new, deve restituire un nuovo oggetto smartphone, 
// con le informazioni (parametri) che passiamo

// Indicazioni utili:

// - Ricordati che `brand` e `name` saranno stringhe e `price` sarà un numero
// - Crea almeno due 'Smartphone' con informazioni diverse

function Smartphone(brand, name, price) {
    this.brand = brand;
    this.name = name;
    this.price = price;
}

let tel1 = new Smartphone("Apple", "Iphone 13", 1000);
let tel2 = new Smartphone("Samsung", "S10", 600);
// # Esercizio 41

// Abbiamo l'oggetto `smartphone`, utilizzando uno specifico metodo degli oggetti, 
// possiamo rendere questo oggetto 'freezato', e quindi non modificare il prezzo così facilmente.
// Sapresti scrivere il metodo che ci serve?

// Indicazioni utili:

// - Abbiamo bisogno di un metodo che renda l'oggetto `smartphone` 'freezato'

const smartphone = {
    brand: "Apple",
    name: "Iphone 13",
    price: 1300,
};
  
Object.freeze(smartphone);
smartphone.price = 100;
  
console.log(smartphone);
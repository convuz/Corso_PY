// # Esercizio 49

// Abbiamo il nostro array di studenti, vogliamo rimuovere lo studente Giovanni ed aggiungere il seguente studente:
// { id: 3, name: "Francesco", surname: "Verdi", age: 41 }
// Sapresti fare questa operazione?

// Dopo ogni operazione inserire il console.log() del nostro array `students`

// Indicazioni utili:

// - Abbiamo già fatto qualcosa di simile, questa volta dovrai farlo lavorando con gli oggetti
// - Sei hai qualche dubbio, qui trovi tutti i metodi che abbiamo per lavorare con gli array: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

const students = [
    { id: 1, name: "Luca", surname: "Rossi", age: 20 },
    { id: 2, name: "Mario", surname: "Bianchi", age: 24 },
    { id: 3, name: "Giovanni", surname: "Brambilla", age: 30 },
];

students.pop();
console.log(students);
students.push({ id: 3, name: "Francesco", surname: "Verdi", age: 41 });
console.log(students);  
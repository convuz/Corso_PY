// # Esercizio 46

// Partendo dall'esercizio precedente, tramite un ciclo `for`, dobbiamo stampare tutti gli elementi contenuti nel nostro array

// Indicazioni utili:

// - In caso di difficoltà, riguarda la lezione
// - Abbiamo fatto qualcosa di simile anche con gli oggetti, iterando su di essi

const student = [
    {id: 1, name: "Mario", surname: "Rossi", age:16},
    {id: 2, name: "Paolo", surname: "Bianchi", age:12},
    {id: 3, name: "Simone", surname: "Carli", age:18}
];

for (let i = 0; i < student.length; i++){
    console.log(student[i]);
}

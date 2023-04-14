// # Esercizio 43

// Il nostro oggetto `student` è incompleto. Abbiamo bisogno di aggiungere a questo oggetto, 
// un ulteriore oggetto al suo interno di nome `personalData`. L'oggetto nested `personalData` deve contenere le seguenti proprietà: 
// `name`, `surname`, `age`.
// Sapresti inserirlo?

// Indicazioni utili:

// - Stampare sul terminale l'oggetto nested `personalData` che dovrà trovarsi dentro `student`

const student = {
    id: 1,
    school: "Liceo",
    year: 3,
    personalData : {
        name: "Riccardo",
        surname: "Convertino",
        age: 21
    }
};

console.log(student.personalData);
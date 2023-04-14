// # Esercizio 39

// Nel nostro file di partenza, troviamo un oggetto `user` che presenta le proprietà `name` e `age`.
// Adesso, se vogliamo creare un nuovo utente partendo da `user`, e dopo proviamo a modificarne il nome,
// come vedrete dai console.log(), andremo a modificare anche l'oggetto di partenza.
// Sapresti modificare il `name` di `newUser`, senza cambiare quello di `user`?

// Indicazioni utili:

// - Potresti utilizzare in ciclo `for in` come abbiamo visto nei video
// - Ti servirà una nuova copia dell'oggetto `user`
// - Potresti trovare delle info utili qui: https://javascript.info/object-copy

let user = {
    name: "Cosimo",
    age: 30,
};

let newUser = {};

for (const pasta in user) {
    newUser[pasta] = user[pasta];
    //console.log(user[pasta]);
}

newUser.name = "Paolo";

console.log(newUser);
console.log(user);
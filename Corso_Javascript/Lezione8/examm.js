function positiveMinimum(numbersArray) {
    let minNumber = numbersArray[0];
    for (let i = 0; i < numbersArray.length; i++){
        if(numbersArray[i] <= minNumber){
           minNumber = numbersArray[i];
       }
    }
//Ho inserito il primo valore dell'array a mano, cosi facendo non ho problemi nel for a far entrare il primo valore.
    if (minNumber < 0 || minNumber == "undefined"){
        minNumber = 0;
    }//in questo controllo dovrei riuscire anche a verificare se ho un valore undefined che mi uscirebbe se inserisco un array vuoto
    return minNumber;
}

let arr1 = [9,6,3,13,1,2,3,4,5,22];
console.log(positiveMinimum(arr1));
let arr2 = [1,1,0,0,1,1,0,0,1,1];
console.log(positiveMinimum(arr2));
let arr3 = [-1,52,-2,2,-3,3,4,76,80,-67];
console.log(positiveMinimum(arr3));

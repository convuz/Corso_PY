#to convert a number to string we can use str() function this is called casting
# - cast num1 to string and assign to num1_str
# - check the length of the string
# - get the third element of string (the one in the 3rd order)
# - get the 3-5 elements of string (both inclusive) by string slicing
# - check if num2 in string (cast if necessary)
# - check if num3 in string (cast if necessary)
# - concatenate 0 to the string from left and assign to string_with_0
# - get the characters of string_with_0 from start to position 4 (end point exclusive)
# - get the characters of string_with_0 from position 5 until the end
# - use negative indexing to reach the "567" string_with_0



num1 = 1122334455666
num1_str = str(num1)
print(len(num1_str))
print(num1_str[2])
print(num1_str[2:5])
#manca il controllo se num2 è una stringa, ma non esiste una variabile num2 perciò per non crearla dal nulla l'ho saltato
#manca il controllo se num3 è una stringa, ma non esiste una variabile num3 perciò per non crearla dal nulla l'ho saltato
string_with_0 = '0' + num1_str
#print(string_with_0)
print(string_with_0[0:4])
print(string_with_0[4:])
#Per non andare a contare la lunghezza della stringa uso l'index -1 per indicare l'ultimo valore della stringa.
print(string_with_0[5:8])
print(string_with_0[-9:-6])
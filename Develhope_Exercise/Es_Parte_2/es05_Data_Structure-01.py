# Remember list,set,dictionary are mutable and tuple is immutable list,tuple elements can be reached by index
# for dictionary it is not an option to reach by index the element key has to be known to reach
# and for set the items cannot be reached directly but it is possible to iterate.

# 1)print the lengths of list1,tuple1,set1,dict1
# 2)print the first element of list1 and tuple1
# 3)print the value of lion key of dict1
# 4)change the 2nd position element of list1 to "rabbit"
# 5)try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
# 6)add "monkey" to list1
# 7)remove "rabbit" from list1
# 8)in dict1 the number of feet is written as value to each animal the fish has wrong value just fix it.

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

print("1)")
print("Lunghezza di list1:",len(list1))
print("Lunghezza di tuple1:",len(tuple1))
print("Lunghezza di set1:",len(set1))
print("Lunghezza di dict1:",len(dict1))

print("\n2)")
print("primo elemento di list1: " + list1[0] + " e di tuple1: " + tuple1[0])

print("\n3)")
print("valore della chiave lion di dict1:", dict1["lion"])

print("\n4)")
print(list1)
list1[1] = "rabbit"
print(list1)

#print("\n5)")
#tuple1[1] = "rabbit"
#Il tipo di oggetto tuple non supporta l'assegnazione di valori 


print("\n6)")
print(list1)
list1.append("monkey")
print(list1)

print("\n7)")
print(list1)
list1.remove("rabbit")
print(list1)

print("\n8)")
print(dict1)
dict1["fish"] = 0
print(dict1)
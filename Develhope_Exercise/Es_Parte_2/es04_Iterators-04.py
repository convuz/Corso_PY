# Iterate each elements of list1,tuple1,set1 and print them out
# For the dict1 iterate all elements but only print the ones who are living on land in the form of x lives in y

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

print("Print di list1:")
for i in list1:
    print(f"{i} ", end=" ")

print("\n\nPrint di tuple1:")
for i in tuple1:
    print(f"{i} ", end=" ")

print("\n\nPrint di set1:")
for i in set1:
    print(f"{i} ", end=" ")

print("\n\nPrint di dict1:")
for i in dict1:
    if dict1[i] == "land":
        print(f"{i} lives in {dict1[i]}")


#Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

string = "Python"

for i in string:
    if i != "o":
        print(i)
    else:
        continue


print("")
for i in string:
    if i == "o":
        continue
    print(i)
print("")
i=0
while i<len(string):
    if string[i] == "o":
        i+=1
        continue
    print(string[i])
    i+=1
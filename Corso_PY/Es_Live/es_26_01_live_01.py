#crea una funzione che si chiama my_sum che prenda come input un qualsiasi numero di elementi e le sommi tra di loro
#The result should be a new, longer sequence of the type provided by the parameters.
#Thus, the result of mysum('abc', 'def') will be the string abcdef, and the result of
#mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6]. Of course, it
#should also still return the integer 6 if we invoke mysum(1,2,3)

def my_sum(*items):
    a = ()
    if items == ():
        #a = "Input vuoto"
        return ""
    else:
        a = items[0]
        for i in items[1:]:
            a+=i
        return a

print(my_sum('abc', 'def'))
print(my_sum([1,2,3], [4,5,6]))
print(my_sum(1,2,3))
print(my_sum())
# Check if it is time for coffee break if it is just break
# To do that lets iterate through given list don't change the COFFEE BREAK statement.
# just find another way to do it

todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break
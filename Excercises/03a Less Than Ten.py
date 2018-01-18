b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
targetnumber = int(input("Please enter a number: \n"))
for element in a:
    if element < targetnumber:
        b.append(element)
print(b)        
        

while True:
    usernumber = int(input("Please enter a number: \n"))
    x = range(1, usernumber + 1)
    for element in x:
        if usernumber % element == 0:
            print(element)
        

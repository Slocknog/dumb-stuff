import time
while True:
    numbera=int(input("Please enter a number:"))
    numberb=int(input("Please enter a number to divide by:"))
    decider=numbera % numberb
    if decider == 0:
        print ("Divides evenly!")
    else:
        print ("Divides unevenly.")

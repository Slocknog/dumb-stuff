import time
while True:
    numbera=int(input("Please enter a number:"))
    decider=numbera % 4
    if decider == 0:
        print ("Multiple of 4!")
        time.sleep(1)        
    elif decider == 1:
        print ("Odd number!")
        time.sleep(1)
    elif decider == 3:
        print ("Odd number!")
        time.sleep(1)        
    elif decider == 2:
        print ("Even number!")
        time.sleep(1)        
            
              

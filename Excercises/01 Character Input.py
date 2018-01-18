import time
name = str( input ("Enter your name:"))
age = int( input("Enter your age in years:"))
year = int( input("Enter the current year:"))

copies = int( input("Enter the amount of copies:"))
              
yeartime =(100 - age) + year

print (("Dear " + name + ", you will be 100 years old on the year " + str(yeartime) + ". \n") * copies)
time.sleep(5)            

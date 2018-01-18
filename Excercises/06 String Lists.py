while True:
    list = str(input("Enter a word to check as a palindrome."))
    #removes spaces
    list = list.replace(" ","")

    list_backward = str(list[::-1])#[::-1] is used to reverse a list

    list_forward = str(list)

    if (list_forward == list_backward):
        print("This is a palindrome. It reads {0} from the front and {1} from the back.".format(list_forward,list_backward))
    else: # this whole {0},{1},etc thing alongside with .format() at the end allows me to add shit to the text from the back or smth
        print("This is not a palindrome. It reads {0} from the front and {1} from the back.".format(list_forward,list_backward))

           

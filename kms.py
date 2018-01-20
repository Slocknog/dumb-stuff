import time
finds = ["chair","rope"]
items = []
while True:
    x = input("You possess: {0} \nYou see: {1} \nType 'suicide' to attempt suicide. \n".format(items,finds))
    if x == "chair":
        for rope in finds:
            print("You took the chair.")
            finds.remove("chair")
            items.append("chair")
    elif x == "rope":
        for rope in finds:
            print("You took the rope.")
            finds.remove("rope")
            items.append("rope")
    elif x == "suicide":
        if len(items) == 2:
            print("You step over the chair.")
            time.sleep(1)
            print("You bring the rope around your neck and tie it to the ceiling.")
            time.sleep(1)
            print("You kick the chair off.")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Congratulations! You have killed yourself!")
            break
        else:
            print("You do not have the required items.")

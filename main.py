from shopping import itemRAT


def makelistRAT(): #makes list
    shoppinglist = []

    while True: #input loop
        numofitems = eval(input("How many items are you going to buy? "))
        if numofitems < 1:
            print("Minimum purchase is 1 item")
        else:
            break

    for i in range(numofitems):
        while True: #input loop
            itemname = input("Enter item name: ")
            amount = eval(input("Enter how many pounds: "))
            item = itemRAT(item_name, amount)
            if itemname == "" or item.getpriceRAT() == 0:
                print("Item name invalid")
            elif amount < 1:
                print("Amount has to be more than 0")
            else:
                break
        shoppinglist.append(item) #appends "item" to list

    return shoppinglist


def displayRAT(listofitems):
    print("-" * 28)
    print("Here's a summary of the items purchased: ")
    for i in range(len(listofitems)):
        print(f"Item {i + 1}")
        print(listofitems[i].__str__() + "\n") #print all in list


def calculatetotalRAT(listofitems):
    total = 0
    for i in range(len(listofitems)):
        total += listofitems[i].totalpriceRAT()
    return total


shoppinglist = makelistRAT()
displayRAT(shoppinglist)
print(f"Total amount: ${calculatetotalRAT(shoppinglist)}")
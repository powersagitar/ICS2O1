##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

# menu, tag, price, cart stack declaration (demo)
menu = ["beefBurger", "cheeseBurger", "doubleBurger", "chickenBurger", "sausageBurger", "fruitopiaStrawberry", "fruitopiaOrange", "coke" "dietCoke", "fries", "iceCream"];
tag = ["meat-burger", "burger", "meat-burger", "meat-burger", "meat-burger", "beverage", "beverage", "beverage", "beverage", "others", "others"];
price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10];
cart = [];

# check special offer validation
if (dateM == dateD):
    # apply special offer
    for i in len(price):
        price[i] = price[i] * 0.8;
    discount = True;

# fetch user input
while (True):
    name = input("Enter your full name: ");
    specificationStore = [];
    # fetch specifications
    while (True):
        userInput = input("Enter your specifications, if none, enter *void*: ");
        specificationStore.append(userInput);
        if ("void" in specificationStore):
            specificationStore = "None";
            break;
        # new specification check
        conditionInnerWhile = input("Continue? Enter True or False: ");
        if (conditionInnerWhile == "False"):
            break;
    
    # avoiding specifications
    if ("vegie" in specificationStore):
        for i in len(tag):
            if (meat in tag[i]):
                price[i] = "unavailable";
    
    #order
    print("Burgers:\n");
    for i in len(tag):
        if ("burger" in tag[i]):
            print("Code:", i, menu[i], "Price: $" + str(price));
    while (True):
        userInput = int(input("Please enter the code of your preferred food: "));
        cart.append(userInput);

    # printing receipt
    print("\nReceipt");
    print("Name:", name);
    print("Specifications:", specificationStore);
    if (DISCOUNT == True):
        print("Special-day discount applied: 20% off"); # ? not sure if it's working, tests needed
    else:
        print("No special-day discount applied");
    
    # new customer check
    conditionOuterWhile = input("Is there any more customers? Enter True or False: ")
    if (conditionOuterWhile == "False"):
        break;

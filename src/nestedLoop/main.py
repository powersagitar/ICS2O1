##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

# menu stack and price stack declaration (demo)
menu = ["salad", "fries", "beefBurger", "beefHotDog"];
price = [10, 10, 10, 10];
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
        specificationInput = input("Enter your specifications, if none, enter *void*: ");
        specificationStore.append(specificationInput);
        if ("void" in specificationStore):
            specificationStore = "None";
            break;
        # new specification check
        conditionInnerWhile1 = input("Continue? Enter True or False: ");
        if (conditionInnerWhile1 == "False"):
            break;
    
    

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

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
menu = ["beefBurger", "cheeseBurger", "doubleBurger", "chickenBurger", "sausageBurger", "fruitopiaStrawberry", "fruitopiaOrange", "coke", "dietCoke", "fries", "iceCream"];
tag = ["meat-burger", "burger", "meat-burger", "meat-burger", "meat-burger", "beverage", "beverage", "beverage", "beverage", "others", "others"];
PRICE = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10];
cart = [];
argu = [];

# fetch user input
while (True):
    # variable initialization
    actualPrice = PRICE.copy();
    argu.clear();
    cart.clear();
    subtotal = 0;
    tax = 0;

    # check special offer validation
    if (dateM == dateD):
        # apply special offer
        for i in range(len(actualPrice)):
            actualPrice[i] = actualPrice[i] * 0.8;
        discount = True;
    else:
        discount = False;

    name = input("Enter your full name: ");
    specification = [];
    # fetch specifications
    while (True):
        userInput = input("Enter your specifications, if none, enter *void*: ");
        specification.append(userInput);
        if ("void" in specification):
            specification = "None";
            break;
        # new specification check
        userInput = input("Any other specifications? Enter True or False: ");
        if (userInput == "False"):
            break;
    
    # avoiding specifications
    if ("vegie" in specification):
        for i in range(len(tag)):
            if ("meat" in tag[i]):
                actualPrice[i] = "N/A";
    
    # ordering
    while (True):
        # burgers
        print("\nBurgers:");
        for i in range(len(tag)):
            if ("burger" in tag[i]):
                print("Code:" + str(i), menu[i], "Price: $" + str(actualPrice[i]));
        while (True):
            userInput = int(input("Please enter the code of your preferred food: "));
            cart.append(userInput);
            userInput = input("Anything else to order? Enter True or False: ");
            if (userInput == "False"):
                break;
        
        # beverages
        print("\nBeverages:");
        for i in range(len(tag)):
            if ("beverage" in tag[i]):
                print("Code:" + str(i), menu[i], "Price: $" + str(actualPrice[i]));
        while (True):
            userInput = int(input("Please enter the code for your preferred food: "));
            cart.append(userInput);
            userInput = input("Anything else to order? Enter True of False: ");
            if (userInput == "False"):
                break;

        # others
        print("\nOthers:");
        for i in range(len(tag)):
            if ("others" in tag[i]):
                print("Code:" + str(i), menu[i], "Price: $" + str(actualPrice[i]));
        while (True):
            userInput = int(input("Please enter the code for your preferred food: "));
            cart.append(userInput);
            userInput = input("Anything else to order? Enter True or False: ");
            if (userInput == "False"):
                break;
        
        # order confirmation
        print();
        for i in range(len(cart)):
                print(str(i + 1) + ".", menu[cart[i]], "Price: $" + str(actualPrice[cart[i]]));
                subtotal += actualPrice[cart[i]];
        userInput = input("Are those all the stuff you want? Enter True or False: ");
        if (userInput == "True"):
            break;
        else:
            cart.clear();
            print("Please choose what you want again.");

    # price calculation
    tax = round((subtotal * 0.13), 2);

    # printing receipt
    print("\nReceipt");
    print("Name:", name);
    print("Specifications:", specification);
    print("Food you ordered:");
    for i in range(len(cart)):
        print(str(i + 1) + ".", menu[cart[i]], "Price: $" + str(actualPrice[cart[i]]));
    
    if (discount == True):
        print("Special-day discount applied: 20% off");
    else: # discount == False
        print("No special-day discount applied");
    
    print("Subtotal: $" + str(subtotal));
    print("HST: $" + str(tax));
    print("Total: $" + str(subtotal + tax))
    
    # new customer check
    userInput = input("Is there any more customers? Enter True or False: ")
    if (userInput == "False"):
        break;
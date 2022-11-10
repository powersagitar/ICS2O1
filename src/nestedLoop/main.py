##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

# printing menu

# fetch user input
while (True):
    # variable initialization
    subtotal = 0;
    tax = 0;
    order = "";

    # check special offer validation
    if (dateM == dateD):
        discount = True;
    else:
        discount = False;

    name = input("Enter your full name: ");
    specifications = input("Enter your specifications, use space to separate each item, and use \"void\" for none: ")

    # printing menu
    print("\nEnter your order, insert dot (.) after each item (including the last one). If you don't want to order any items, enter \"void\". NOTE: This input is space sensitive.\n");
    print("MENU (Standard Price)");

    # ordering
    # vegeterian
    if "vegie" in specifications:
        print("Burgers:");
        print("1. cheese burger: $10");
        order = order + input();

        print("\nBeverages:");
        print("6. fruitopia strawberry: $10\n7. fruitopia orange: $10\n8. diet coke: $10\n9. coke: $10");
        order = order + input();

        print("\nOthers:");
        print("10. fries: $10\n11. ice cream: $10");
        order = order + input();
    # regular
    else:
        print("Burgers:");
        print("1. beef burger: $10\n2. cheese burger: $10\n3. double burger: $15\n4. chicken burger: $10\n5. sausage burger: $10");
        order = order + input();

        print("\nBeverages:");
        print("6. fruitopia strawberry: $10\n7. fruitopia orange: $10\n8. coke: $10\n9. diet coke: $10");
        order = order + input();

        print("\nOthers:");
        print("10. fries: $10\n11. ice cream: $10");
        order = order + input();
    
    # pricing
    # subtotal
    print("For each item, large size will charge $2 more, small size will charge $2 less, medium size will remain the standard price.");
    for i in range(order.count('.')):
        if ("beef burger." in order):
            order = order.replace("beef burger", "", 1);
            subtotal += 10;
            print("beef burger", end = "");
        elif ("cheese burger." in order):
            order = order.replace("cheese burger", "", 1);
            subtotal += 10;
            print("cheese burger", end = "");
        elif ("double burger." in order):
            order = order.replace("double burger", "", 1);
            subtotal += 15;
            print("double burger", end = "");
        elif ("chicken burger." in order):
            order = order.replace("chicken burger", "", 1);
            subtotal += 10;
            print("chicken burger", end = "");
        elif ("sausage burger." in order):
            order = order.replace("sausage burger", "", 1);
            subtotal += 10;
            print("sausage burger", end = "");
        elif ("fruitopia strawberry." in order):
            order = order.replace("fruitopia strawberry", "", 1);
            subtotal += 10;
            print("fruitopia strawberry", end = "");
        elif ("fruitopia orange." in order):
            order = order.replace("fruitopia orange", "", 1);
            subtotal += 10;
            print("fruitopia orange", end = "");
        # ! changed order, not sure if will work. experiment needed
        elif ("diet coke." in order):
            order = order.replace("diet coke", "", 1);
            subtotal += 10;
            print("diet coke", end = "");
        elif ("coke." in order):
            order = order.replace("coke", "", 1);
            subtotal += 10;
            print("coke", end = "");
        elif ("fries." in order):
            order = order.replace("fries", "", 1);
            subtotal += 10;
            print("fries", end = "");
        elif ("ice cream." in order):
            order = order.replace("ice cream", "", 1);
            subtotal += 10;
            print("ice cream", end = "");
        elif ("void" in order):
            subtotal = 0;
            break;
        
        argu = input(" size: \"large\" for large, \"medium\" for medium, \"small\" for small\n");
        if (argu == "large"):
            subtotal += 2;
        elif (argu == "small"):
            subtotal -= 2;
        
    # tax and total
    # special deal
    if (dateM == dateD):
        discount = True;
        subtotal = round(subtotal * 0.8, 2);
    else:
        discount = False;
    tax = round((subtotal * 0.13), 2);
    total = subtotal + tax;

    # printing receipt
    print("\nRECEIPT");
    if (discount == True):
        print("Special deal applied. You got 20% off for subtotal.")
    print("Subtotal:", subtotal, "\nHST:", tax, "\nTotal:", total);
    
    # new customer check
    userInput = input("Is there any more customers? Enter \"true\" or \"false\": ")
    if (userInput == "false"):
        break;
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

    # check special offer validation
    if (dateM == dateD):
        discount = True;
    else:
        discount = False;

    name = input("Enter your full name: ");

    # printing menu
    print("MENU");
    
    
    # ordering
    while (True):
        break;
        
    # price calculation
    tax = round((subtotal * 0.13), 2);

    # printing receipt
    print("\nReceipt");
    
    # new customer check
    userInput = input("Is there any more customers? Enter True or False: ")
    if (userInput == "False"):
        break;
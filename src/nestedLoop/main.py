##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# discount declaration
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));
if (dateM == dateD):
    DISCOUNT = 0.9

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
    if (DISCOUNT is not None):
        print("Special-day discount applied:", DISCOUNT);
    else:
        print("No special-day discount applied");
    
    # new customer check
    conditionOuterWhile = input("Is there any more customers? Enter True or False: ")
    if (conditionOuterWhile == "False"):
        break;

##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

index = 0;
menu = ".beef burger.cheese burger.double burger.chicken burger.sausage burger.fruitopia strawberry.fruitopia orange.coke.diet coke.fries.ice cream.";
tag = ".meat-burger.burger.meat-burger.meat-burger.meat-burger.beverage.beverage.beverage.beverage.others.others.";
PRICE = ".10.10.10.10.10.10.10.10.10.10.10."
cart = "";

# fetch user input
while (True):
    # variable initialization
    actualPrice = PRICE;
    cart = "";
    subtotal = 0;
    tax = 0;

    # check special offer validation
    if (dateM == dateD):
        # apply special offer
        divider = actualPrice.index('.');
        for i in range(actualPrice.count('.') - 1):
            secondDivider = actualPrice.index('.', divider + 1);

            actualPrice[divider + 1:secondDivider] = float(PRICE[divider + 1:secondDivider]) * 0.8;

            divider = secondDivider;
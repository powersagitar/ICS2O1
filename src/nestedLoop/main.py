##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

#index = 0;
menu = "|beef burger|cheese burger|double burger|chicken burger|sausage burger|fruitopia strawberry|fruitopia orange|coke|diet coke|fries|ice cream|";
tag = "|meat-burger|burger|meat-burger|meat-burger|meat-burger|beverage|beverage|beverage|beverage|others|others|";
PRICE = "|10|10|10|10|10|10|10|10|10|10|10|"
cart = "";

# fetch user input
while (True):
    # variable initialization
    cart = "";
    subtotal = 0;
    tax = 0;

    # check special offer validation
    if (dateM == dateD):
        # apply special offer
        actualPrice = '|';
        start = PRICE.index('|');
        for i in range(PRICE.count('|') - 1):
            end = PRICE.index('|', start + 1);
            actualPrice += str(round((float(PRICE[start + 1:end]) * 0.8), 2)) + '|';
            start = end;
        DISCOUNT = True;
    else:
        actualPrice = PRICE;
        DISCOUNT = False;

    # fetch customer info
    name = input("Enter your name: ");
    # specification check
    userInput = input("Enter your specifications, put '|' after each specification (including last one). If none, enter 'void': ");
    if (userInput != "void"):
        specification = '|' + userInput;
    else:
        specification = "void";

    # printing menu
    # burgers
    print("\nBurgers");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("burger" in tag[start + 1:end]):

            # find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');

            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)]);
        start = end;

    # beverages
    print("\nBeverages");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("beverage" in tag[start + 1:end]):

            # find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');

            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)]);
        start = end;
    
    # others
    print("\nOthers");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("others" in tag[start + 1:end]):

            # find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');

            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)]);
        start = end;


    # new customer check
    userInput = input("Is there any new customers? Enter 'true' or 'false': ");
    if (userInput == "false"):
        break;
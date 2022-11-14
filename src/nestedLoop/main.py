##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));

# variable initialization
menu = "|beef burger|cheese burger|double burger|chicken burger|sausage burger|fruitopia strawberry|fruitopia orange|coke|diet coke|fries|ice cream|";
tag = "|meat-burger|burger|meat-burger|meat-burger|meat-burger|beverage|beverage|beverage|beverage|others|others|";
PRICE = "|10|10|10|10|10|10|10|10|10|10|10|"

# fetch user input
while (True):
    # variable initialization
    cart = '|';
    actualPrice = '|';
    subtotal = 0;
    tax = 0;

    # check special offer validation
    if (dateM == dateD):
        # apply special offer
        DISCOUNT = True;
    else:
        DISCOUNT = False;

    # fetch customer info
    name = input("Enter your name: ");
    # specifications check
    specifications = input("Enter your specifications, put '|' after each. If none, enter 'void': ");
    
    # updating actual price
    if "vegie" in specifications:
        start = tag.index('|');
        for i in range(tag.count('|') - 1):
            end = tag.index('|', start + 1);
            if ("meat" in tag[start + 1:end]):
                actualPrice += "N/A|";
            else:
                # find the nth occurrence of the divider
                occurrence = tag.count('|', 0, end) - 1;
                parts = PRICE.split('|', occurrence + 1);
                index = len(PRICE) - len(parts[-1]) - len('|');
                if DISCOUNT:
                    actualPrice += str(round((float(PRICE[index + 1:PRICE.index('|', index + 1)]) * 0.8), 2)) + '|';
                else:
                    actualPrice += str(float(PRICE[index + 1:PRICE.index('|', index + 1)])) + '|';
            start = end;
    else:
        start = tag.index('|');
        for i in range(tag.count('|') - 1):
            end = tag.index('|', start + 1);
            # find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = PRICE.split('|', occurrence + 1);
            index = len(PRICE) - len(parts[-1]) - len('|');
            if DISCOUNT:
                actualPrice += str(round((float(PRICE[index + 1:PRICE.index('|', index + 1)]) * 0.8), 2)) + '|';
            else:
                actualPrice += str(float(PRICE[index + 1:PRICE.index('|', index + 1)])) + '|';
            start = end;


    # printing menu
    # burgers
    print("\nBurgers");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("burger" in tag[start + 1:end]):
            # menu - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');
            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

            # actual price - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = actualPrice.split('|', occurrence + 1);
            index = len(actualPrice) - len(parts[-1]) - len('|');
            print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
        start = end;
    cart += input("Enter the code of your preferred items, put '|' after each (including last one): ");

    # beverages
    print("\nBeverages");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("beverage" in tag[start + 1:end]):
            # menu - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');
            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

            # actual price - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = actualPrice.split('|', occurrence + 1);
            index = len(actualPrice) - len(parts[-1]) - len('|');
            print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
        start = end;
    cart += input("Enter the code of your preferred items, put '|' after each (including last one): ");

    # others
    print("\nOthers");
    start = tag.index('|');
    for i in range(tag.count('|') - 1):
        end = tag.index('|', start + 1);
        if ("others" in tag[start + 1:end]):
            # menu - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = menu.split('|', occurrence + 1);
            index = len(menu) - len(parts[-1]) - len('|');
            print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

            # actual price - find the nth occurrence of the divider
            occurrence = tag.count('|', 0, end) - 1;
            parts = actualPrice.split('|', occurrence + 1);
            index = len(actualPrice) - len(parts[-1]) - len('|');
            print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
        start = end;
    cart += input("Enter the code of your preferred items, put '|' after each (including last one): ");

    # order confirmation
    print("\n", cart);
    userInput = input("Are those all the stuff you want to buy? Enter 'true' or 'false': ");
    if (userInput == "false"):
        continue;

    # subtotal calculation
    start = cart.index('|');
    for i in range(cart.count('|') - 1):
        end = cart.index('|', start + 1);
        # find the nth occurrence of the divider
        parts = actualPrice.split('|', int(cart[start + 1:cart.index('|', start + 1)]));
        index = len(actualPrice) - len(parts[-1]) - len('|');

        subtotal += float(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
        start = end;
    
    # printing receipt
    print("Subtotal:", subtotal);

    # new customer check
    userInput = input("Is there any new customers? Enter 'true' or 'false': ");
    if (userInput == "false"):
        break;
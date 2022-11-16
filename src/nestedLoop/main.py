##############################################################
# Program: Menu - Nested Loop
# Date: 11/01/2022
# Author: Mohan D.
# Description: An assignment about menus.
##############################################################

# date check
dateM = int(input("Enter today's date (MM): "));
dateD = int(input("Enter today's date (DD): "));
if (dateM == (1 or 3 or 5 or 7 or 8 or 10 or 12)):
    if (dateD > 31 or dateD <= 0):
        print("The entered date is invalid.");
        exit(-1);
elif (dateM == 2):
    if (dateD > 29 or dateD <= 0):
        print("The entered date is invalid.");
        exit(-1);
else: # (dateM == (4 or 6 or 9 or 11)) or (dateM <= 0 or dateM > 12)
    if (dateD > 30 or dateD <= 0 or dateM <= 0 or dateM > 12):
        print("The entered date is invalid.");
        exit(-1);

# variable initialization
menu = "|beef burger|cheese burger|double burger|chicken burger|sausage burger|fruitopia strawberry|fruitopia orange|coke|diet coke|fries|ice cream|";
tag = "|meat-burger|burger|meat-burger|meat-burger|meat-burger|beverage|beverage|beverage|beverage|others|others|";
PRICE = "|10|11|12|13|14|15|16|17|18|19|20|"
customerCount = 0;
revenue = 0;
donationReceived = 0;

# fetch user input
while (True):
    # check special offer validation
    if (dateM == dateD):
        # apply special offer
        DISCOUNT = True;
    else:
        DISCOUNT = False;

    # mode selection
    print("\nMain\n0. Exit\n1. Purchase mode (Will lose all the ordered items after re-entry)\n2. Refund mode\n3. Check out\n4. Show data analysis");
    userInput = int(input("Enter the sub menu (code) you want to enter: "));
    print(); # changing line (beautifing)

    if (userInput == 0): # exit
        break;

    elif (userInput == 1): # mode purchase
        # initialize and reset variables
        cart = '|';
        actualPrice = '|';
        subtotal = 0;
        tax = 0;
        originalSubtotal = 0;

        # fetch customer info
        name = input("Enter your name: ");
        # specifications check
        print("Enter your specifications, put '|' after each. If none, enter 'void'.");
        print("Currently available specifications:\n'veggie'");
        specifications = input("Specifications: ");
        
        # updating actual price
        if "veggie" in specifications:
            start = tag.index('|');
            for i in range(tag.count('|') - 1):
                end = tag.index('|', start + 1);
                if ("meat" in tag[start + 1:end]):
                    actualPrice += "N/A|";
                else:
                    # find the nth occurrence of the divider
                    parts = PRICE.split('|', tag.count('|', 0, end));
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
                parts = PRICE.split('|', tag.count('|', 0, end));
                index = len(PRICE) - len(parts[-1]) - len('|');
                if DISCOUNT:
                    actualPrice += str(round((float(PRICE[index + 1:PRICE.index('|', index + 1)]) * 0.8), 2)) + '|';
                else:
                    actualPrice += str(float(PRICE[index + 1:PRICE.index('|', index + 1)])) + '|';
                start = end;


        # printing menu
        print("\nMENU (Standard Price)")
        # burgers
        print("Burgers");
        start = tag.index('|');
        for i in range(tag.count('|') - 1):
            end = tag.index('|', start + 1);
            if ("burger" in tag[start + 1:end]):
                # menu - find the nth occurrence of the divider
                parts = menu.split('|', tag.count('|', 0, end));
                index = len(menu) - len(parts[-1]) - len('|');
                print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

                # actual price - find the nth occurrence of the divider
                parts = actualPrice.split('|', tag.count('|', 0, end));
                index = len(actualPrice) - len(parts[-1]) - len('|');
                print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
            start = end;
        userInput = input("Enter the code of your preferred items, put '|' after each (including last one). If you dont want to order anything, enter 'void': ");
        if (userInput != "void"):
            cart += userInput;

        # beverages
        print("\nBeverages");
        start = tag.index('|');
        for i in range(tag.count('|') - 1):
            end = tag.index('|', start + 1);
            if ("beverage" in tag[start + 1:end]):
                # menu - find the nth occurrence of the divider
                parts = menu.split('|', tag.count('|', 0, end));
                index = len(menu) - len(parts[-1]) - len('|');
                print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

                # actual price - find the nth occurrence of the divider
                parts = actualPrice.split('|', tag.count('|', 0, end));
                index = len(actualPrice) - len(parts[-1]) - len('|');
                print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
            start = end;
        userInput = input("Enter the code of your preferred items, put '|' after each (including last one). If you dont want to order anything, enter 'void': ");
        if (userInput != "void"):
            cart += userInput;

        # others
        print("\nOthers");
        start = tag.index('|');
        for i in range(tag.count('|') - 1):
            end = tag.index('|', start + 1);
            if ("others" in tag[start + 1:end]):
                # menu - find the nth occurrence of the divider
                parts = menu.split('|', tag.count('|', 0, end));
                index = len(menu) - len(parts[-1]) - len('|');
                print(str(i + 1) + '.', menu[index + 1:menu.index('|', index + 1)], end = " Price: $");

                # actual price - find the nth occurrence of the divider
                parts = actualPrice.split('|', tag.count('|', 0, end));
                index = len(actualPrice) - len(parts[-1]) - len('|');
                print(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
            start = end;
            
        # order confirmation
        while (True):
            userInput = input("Enter the code of your preferred items, put '|' after each (including last one). If you dont want to order anything, enter 'void': ");
            if (userInput != "void"):
                cart += userInput;
            print("\n", cart);
            userInput = input("Are those all the stuff you want to buy? Enter 'true' or 'false': ");
            if (userInput == "false"):
                continue;
            else:
                break;
        
        # size choosing
        print("\nFor each item, large size will charge $2 more, small size will charge $2 less, medium size will remain the standard price. No special deal will apply for this price change.");
        start = cart.index('|');
        for i in range(cart.count('|') - 1):
            end = cart.index('|', start + 1);

            # find the nth occurrence of the divider
            parts = menu.split('|', int(cart[start + 1:cart.index('|', start + 1)]));
            index = len(menu) - len(parts[-1]) - len('|');

            print(menu[index + 1:menu.index('|', index + 1)], end = "");
            argu = input(" size: \"large\" for large, \"medium\" for medium, \"small\" for small\n");
            if (argu == "large"):
                subtotal += 2;
                originalSubtotal += 2;
            elif (argu == "small"):
                subtotal -= 2;
                originalSubtotal -= 2;

            start = end;
    
    elif (userInput == 2): # mode refund
        # refunding
        print("You ordered:", cart);
        i = 0;
        userInput = "true";
        while (userInput == "true"):
            i += 1;
            if (i > (cart.count('|') - 1) or (cart.count('|') - 1) <= 0):
                print("There is nothing in the queue.");
                break;

            refund = int(input("Enter the item you want to return. Enter ONE item each prompt: "));

            userInput = input("Enter the size of the item ('large', 'medium', 'small'): ");
            if (userInput == "large"):
                subtotal -= 2;
                originalSubtotal -= 2;
            elif (userInput == "small"):
                subtotal += 2;
                originalSubtotal += 2;
            
            # find the nth occurrence of the divider
            parts = actualPrice.split('|', refund);
            index = len(actualPrice) - len(parts[-1]) - len('|');
            subtotal -= float(actualPrice[index + 1:actualPrice.index('|', index + 1)]);

            # find the nth occurrence of the divider
            parts = PRICE.split('|', refund);
            index = len(PRICE) - len(parts[-1]) - len('|');
            originalSubtotal -= float(PRICE[index + 1:PRICE.index('|', index + 1)]);

            userInput = input("Do you want to return anything else? Enter 'true' or 'false': ");

    elif (userInput == 3): # mode check out
        # price calculation
        # subtotal calculation
        start = cart.index('|');
        for i in range(cart.count('|') - 1):
            end = cart.index('|', start + 1);
            # find the nth occurrence of the divider
            parts = actualPrice.split('|', int(cart[start + 1:cart.index('|', start + 1)]));
            index = len(actualPrice) - len(parts[-1]) - len('|');

            subtotal += float(actualPrice[index + 1:actualPrice.index('|', index + 1)]);
            start = end;
        
        # original price calculation
        if DISCOUNT:
            start = cart.index('|');
            for i in range(cart.count('|') - 1):
                end = cart.index('|', start + 1);
                # find the nth occurrence of the divider
                parts = PRICE.split('|', int(cart[start + 1:cart.index('|', start + 1)]));
                index = len(PRICE) - len(parts[-1]) - len('|');

                originalSubtotal += float(PRICE[index + 1:PRICE.index('|', index + 1)]);
                start = end;
        
        # format prices
        subtotal = abs(round(subtotal, 2));
        originalSubtotal = abs(round(originalSubtotal, 2));

        # donation
        donation = float(input("Do you want to donate to the local food bank? If yes, enter the amount, if not, enter '0': "));

        # tax calculation
        tax = round(subtotal * 0.13, 2);
        
        # printing receipt
        print("\nRECEIPT");
        if (DISCOUNT and originalSubtotal != 0):
            print("Spcial deal applied. You got 20% off! The original subtotal was $" + str(originalSubtotal));
        print("Subtotal: $" + str(subtotal));
        print("HST: $" + str(tax));
        print("You donated $" + str(donation));
        print("Total: $" + str(round((subtotal + tax + donation), 2)));

        # update analysis
        customerCount += 1;
        revenue += subtotal + tax;
        donationReceived += donation;

    elif (userInput == 4):
        print("Data Analysis (this session)");
        if (customerCount == 0):
            print("Nobody has come since now.");
        else:
            print("Customer served:", customerCount);
            print("Revenue: $" + str(revenue));
            print("Average consumption: $" + str(round(revenue / customerCount, 2)));

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
	specification = [];
	# fetch specifications
	while (True):
		userInput = input("Enter your specifications, if none, enter *void*: ");
		specification.append(userInput);
		if ("void" in specification):
			specification = "None";
			break;
		# new specification check
		userInput = input("Continue? Enter True or False: ");
		if (userInput == "False"):
			break;
	
	# avoiding specifications
	if ("vegie" in specification):
		for i in len(tag):
			if (meat in tag[i]):
				price[i] = "N/A";
	
	# ordering
	while (True):
		# burgers
		print("Burgers:\n");
		for i in len(tag):
			if ("burger" in tag[i]):
				print("Code:", i, menu[i], "Price: $" + str(price));
		while (True):
			userInput = int(input("Please enter the code of your preferred food: "));
			cart.append(userInput);
			userInput = input("Anything else to order? Enter True or False: ");
			if (userInput == "False"):
				break;
		
		# beverages
		print("Beverages:\n");
		for i in len(tag):
			if ("beverage" in tag[i]):
				print("Code:", i, menu[i], "Price: $" + str(price));
		while (True):
			userInput = int(input("Please enter the code for your preferred food: "));
			cart.append(userInput);
			userInput = input("Anything else to order? Enter True of False: ");
			if (userInput == "False"):
				break;

		# others
		print("Others:\n");
		for i in len(tag):
			if ("others" in tag[i]):
				print("Code:", i, menu[i], "Price: $" + str(price));
		while (True):
			userInput = int(input("Please enter the code for your preferred food: "));
			cart.append(userInput);
			userInput = input("Anything else to order? Enter True or False: ");
			if (userInput == "False"):
				break;
		
		subtotal = 0; # subtotal initialization

		# order confirmation
		for i in len(cart):
				print(str(i + 1) + ".", menu[cart[i]], "Price: $" + str(price[cart[i]]));
				subtotal += price[cart[i]];
		userInput = input("Are those all the stuff you want? Enter True or False: ");
		if (userInput == "True"):
			break;
		else:
			cart.clear;
			print("Please choose what you want again.\n");

	# printing receipt
	print("\nReceipt");
	print("Name:", name);
	print("Specifications:", specification);
	print("Food you ordered:");
	for i in len(cart):
		print(str(i + 1) + ".", menu[cart[i]], "Price: $" + str(price[cart[i]]));
	
	if (DISCOUNT == True):
		print("Special-day discount applied: 20% off"); # ? not sure if it's working, tests needed
	else:
		print("No special-day discount applied");
	
	print("Subtotal: $" + str(subtotal));
	
	# new customer check
	userInput = input("Is there any more customers? Enter True or False: ")
	if (userInput == "False"):
		break;

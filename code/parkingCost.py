##############################################################
#Program: IPO Table and Pseudocode - Practice
#Date: 10/27/2022
#Author: Mohan D.
#Description: An assignment about parking cost.
##############################################################

#key point: the duration is not longer than 24 hours.
#Line 19-30 will only work if the duration is not longer than 24 hours.
#Subtotal will never has more than two decimal places.
HST = 0.13
CHARGE = 1.75
inHour = int(input("Enter your in time (Hour): "));
inMin = int(input("Enter your in time (Minute): "));
outHour = int(input("Enter your out time (Hour): "));
outMin = int(input("Enter your out time (Minute): "));

if (inHour <= 23 and inMin <= 59 and outHour <= 23 and outMin <= 59):
    if inHour > outHour: #the next day
        duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour * 60) + outMin;
    elif inHour == outHour:
        if inMin >= outMin: #the next day
            duration = ((23 - inHour) * 60) + (60 - inMin) + (outHour * 60) + outMin;
        else: #the same day
            duration = outMin - inMin;
    else: #the same day
        duration = ((outHour - inHour) * 60) + (60 - inMin) + outMin;
        if inMin == 0:
            duration -= 60;

    if (duration % 30) != 0:
        period = duration // 30 + 1;
    else:
        period = duration // 30;

    subtotal = CHARGE * period;
    tax = round((subtotal * HST), 2);
    
    print();
    print("ICS2O1 Parking Management Inc.");
    print("Your in time is:", str(inHour).zfill(2) + ":" + str(inMin).zfill(2));
    print("Your out time is:", str(outHour).zfill(2) + ":" + str(outMin).zfill(2));
    print("The duration of stay is:", duration, "minutes.");
    print("Your staying periods are:", period, "periods.");
    print("Subtotal: $" + str(subtotal));
    print("HST: $" + str(tax));
    print("Total: $" + str(round(subtotal + tax, 2)));
else:
    print("Please enter a valid time.");
    print();

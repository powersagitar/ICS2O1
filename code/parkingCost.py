##############################################################
#Program: IPO Table and Pseudocode - Practice
#Date: 10/27/2022
#Author: Mohan D.
#Description: An assignment about parking cost.
##############################################################

while(True):

    HST = 0.13
    CHARGE = 1.75
    inHour = int(input("Enter your in time (Hour): "));
    inMin = int(input("Enter your in time (Minute): "));
    outHour = int(input("Enter your out time (Hour): "));
    outMin = int(input("Enter your out time (Minute): "));

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
        period = duration / 30;

    print("duration Min:", duration);
    print("duration Hrs:", duration / 60);
    print("period:", period);
    print();

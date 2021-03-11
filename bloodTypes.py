# Belle Pan
# 260839939

donor = input("Enter donor blood type:")
recipient = input("Enter recipient bood type:")

donorType=donor[0:-1] # all but the last character of donor
donorRhesus=donor[-1] # the last character of donor

recipientType=recipient[0:-1]  # all but the last character of recipient
recipientRhesus=recipient[-1]  # the last character of recipient
# write your code here
if donorType == "O":
    if donorRhesus == "-":
        if recipientRhesus != "+" and recipientRhesus != "-":
            print("Invalid")
        elif recipientType != "O" and recipientType != "B" and recipientType != "A" and recipientType != "AB":
            print("Invalid")
        else:
            print("Compatible")
    elif donorRhesus == "+":
        if recipientType != "O" and recipientType != "B" and recipientType != "A" and recipientType != "AB":
            print("Invalid")
        elif recipientRhesus == "+":
            print("Compatible")
        elif recipientRhesus == "-":
            print("Incompatible")
        else:
            print("Invalid")
    else:
        print("Invalid")
elif donorType == "B":
    if donorRhesus == "-":
        if recipientRhesus != "+" and recipientRhesus != "-":
            print("Invalid")
        elif recipientType == "B" or recipientType == "AB":
            print("Compatible")
        elif recipientType == "O" or recipientType == "A":
            print("Incompatible")
        else:
            print("Invalid")
    elif donorRhesus == "+":
        if recipientRhesus == "+":
            if recipientType == "B" or recipientType == "AB":
                print("Compatible")
            elif recipientType == "O" or recipientType == "A":
                print("Incompatible")
            else:
                print("Invalid")
        elif recipientRhesus == "-":
            print("Incompatible")
        else:
            print("Invalid")
    else:
        print("Invalid")
elif donorType == "A":
    if donorRhesus == "-":
        if recipientRhesus != "+" and recipientRhesus != "-":
            print("Invalid")
        elif recipientType == "A" or recipientType == "AB":
            print("Compatible")
        elif recipientType == "O" or recipientType == "B":
            print("Incompatible")
        else:
            print("Invalid")
    elif donorRhesus == "+":
        if recipientRhesus == "+":
            if recipientType == "A" or recipientType == "AB":
                print("Compatible")
            elif recipientType == "O" or recipientType == "B":
                print("Incompatible")
            else:
                print("Invalid")
        elif recipientRhesus == "-":
            print("Incompatible")
        else:
            print("Invalid")
    else:
        print("Invalid")
elif donorType == "AB":
    if donorRhesus == "-":
        if recipientRhesus != "+" and recipientRhesus != "-":
            print("Invalid")
        elif recipientType == "AB":
            print("Compatible")
        elif recipientType == "O" or recipientType == "A" or recipientType == "B":
            print("Incompatible")
        else:
            print("Invalid")
    elif donorRhesus == "+":
        if recipientRhesus == "+":
            if recipientType == "AB":
                print("Compatible")
            elif recipientType == "O" or recipientType == "A" or recipientType == "B":
                print("Incompatible")
            else:
                print("Invalid")
        elif recipientRhesus == "-":
            print("Incompatible")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
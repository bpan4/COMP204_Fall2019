# Belle Pan
# 260839939 

history = input("Family history?")

# complete the program by writing your own code here

if history == "No":
    print("Low risk")
elif history == "Yes":
    ancestry = input("European ancestry?")
    if ancestry == "No":
        try:
            AR_GCCRepeat = int(input("AR_GCC repeat copy number?"))
            if AR_GCCRepeat <16 and AR_GCCRepeat >=0:
                print("High risk")
            elif AR_GCCRepeat >=16:
                print("Medium risk")
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    elif ancestry == "Mixed":
        try:
            AR_GCCRepeat = int(input("AR_GCC repeat copy number?"))
            if AR_GCCRepeat <16 and AR_GCCRepeat >=0:
                CYP3A4type = input("CYP3A4 haplotype?")
                if CYP3A4type == "AA":
                    print("Medium risk")
                elif CYP3A4type == "GA" or CYP3A4type == "AG" or CYP3A4type == "GG":
                    print("High risk")
                else:
                    print("Invalid")
            elif AR_GCCRepeat >=16:
                print("Medium risk")
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    elif ancestry == "Yes":
        CYP3A4type = input("CYP3A4 haplotype?")
        if CYP3A4type == "AA":
            print("Low risk")
        elif CYP3A4type == "GA" or CYP3A4type == "AG" or CYP3A4type == "GG":
            print("High risk")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")

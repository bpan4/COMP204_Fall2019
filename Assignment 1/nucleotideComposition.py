# Belle Pan
# 260839939

sequence = input("Enter a DNA sequence:")

# Write your program here

aCount = cCount = gCount = tCount = 0
index = 0
invalid = False
while index < len(sequence):
    base = sequence[index]
    if base == "A":
        aCount = aCount + 1
    elif base == "C":
        cCount = cCount + 1
    elif base == "G":
        gCount = gCount + 1
    elif base == "T":
        tCount = tCount + 1
    else:
        invalid = True
        break
    index = index + 1
if invalid:
    print ("Invalid")
else:
    print (aCount, cCount, gCount, tCount)
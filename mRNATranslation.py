# Belle Pan
# 260839939

mRNA = input("Enter mRNA sequence: ")

# Write your code here
length = 0
startCodon = False
i = 0
while i < len(mRNA):
    if startCodon == True:
        if mRNA[i:i+3] == "UGA" or mRNA[i:i+3] == "UAA" or mRNA[i:i+3] == "UAG":
            break
        length = length + 1
#        print(length)
        i = i + 2
    if startCodon == False and mRNA[i:i+3] == "AUG":
        length = 1
        startCodon = True
        i = i + 2
    i = i + 1
print ("The length of the amino acid sequence encoded is " , length)
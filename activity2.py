#Input a word or a sentence
string = input("Please enter your own string:  ")


string2 = (' ')
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("The Reversed String = ", string2)
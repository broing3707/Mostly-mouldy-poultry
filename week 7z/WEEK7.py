import random
letters = "abcdefghijklmnopqrstuvwxyz"
input_letter = random.choice(letters)

# don't edit the code above
# put your code below here:

print(input_letter)
if input_letter in "aeiou":
    print("vowel")
elif input_letter == "y":
    print ("it depends")
else:
    print("constenant")
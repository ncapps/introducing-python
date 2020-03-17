#4.1 
# Choose a number between 1 and 10 an assign it to the variable: secret
# Choose a number between 1 and 10 and assign it to the variable: guess
secret = 7
guess = 7

if secret < guess:
    print("too high")
elif secret > guess:
    print("too low")
else:
    print("just right")

#4.2
# Assign True or False to the variables: small and green

small = True
green = True

if small:
    if green:
        print("pea")
    else:
        print("cherry")

else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
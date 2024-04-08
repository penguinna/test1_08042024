"""
PowerOfTen
"""
# Provide your solution here

number = int(input("Enter a max 3 digit number: "))

if number < 0:
    print("number cannot be negative")
elif number > 999:
    print("number has more than 3 digits")
elif number < 10:
    print(f"{number} = {number} * 1")
elif number > 9 and number < 100:
    print(f"{number} = {number//10} * 10 + {number%10} * 1")
elif number > 99 and number < 1000:
    print(f"{number} = {number//100} * 100 + {number//50} * 10 + {number%10} * 1")
                                                # I have a math problem with 5 in 256, I do not remember how to count this module
"""
Cash Box
"""
# Provide your solution here
price = int(input("To pay: "))

if price < 0:
    print("Negative payment is invalid.")
else:
    money = int(input("Received: "))
    if money < 0:
        print("Negative received amount is invalid.")
    elif price > money:
        print("You did not pay enough.")
    else:
      print(f"Your change is: {money - price}")


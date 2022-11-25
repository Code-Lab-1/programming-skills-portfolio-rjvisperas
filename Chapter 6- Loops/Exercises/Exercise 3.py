tanong = "How old are you?"
tanong += "Type 'exit' when you're done."

while True:

    age = input("How old are you?")
    
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age < 13:
        print("You have to pay $2,000")
    else:
        print("You have to pay $5,000")
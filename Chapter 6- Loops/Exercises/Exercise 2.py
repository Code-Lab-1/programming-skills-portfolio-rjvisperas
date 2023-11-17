q = "How old are you?"
q += "\nType 'exit' when you are finished. "

while True:
    age = input(q)
    if age == 'exit':
        break
    age = int(age)

    if age < 3:
        print("  You're free!")
    elif age < 13:
        print("  Your ticket is $2,000.")
    else:
        print("  Your ticket is $5,000.")
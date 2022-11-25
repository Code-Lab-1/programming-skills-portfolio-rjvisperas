q = "\nWhat topping would you like to add on your pizza?"
q += "\nType 'exit' when you are finished: "

while True:
    topping = input(q)
    if topping != 'exit':
        print("  Your wish we command so we gonna add " + topping + " to your pizza.")
    else:
        break
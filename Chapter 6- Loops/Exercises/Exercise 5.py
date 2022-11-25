orders = [
    'ginataan', 'pinakbet', 'bicol express', 'pancit',
    'poto', 'kare-kare', 'Adobong manok']
food = []

print("I'm sorry, we're all out of Adobong manok today.")
while 'Adobong manok' in orders:
    orders.remove('Adobong manok')

print("\n")
while orders:
    current_sandwich = orders.pop()
    print("I'm working on your " + current_sandwich + " food.")
    food.append(current_sandwich)

print("\n")
for sandwich in food:
    print("I made a " + sandwich + " food.")
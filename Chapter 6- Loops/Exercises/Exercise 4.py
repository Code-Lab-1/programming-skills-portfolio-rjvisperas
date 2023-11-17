orders = ['Migilito', '2x2', '4x4', 'Pulang Kabayo']
sandwiches = []

while orders:
    current_sandwich = orders.pop()
    print("I'm working on your " + current_sandwich + " Beverages.")
    sandwiches.append(current_sandwich)

print("\n")
for sandwich in sandwiches:
    print("I made a " + sandwich + " Beverages.")
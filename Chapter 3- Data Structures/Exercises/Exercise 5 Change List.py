guests = ['Klaithem bintwalee', 'Errol Carranza', 'Dan Franco']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")
# Errol can't go. Let's invite someone
del(guests[1])
guests.insert(1, 'Pauline Fernandez')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")
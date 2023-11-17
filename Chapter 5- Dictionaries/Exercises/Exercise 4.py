g = {
    'Arjay': 'Bilibinas',
    'Klai': 'UAE',
    'Errol': 'Filifines',
    'Pau': 'Turkey',
    'Dan': 'Korea',
    }

for a, b in g.items():
    print("I'm " + a.title() + " From " + b.title() + ".")

print("\nThe following names are included in this data set:")
for a in g.keys():
    print("- " + a.title())

print("\nThe following countries are included in this data set:")
for b in g.values():
    print("- " + b.title())
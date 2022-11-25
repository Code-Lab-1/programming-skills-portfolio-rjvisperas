
pets = []


pet = {
    'animal type': 'Cat',
    'name': 'Ming ming',
    'owner': 'Anwar',
    'weight': 4,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'red horse',
    'owner': 'san miguel',
    'weight': 5,
    'eats': 'liver',
}
pets.append(pet)

pet = {
    'animal type': 'crocodile',
    'name': 'rawaad',
    'owner': 'klai',
    'weight': 45,
    'eats': 'people',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
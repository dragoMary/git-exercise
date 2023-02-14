'''
person = {
    'name': 'Bart Simpson',
    'address': '742 Evergreen Terrace'
}

print(f"{person['name']}, {person['address']}")


#Task2
bart = {'name': 'Bart Simpson'}
homer = {'name': 'Homer Simpson'}
address = {'address': '742 Evergreen Terrace'}

bart.update(address)
homer.update(address)

print(homer['address'])

#Task 3
ages = {"Peter": 36, "Robin": 29, "Michael": 33}

for name, age in ages.items():
    print(f"{name} is {age} years old")

'''


#Task4

animals = {"Alligator": 5, "Tiger": 22, "Parrot": 11, "Hamster": 10, "Dolphin": 7}

for animal in list(animals.keys()):
    if animal.endswith("r"):
        animals.pop(animal)

for animal, value in animals.items():
    print(f"{animal}: {value}")





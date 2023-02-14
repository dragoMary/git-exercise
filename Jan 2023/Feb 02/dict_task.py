task1_dict = {
    1: 1,
    2: 6,
    3: 9,
    4: 16,
    5: 20,
    6: 36,
    7: 7,
    8: 64,
    9: 81,
    10: 100,
    11: 121,
    12: 14,
    13: 169,
    14: 19,
    15: 225
}

task1_dict = {}
for i in range(1,16):
    task1_dict[i] = i**2
print(task1_dict)

'''
#SWAP items
task2_dict = {'Name': 'Julia', 'Age': 36}

new_dict = {value: key for key, value in task2_dict.items()}
print(new_dict)

#Remove key 'name'

task3_dict = {'Name': 'Julia', 'Age': 36, 'f_name': 'Shcherbyna'}
a = task3_dict.pop('Name')
print(a)
print(task3_dict)


#Check if dictionary contain key 'zamek'
task4_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
if "zamek" in task4_dictionary:
    print("The key 'zamek' exists in the dictionary.")
else:
    print("The key 'zamek' does not exist in the dictionary.")


# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

d3.update(d1)
d3.update(d2)
print(d3)

'''
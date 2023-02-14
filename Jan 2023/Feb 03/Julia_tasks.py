'''

# Task 1
# loop dictionary with enumerate function for each item in dictionary print with formatted string method:
# Hello I am item of dictionary with key 'age' my value is '54' and my position in dictionary is 1
my_dict = {
    'name': 'Bob',
    'age': 54,
    'address': 'Bla-Bla street',
    'grade': 3,
    'city': 'Berlin',
    'country': 'Germany'
}
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Hello I am item of dictionary with key '{key}' my value is '{value}' and my position in dictionary is {index + 1}")


# Task 2
names = ['Bob', 'Marlen', 'Jessica', 'David', 'Piet']
countries = ['Germany', 'Portugal', 'USA', 'England', 'Germany']
set_prize = {'Car', '10 000$', 'Vacation in Maldives', 'Dinner in restaurant', 'Trip to Disneyland'}

zip_var = zip(names, countries, set_prize)
for name, country, prize in zip_var:
    print(f"Prize for {name} from {country} is {prize}")


# Task 3

def sort_profiles(profiles, sort_by, reverse=True):
    if sort_by == 1:
        key = "name"
    elif sort_by == 2:
        key = "age"
    elif sort_by == 3:
        key = "tall"
    else:
        key = "weight"
    return sorted(profiles, key=lambda x: x[key], reverse=reverse)

dict1 = [
   {"name": "John", "age": 31, 'tall': 1.76, 'weight': 79},
   {"name": "Mary", "age": 46, 'tall': 1.69, 'weight': 55},
   {"name": "Lucy", "age": 25, 'tall': 1.97, 'weight': 102}
]

print(sort_profiles(dict1, 2, reverse=True))
# daca setam reverse True , python intoarce cea mai inalta valoare a unei key : age, name, tall etc
# Si intoarce cea mai mica valoare daca setam  reverse False
# punem reverse=reverse pt ca se specifica  sortarea  fie ascendent fie descendent(false or true)


# Task 4

def insert_to_list():
    sample_list = [1, 2, 3, 4, 5]
    string = "emp"
    new_list = list(map(lambda x: f"{string}{x}", sample_list))
    return new_list

print(insert_to_list())

# f' string x returneaza valoarea lui x si concateneaza stringul cu x
# functia map aplica apoi aceasta functie anonima fiecarui element din sample_list

'''


# Task 5
# Write a program with filter() function what will filter all pdf file names from list
files_list = ['image3464456.jmp',
              'class.pdf', 'requirenments.txt',
              'some_data.md', 'presentation.pdf',
              'my presentation.pdf', 'dog.jpeg']


pdf_files = list(map(lambda x: x if '.pdf' in x else None, files_list))
pdf_files = [x for x in pdf_files if x is not None]
print(pdf_files)

#non_pdf_files = list(filter(lambda x: '.pdf' not in x, files_list))
#print(non_pdf_files)
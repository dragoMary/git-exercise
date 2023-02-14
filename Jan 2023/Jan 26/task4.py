
#Task4

def print_user_profile(gender="female", first="Jane", last="Doe", pictures=[]):
    #pictures.insert(0, "common_header.png")


    if gender == "male":
        first = "John"

    if not pictures:
        pictures = []
    print(f"The user {first} {last} has the following pictures:")
    print("common_header.png")
    for picture in pictures:
        print(picture)


test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
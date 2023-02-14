
settings = {"title": "Citizen Kane"}

def change_site_title(second_title):
    global settings
    settings["title"] = second_title

print(settings)
change_site_title("A new fancy title")
print(settings)
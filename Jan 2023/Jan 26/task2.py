#Task2


default_settings = {"title": "Citizen Kane"}
settings = {"title": "Citizen Kane"}

def get_title(settings = default_settings ):
    return settings["title"]

def change_site_title(new_title, settings=default_settings):
    settings["title"] = new_title

print(get_title(settings))
print(get_title())

change_site_title("A new fancy title", settings)

print(get_title(settings))
print(get_title())







#Task3

default_settings = {"pages": []}
settings = {"pages": []}

get_pages = lambda s=default_settings: s["pages"]        # get_pages function is defined with a default parameter s=default_settings
add_page = lambda page, s=default_settings: s["pages"].append(page)

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))




#if its call the function without any arguments, it will use default_settings as the settings dictionary.
# The add_page function is defined with two parameters, the first one is mandatory.
#The second one is optional with a default value of default_settings.




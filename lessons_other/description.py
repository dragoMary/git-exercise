
'''
description = 'Paris is the city of love'
print(description)
print(description.split('a'))
print(description.split())

news = 'Ein 17-jähriger Schüler steht im Verdacht im münsterländischen Ibbenbüren (NRW) seine Lehrerin umgebracht zu haben.'
print(news)
print(news.split(maxsplit=3))



space = '#'
print(space.join(news))
'''

#STRING SLICING

name = 'monalisa'
print(name[0:3])
print(name[0:])
print(name[2:6])
print(name[:3])
print(name[0:8:2]) #'skip letter every 2 steps'
print(name[::-1]) #reverse the name, characters

description = 'Paris is a city of love'
print(description.replace('Paris', 'London'))

song = "  Paris is a city of love  "
print(song.strip())
print(song.rstrip())

town = 'PBerlin'
print(town.strip('P'))

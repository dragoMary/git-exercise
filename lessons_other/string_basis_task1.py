news = 'Der Blick auf den Kontostand verheißt im Januar für viele Deutsche nichts Gutes'  # concatenation
print(news + 'Es gibt aber auch eine gute Nachricht.')

traveling = 'mountains and seas whrever you go'  #lenght of text
print(len(traveling))
print(traveling.upper())
print(traveling.capitalize())

#USAGE

city1 = ' London '    #task 1
print(city1)

city2 = 'berlin'
population = 3645000
print(city2.capitalize(), ':', str(population))     #task2

city3 = 'london'                                    #task3
population = 900000
print('city:', city3.capitalize(), city3.isalpha())
print(population)


text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."   #task4
print('capital', text.index('capital'))


#task5
text = 'Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.'
print(text.split())

#task6

text = 'Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburgs capital.'
print(text.replace('capital', 'capital of Germany'))


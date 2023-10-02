# List, Tupel, Sets, Dictionary
'''
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''
# cities=['nashik','pune','mumbai','surat','chennai','delhi']

# print(len(cities))
# print(len("lets check length of this string"))

# print(cities[len(cities)-1])
# print(cities[5])
# print(cities[-1])
# print(cities[-1])
# print(cities[::-1])
# for city in cities:
#     print(city.upper())

# cities.append("panjim")
# print(cities)
# cities.insert(5,"pune")
# print(cities)
# newCities=['hydrabaad','ahemdabaad','prayagrraj']
# cities.extend(newCities)
# print(cities)
# cities[2]="Bombay"
# print(cities)
# popeedItem=cities.pop()
# print(cities)
# print(popeedItem)
# cities.remove("Bombay")
# print(cities)
# cities.clear()
# print(cities)

# names=('sanket','sushil','divakar','amit','parth','rudrani','amit')
# names[0]="rahul"

# print(set(cities))

# animals={'dog','cat','tiger','chitah','lepord','dog','cat'}
# print(animals)

person={
    "name":"amit mali",
    "age":33,
    "married":True,
    "laguages":['python','php','c','c++','javascript','htm','css'],
    "address":{
        "city":"Nashik",
        "state":"Maharastra",
        "zip":422009
    }
}

# print(person['name'])
# for key in person:
#     print(person[key])

# print(person.keys())

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# print(person.items())
# for key,value in person.items():
    # key,value=item
    # print(f"{key} = {value}")

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.union(s2))  # or 's1 | s2'
# {1, 2, 3, 4, 5}

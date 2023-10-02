names=('sanket','sushil','divakar','amit','parth','rudrani','amit')

# def makeItCapital(name):
#     return name.capitalize()

# print(makeItCapital(names[0]))

# makeItCapital2=lambda name:name.capitalize()
# print(makeItCapital2(names[0]))
# newNames=map(makeItCapital,names)
newNames=map(lambda name:name.capitalize(),names)
# print(list(newNames))
# print(names)
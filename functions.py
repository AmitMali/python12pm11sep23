def hello(name="user"):
    print(f"Hello {name} ")


hello("amit")
hello("Sahil")
hello()


def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def add(no1, no2):

    return no1 + no2



# print(add(10, 20))
#
# print(isEven(7))
# print(isEven(9))
# print(isEven(4))
# print(isEven(2))
#

foo="i am global variable"

def local():
    foo="i am global declared in function"
    print(foo)
    def local2():
        foo2="nested local"
        print(foo2,foo)

print(foo)
local()
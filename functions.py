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
'''
function that accepts price as an argument and
returns price with gst added,
if your does not pass gst per default value should 5%,
also provide optional arguments to pass shipping rate 
'''

def mrp(price,gst=5,shipping=0):
    gst = (price * gst) / 100
    total = price + shipping + gst
    return [gst/2,total,price]

def printBill(price,discount=0):
    def mrp(price, gst=5, shipping=0):
        gst = (price * gst) / 100
        total = price + shipping + gst
        return [gst / 2, total, price]

    gst, mrp, price = mrp(price)
    print(f'''
        Price: {price}
        SGST : {gst}
        CGST : {gst}
        --------------
        Total : {mrp}
    ''')
# print(mrp(100))
# print(mrp(100,12))
# print(mrp(100,12,30))
# print(mrp())

[gst,total,price]=mrp(100)
printBill(100)


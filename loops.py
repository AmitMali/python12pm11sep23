
# no=1
# while no<=10:
#     print(no)
#     no=no+1

# def myRange(start,end,step=1):
#     no = start
#     while no <end:
#         print(no)
#         no = no + step
#
# myRange(1,11,2)

def printNumberTable(num):
    no = 1
    while no<=10:
        print(f"{num} x {no} = {no*num}")
        no=no+1



printNumberTable(2)
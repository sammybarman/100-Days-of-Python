# given two variables swap their values by
# not using a third variable (mathematical solution)
# using a third variable (swap)
# using a built in function (swap)

def maths(a, b):
    a = a+b
    b = a-b
    a = a-b
    return a, b


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def built_in(a, b):
    a, b = b, a
    return a, b


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Numbers are : ", a, b)
print("Swapping using method one")
print("Numbers are - ", maths(a, b))
print("Swapping using method two")
print("Numbers are - ", swap(a, b))
print("Swapping using method three")
print("Numbers are - ", built_in(a, b))

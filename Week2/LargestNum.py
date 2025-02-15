numbers = [1, 2, 3, 4, 7, 9]


def LargestNumber():
    x = 0
    for i in numbers:
        if (i >= x):
            x = i
        else:
            x = x
    return x


print(LargestNumber())

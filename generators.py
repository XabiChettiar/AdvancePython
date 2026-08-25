def complex(i):
    return i*i


def genNum():
    for i in range(5):
        yield complex(i)


# number=genNum()

# print(number,type(number))

# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


gen=(i for i in range(5))

print(list(gen))
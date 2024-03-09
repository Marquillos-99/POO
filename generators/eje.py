#def generator():
#    yield 5
#
#a = generator()
#print (next(a))
#print (next(a))

def generator():
    n = 10
    yield n

    n += 5
    yield n

    n -= 2
    yield n

for i in generator():
    print(i)
#def primerosnum(n):
#    nums = []
#    for i in range(n):
#        nums.append(i)
#    return nums

#print(sum(primerosnum(100)))


def primerosnum(n):
    num = 0
    for i in range(n):
        yield num
        num += 1
print(sum(primerosnum(100)))

print(sum(range(100)))
from functools import reduce
integer = [1,2,3,4,5,6,7,8,9,10,11,12]
sumcum = reduce(lambda a,b: a + b, integer)
print (sumcum)
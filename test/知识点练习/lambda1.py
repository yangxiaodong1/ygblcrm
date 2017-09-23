# Author : July  Yang 
from functools import reduce

li = [1,2,3,4,5]
new_li = map(lambda x:x+1,li)
print(list(new_li))

new_li2 = filter(lambda x:x % 2 !=0,li)
print(list(new_li2))

new_li3 = reduce(lambda x,y:x+y,li)
print(new_li3)

square = lambda x,y:x*y
print(square(2,3))








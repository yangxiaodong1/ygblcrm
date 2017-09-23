# Author : July  Yang 
import re
from operator import itemgetter, attrgetter
old_string = "A small small small sample of texts sample of"
lst = re.split('[0-9\W]+', old_string)

d = {}
for i in lst:
    if i not in d:
        d[i]=0
    d[i]+=1


print(sorted(d.items(),key=lambda item:item[1]))
print(sorted(d.items(),key=lambda item:item[1])[0:3])


# d = {'data1':3, 'data2':1, 'data3':2, 'data4':4}
# print(sorted(d.items(), key=itemgetter(1), reverse=True)  )






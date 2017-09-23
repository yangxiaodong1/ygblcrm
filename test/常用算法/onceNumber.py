# Author : July  Yang 
list1 = [9,1,1,2,2,3,74,1,5,52,3,3,4,4,4,2,5,1,1,1,]
dict1 = {}
k =0
for i in list1:
    if i not in dict1:
        dict1[i] = 0
    dict1[i] +=1
print(dict1)

for index,value in dict1.items():
    if value == 1:
        print(index)






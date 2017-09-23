# Author : July  Yang 
list1 = [9,1,1,2,2,3,74,1,5,52,3,3,4,4,4,2,5,1,1,1,]

dict2 ={}

for i in list1:
    if i not in dict2:
        dict2[i]=0
    dict2[i]+=1

for k,v in dict2.items():
    print(k,'------',v)







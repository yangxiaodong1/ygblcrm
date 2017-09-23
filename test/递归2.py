# Author : July  Yang 
# def fab(max):
#     n,a,b=0,0,1
#     while n<max:
#         a,b=b,a+b
#         print(b)
#         n+=1
#     return 'done'
#
# print(fab(10))
def ab(n):
    if n<=1:
        return 1
    else:
        num = ab(n-1)+ab(n-2)
        return num

for i in range(10):
    print(ab(i))









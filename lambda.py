"""count=0
def orders(*items,**details):
    print(f"details:{details}")
    print(f"details:{items}")
    global count
    count+=1
    print(f"total orders:{count}")
orders("pizza",name = "neha",destination = "cvcrop")"""
l=[[1,2],[3,4],[5,6]]
"k = list(map(lambda x:x.append(5),l))"
k = list(map(lambda x:x+[5],l))
print(k,l)
l1=[1,2,3,4,5,6,7,8,9]
c= list(filter(lambda x:x&1,l1))
print(c)
l2 = [3,6,1,2,5,9,12,16]
"""a = input()
b = ['a','e','i','o','u']
d = list(filter(lambda x:x not in  b ,list(a)))
print(d)"""
l3 = [1,7,8,12,14,21,22,63,60]
z = list(map(lambda x:x**3,l3))
x = list(filter(lambda y: y%4 == 0,z))
print(x)
si = list(filter(lambda x:x%4==0,map(lambda x:x**3 ,l3)))
print(si)
from functools import reduce
a = reduce(lambda x,y :x+y ,l1)
print(a)
st = ['.','j','o','i','n','(',')']
b = reduce(lambda x,y:x+y , st ,"@")
print(b)
li = [1,7,6,3,8,9,11,10]
c = reduce(lambda x,y : x if x>y else y, li)
print(c)
q = [0,22,31,35,23,6]
d = reduce(lambda x,y: x+y,list(filter(lambda x:x%3==0,map(lambda x :(x*1.8)+32,q))),0)
print(d)
x = list(filter(lambda x: x%3==0 ,map(lambda x : (x*1.8)+32 , q)))
z = reduce(lambda x,y :x+y,x ,0)
print(z)
l = [23,21,27,28,44,46]
a=sorted(l,key=lambda x:x%7,reverse=True)
print(a)

'2'
a = [1,2,3,4]
b = [10,20,30,40]
c = list(map(lambda x,y:x+y , a,b))
print(c)
'3'
nums = [12,15,7,18,20,21,25]
d = list(filter(lambda x: x%3==0 or x%5==0 ,nums))
print(d)
'4'
from functools import reduce
nums = [1,2,3,4]
e = reduce(lambda x,y:x+y ,nums,10)
print(e)
'5'
nums = [[1,2],[3,4],[5,6]]
result = list(map(lambda x:x.append(10),nums))
print(result)
print(nums)
'1'
l1 = [[1,2],[3,4],[5,6]]
x = list(map(lambda x:x.append(5),l1))
print(l1,x)
'2'
d = {"apple":100,'banana':40,"cherry":150}
f = list(filter(lambda x:d[x]>50 ,d))
print(f)
'3'
"""n = list(map(int,input().split()))
z = reduce(lambda x,y:x if x>y else y , n)
print(z)"""
'5'
"""n = input()
s = list(map(ord,list(n)))
print(s)"""
'6'
"""e = list(filter(lambda x : x not in "aeiou",input()))
print(e)"""
'7'
input = ['p','y','t','h','o','n']
f = reduce(lambda x,y:x+y,input)
print(f)
'8'
l = [10,350,10,350,20]
z= list(map(lambda x:id(x),l))
print(z)
'10'
l2=[5,10,15,20,25,30]
g = reduce(lambda x,y:x+y,list(filter(lambda x:x%5==0,map(lambda x:x**2,l2))))
print(g)
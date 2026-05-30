def f1(*a):
    print((sum(a))/(len(a)))
f1(10,20,30,40,50)
def f2(a):
    if (a>=0):
        return "positive"
    else:
        return "negative"
print(f2(10))
print(f2(-5))
def f3(a):
    for i in range(1,a+1):
        if i%2 == 0:
            print(i,end =" ")
f3(20)

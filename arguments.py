def fun(*a):
    print(a)             #positional
    print(*a)           #unpacked
fun(10,20,30,40,50)
def fun3(a,b,c,d):
    print(a,b,c,d)
def fun2(**b):
    print(b)                   #keyword
    fun3(**b)
fun2(a=75,b=30,c=40,d=70)
def fun5(*a,**b):
    print(a,b,sep = "\n")
fun5(10,1,7,38,6,7,90)
fun5(10,1,7,38,6,7,90,a = 75,b=30)
def fun4(*a):
    print(sum(a))
fun4(1,7,8,25,30,60,70)
def fun6(*a):
    sum = 0
    for i in a:
        if(i%2 == 0):
            sum += i
    print(sum)
fun6(1,7,8,25,30,60,70)
def fun7(*a):
    sum = 0
    i = 0
    while i < len(a):
        sum += a[i]
        i += 2
    print(sum)
fun7(1,2,3,4,5,7,7,8,8,10)
'''
#func with arguements without return type

def fun(s,d):
    for i in s:
        d[i]=s.count(i)
    print(d)
fun('kavya',{})


#func without arguements and with return type

def fun():
    l=[1,2,3,4]
    sum=0
    for i in l:
        sum+=i
    return sum
print(fun())


#func with arguements and with return type

def pal_lst(l,l1):
    for i in l:
        l1=[i]+l1
    return l1
l=[1,2,2,1,3,1,2,2,1]
res=pal_lst(l,[])
if res==l:
    print('pal')
else:
    print('not')


#func without arg and without return type

def fib():
    n=int(input('enter a num'))
    fib=0
    fib1=1
    print(fib,fib1,sep='\n')
    for i in range(0,n):
        fib2=fib+fib1
        fib=fib1
        fib1=fib2
        print(fib2)
fib()
'''
l=[10,26,83,45,15,10]
#print(list(set(l)))
c=[]
for i in l:
    if i in c:
        l.remove(i)
    else:
        c+=[i]
print(l)


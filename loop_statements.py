
#print even nums in a given range
n=int(input("enter a num"))
for i in range(0,n):
    if i%2==0:
        print(i)
    else:
        continue

#pgm to print fibanocci series
fib=0
fib1=1
print(fib,fib1,sep='\n')
for i in range(0,n):
    fib2=fib+fib1
    fib=fib1
    fib1=fib2
    print(fib2)


#pgm to print fibanocci nums within the given range
fib=0
fib1=1
print(fib)
for i in range(1,n):
    fib2=fib+fib1
    if i==fib2:
        print(i)
        fib=fib1
        fib1=fib2
    else:
        continue


#pgm to print the second largest in a list
l=[3,5,2,6,7,10,8]
#l.remove(max(l))
#print(max(l))

c=0
for i in range(0,len(l)):
    if l[i]>c and l[i]<max(l):
        c=l[i]

    else:
        continue
print(c)


#pgm to print square nums in a given range
for i in range(n):
    for j in range(1,(i//2)+1):
        if i==j*j:
            print(i)
            break
        else:
            continue
        

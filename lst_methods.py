'''
col=['red','green','blue','yellow','white','skyblue']
res=[]
for i in col:
    res=res+[len(i)]
for i in col:
    for j in res:
        if len(i)==max(res):
            print(i)
            break

col=['red','green','blue','yellow','white','skyblue']
for i in col:
    if len(i)>5:
        print(i)

col=['red','green','blueb','yellow','whitew','skyblue']
for i in col:
    if i[0]==i[len(i)-1]:
        print(i)


lst=[1.0,1.5,9,10.7,2]
lst.sort()
print(lst)


l=['bread','biscuit','cupcake','pastry','pancake']
l.sort(reverse=True)
print(l)


lst=['apples','apples','bananas','apples','pear','pear','apples','bananas']
l1=['apples','bananas','pear']
for i in lst:
    for j in l1:
        print(lst.count(j))
    break

L= ['aaa','red','round','ccc','road','orange']
L1=[]
for i in L:
    if len(i)>=3 and i.startswith('r'):
        L1.append(i)
print(L1)
'''
#pgm to remove concecutive duplicate items

L=[1,1,2,2,3,4,5,4,4,5,5,6,7]
L1=[]
for i in range(0,len(L)):
    if L[i]!=L[i-1]:
        L1+=[L[i]]
    else:
        continue
print(L1)

    

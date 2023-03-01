l=[10,20,40,30,50]
for i in l:
    print(max(l))   #first largest
    l.remove(max(l))
    print(max(l))   #prints second largest num
    l.remove(max(l))
    print(max(l))   #third largest
    break


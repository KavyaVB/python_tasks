i=input("enter PIN")
if not('0'<=i<='9' and 4<=len(i)<=6 and i==' '):
    print('invalid')
else:
    print('valid')

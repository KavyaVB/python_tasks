n1=1
n2=3
if type(n1) and type(n2)==int:
    print(str(n1)+str(n2))
elif type(n1) or type(n2)==str:
    print(int(n1)+int(n2))
else:
    print('None')

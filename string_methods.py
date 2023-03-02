'''
s='abcdefghijk'
print(s[0:(len(s)//2)-1]+s[-1:-8:-1])


def myCopy(s,s1,i):
    if i==len(s):
        print(s1)
    else:
        s1=s1+s[i]
        myCopy(s,s1,i+1)
s='abcdefghijk'
s1=''
i=0
myCopy(s,s1,i)
'''
def myCopy(s='abcdefghijk',s1='',i=0):
    if i!=len(s):
        s1=s1+s[i]
        return myCopy(s,s1,i+1)
    return s1
res=myCopy()
print(res)

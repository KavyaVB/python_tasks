'''
def move(s,s1):
    for i in range(0,len(s)):
        s1+=chr(ord(s[i])+1)
    return s1
s=input('enter a string')
print(move(s,s1=''))
'''
#using recursion function
def move(s,s1,i=0):
    if i>=len(s):
        return s1
    else:
        s1+=chr(ord(s[i])+1)
        return move(s,s1,i+1)
s=input('enter a string')
print(move(s,s1='',i=0))
        

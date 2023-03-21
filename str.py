s=input('enter a string')
#pgm to check whether the string is pal/not
print('rev of str is:',s[::-1])
if s[::-1]==s:
    print('pal')
else:
    print('not pal')


#pgm to remove last char in a str
s1=''
i=0
while i<len(s)-1:
    s1=s1+s[i]
    i+=1
print(s1)


#pgm to reverse a str
print(s[::-1])

#pgm to find len of a str
print(len(s))


#pgm to avoid spaces in str len
c=0
for i in s:
    if i!=' ':
        c+=1
    else:
        continue
print(c)


#pgm to print even index char
for i in range(0,len(s),2):
    print(s[i])


#pgm to print even len words in a sentence
n=s.split(' ')
print(n)
for i in n:
    if len(i)%2==0:
        print(i)
    else:
        continue

#pgm to print uppercase half str
s1=''
for i in range(0,len(s)):
    if i>=len(s)//2 and 'a'<=s[i]<='z':
        s1+=chr(ord(s[i])-32)
    elif i<=len(s)//2 and 'A'<=s[i]<='Z':
        s1+=chr(ord(s[i])+32)
    else:
        s1+=s[i]
print(s1)


#pgm to capitalize first & last char
s1=''
for i in range(0,len(s)):
    if (i==0 or i==len(s)-1) and 'a'<=s[i]<='z':
        s1+=chr(ord(s[i])-32)
    else:
        s1+=s[i]
print(s1)

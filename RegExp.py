#pgm to validate phone num
import re
'''
def isValid(s):
    Pattern=re.compile("(\+)(91)(\-)[6-9][0-9]{9}")
    return Pattern.match(s)
s=input("enter your num")
if (isValid(s)) and len(s)==14:
    print("valid")
else:
    print("invalid")

    
#pgm to extract all numbers from a string
p=re.compile('\d+')
print(p.findall("I was in Banglore from 26th April 2021 to 30-01-2022"))


#pgm to check if the entered date is in dd/sss/dddd format
date=input('enter date in dd/mmm/yyyy format')
def valDate(date):
    pattern=re.compile('[0-31]{2}\/[a-zA-Z]{3}\/[1900-2030]{4}')
    return pattern.match(date)

if (valDate(date)):
    print("valid")
else:
    print("invalid")
 

#pgm to check if the entered date is in dd/sss/dddd format

s="Twelve:12 Eighty nine:89 thirty-two:32"
def substr(s):
    res1=re.findall(r"\D+:",s)  #returns the characters which are located before :
    res2=re.split(r"\:",s,maxsplit=1)  #return the sentence with only one split @first occurance
    
    return res1,res2


out=substr(s)
print(out)

#pgm to remove whitespaces & replace with $

s='abc 12\de 23\n f45 6'
def rem(s):
    pattern1=re.sub(' ','',s)   #return the sentence without any spaces
    pattern2=re.sub(' ','$',s)  #return the sentence where spaces are replaced with $ 
    return pattern1,pattern2
res=rem(s)
print(res)

#pgm to check whether the string is present in the given sentence/not
s='Python is easy to learn..but only if you practice Python it can be easy'
def check(s):
    res=re.search(r'Python',s)
    return res

if (check(s)):
    print(True)
else:
    print(False)


#pgm to print a list of 3digit num followed by a space which is followed by 2digit num    
s='1233 896 45 908 99'
def find(s):
    pattern=re.compile(r'\b\d{3}\s\d{2}\b')
    return pattern.findall(s)
res=find(s)
print(res)
'''
s='python'
#print(re.search(r'p',s))
res=re.search(r'p',s)
print(res.group())

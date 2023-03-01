'''
file=open("C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt","w+")
file.writelines("I am a little teapot\nShort and stout\nHere is my handle (one hand on hip)\nHere is my spout (other arm out straight)")
print(file.read())
file.close()
'''

file=open("C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt","r")
print('Before replacement\n',file.read())
search_txt="Here"
replace_txt="There"

with open('C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt','r')as file:
    data=file.read()
    data=data.replace(search_txt,replace_txt)
with open('C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt','w')as file:
    file.write(data)
with open('C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt','r')as file:
    print('After replacement\n',file.read())
print("txt replaced")

'''
#using reg exp
import re
def replacetxt(search_txt,replace_txt):
    with open('C:/Users/Kavya VB/OneDrive/Desktop/file_handling_ex.txt','r+')as f:
        file=f.read()
        file=re.sub(search_txt,replace_txt,file)
        f.write(file)
        f.truncate()
    return "txt replaced"
print(replacetxt('here','There'))

import re
#file=open("dummy.txt","r")
with open('dummy.txt')as f:
    fin=f.read()
    print(re.search(r'High\s\D+\n\b',fin).group())
'''    

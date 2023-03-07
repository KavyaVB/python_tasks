'''
a=20
b=1
c = 1
d =10
exp2 = a*b^c+d//2
print(exp2)

a=3
b=2
res=lambda a,b:a^b
print(res(a,b))

a=2
a=a*2+6
print(a)


#what will be the output for following expression
exp=4/(3*(2-1))
print(exp)

#4/(3*(2-1)) and 4/3*(2-1) same/not

exp1=4/(3*(2-1))
exp2=4/3*(2-1)
print(exp1==exp2)
'''

a=10
b=15
c=4
d=2
'''
#AND operator
exp=a+d&d*(b//c)
print(exp)


#OR operator
exp=c*d+a|a%c//b
print(exp)


#XOR operator
exp=a//b+(d*c)^b%a
print(exp)


#Ones compliment
print(~b)
'''

#Lshift
print(a<<2)

#Rshift
print(a>>2)

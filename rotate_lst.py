n=1
lst=[1,2,3,4,5]
if n>len(lst):
    n=int(n%len(lst))
lst=(lst[-n:]+lst[:-n])
print(lst)

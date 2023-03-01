d={'a':1,'b':2,'c':3}
#inv_d={v:k for k,v in d.items()}
#print(inv_d)

inv_d={}
for k,v in d.items():
    inv_d.update({v:k})
print(inv_d)

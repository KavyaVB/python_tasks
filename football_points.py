win_p=3
draw_p=1
loss_p=0
def football(wins,draws,losses):
    res=wins,draws,losses
    print(res)
    return (res[0]*win_p)+(res[1]*draw_p)+(res[2]*loss_p)

result=football(3,4,2)
print(result)
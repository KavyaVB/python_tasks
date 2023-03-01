
import math
def calc_time(N,M,sec=21):
    calc=(((21*N)/60)*30)*M
    intp,decp=int(calc),calc-int(calc) #integer part and decimal part
    #calc1=math.modf(calc)
    #print(calc1)-->print as (0.0,588.0)
    my_str='{},{}-->{}min and {}sec'
    print(my_str.format(N,M,intp,decp))
N=int(input('enter num of times wahsed your hands'))
M=int(input('enter the num of months'))
calc_time(N,M,sec=21)
'''
#using class & object
class wash_hands:
    Min=60
    days=30
    sec=21

    def __init__(self,no_times,no_months):
        self.no_times=no_times
        self.no_months=no_months

    def calc(self):
        calc=(((wash_hands.sec*self.no_times)/wash_hands.Min)*wash_hands.days)*self.no_months
        intp,decp=int(calc),calc-int(calc)
        my_str='({},{})-->{}min and {}sec'
        print(my_str.format(self.no_times,self.no_months,intp,decp))

no_times=int(input('enter num of times wahsed your hands'))
no_months=int(input('enter the num of months'))
time=wash_hands(no_times,no_months)
time.calc()

class animals:
    chicken=2
    cow=4
    pig=4
    def __init__(self,no_chicken,no_cow,no_pig):
        self.no_chicken=no_chicken
        self.no_cow=no_cow
        self.no_pig=no_pig

    def disp(self):
        val=self.no_chicken,self.no_cow,self.no_pig
        res=animals.chicken*val[0],animals.cow*val[1],animals.pig*val[2]
        print(val)
        print(sum(res))

obj=animals(1,2,3)
obj.disp()
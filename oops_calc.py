class calculator:
    def __init__(self):
        pass

    def add(self,n1,n2):
        return n1+n2

    def sub(self,n1,n2):
        return n1-n2

    def mul(self,n1,n2):
        return n1*n2

    def div(self,n1,n2):
        if n2==0:
            return 'ZeroDivisionError'
        return n1/n2

calc=calculator()
print(calc.add(2,3))
print(calc.div(10,0))


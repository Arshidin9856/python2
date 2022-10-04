class Investment:
    def __init__(self,p,i) -> None:
        self.p=p
        self.i=i
    def value_after(self,n): return self.p*n*(1+self.i)
    def __str__(self) -> str:
        return f'Principal - ${self.p}, Interest rate - {self.i}%'

constructor=Investment(1000,3.5)
print(constructor.value_after(5))
print(constructor)
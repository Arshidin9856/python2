class shop:
    def __init__(self,name,amount,price) -> None:
        self.name=name
        self.amount=amount
        self.price=price

    def get_price(self,n):
        # if n>=self.amount: print('didnt have')
        if n<=10 and n>=1: return self.price
        elif n<=99 and n>10: return self.price*0.9
        elif n>=10:return self.price*0.8
    def make_purchase(self,m):
        if m>self.amount: 
            return "didnt have, sorry"
            
        else: 
            self.amount-=m
            return shop.get_price(self,m)*m
    # def __str__(self) -> str:
    #     return f"for 1 kg witrh price {self.price} will be {shop.get_price(self,11)}"
list_for_shop={'apple':203,'banana':90,'orange':50}
d=[[200,15],[300,36],[400,10]]
check=[]
p_for_1=[]
res_price=0
for fruit,j in zip(list_for_shop.items(),d):
    fruit=list(fruit)
    
    
    fruit[0]=shop(fruit[0],j[0],j[1])
    p_for_1.append(fruit[0].get_price(fruit[1]))
    check.append(fruit[0].make_purchase(fruit[1]))
    if type(fruit[0].make_purchase(fruit[1]))==type(10.0):

        res_price+=fruit[0].make_purchase(fruit[1])

    else :continue
for i,j in zip(list_for_shop.keys(),p_for_1):
    

    print(f'for 1kg of {i} - {j}' )
print('\n')
for i,j in zip(list_for_shop.keys(),check):
    if type(j) != str:
        print(f'for {i} --- {j}')
    else: print(f"don't have enough {i}")
print(f"total price {res_price}")    

from ast import Pass


class Password_Manager:
    def __init__(self) -> None:
        self.lis=[]
    def get_password(self):
        if len(self.lis)>0:
            return self.lis[-1]
        else: return 'set password before'    
    def set_password(self,new_password): 
        b=True
        for i in self.lis:
            if new_password==i:
                b=False
        if b:self.lis.append(new_password)
        else: 
            self.lis.remove(new_password)
            self.lis.append(new_password)
    def is_current(self,n):
        if len(self.lis)>0:
            if self.lis[-1]==n: return True
            else: return False
        else: return 'set password before' 
        
user1=Password_Manager()
print(user1.get_password())
user1.set_password('1234')
user1.set_password('qwerty')
user1.set_password('1234')
print(user1.is_current('qwerty'))
print(user1.is_current('1234'))

print(user1.get_password())
print(user1.lis)


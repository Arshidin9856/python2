class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def x_coord(self): return self.x
    def y_coord(self): return self.y
    def __add__(self,point_2):
        return point(self.x_coord+point_2.x_coord,self.y_coord+point_2.y_coord)

x=point(1,1)
y=point(4,4)
c=x+y
print(c.x_coord,c.y_coord)



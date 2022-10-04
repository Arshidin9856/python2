class Time:
    def __init__(self,my_time):
        self.my_time=my_time
    def to_min(self):
        m=self.my_time//60
        s=self.my_time-(m*60)
        return (f'{self.my_time} is {m}:{s}')
    def to_hours(self):
        m=self.my_time//60
        s=self.my_time-(m*60)
        h=0
        if m>=60:
            h=m//60
            m=m-h*60
        return (f'{self.my_time} is {h}:{m}:{s}')

print(Time(230).to_min())
print(Time(10230).to_min())
print(Time(10230).to_hours())


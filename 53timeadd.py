class Time:
    def __init__(self, h, m, s):
        self.__h=h
        self.__m=m
        self.__s=s

    def __add__(self, other):
        total_sec=(self.__h*3600+self.__m*60+self.__s+other.__h*3600+other.__m*60+other.__s)

        h=total_sec//3600
        m=(total_sec%3600)//60
        s=total_sec%60
        
        return Time(h,m,s)

    def display(self):
    	print("Added time:",self.__h,":",self.__m,":",self.__s)

t1=Time(2,45,30)
t2=Time(3,20,40)

t3=t1+t2
t3.display()

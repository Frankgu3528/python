class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def describe(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" mile on it")
    def update_odometer(self,mile):
        if mile>=self.odometer_reading:
            self.odometer_reading=mile
        else:
            print("you can't roll back an odometer")
class electriccar(car):#子类在括号中加入父类名称
    def __init__(self, make, model, year):
        super().__init__(make, model, year)#super函数帮助子类调用父类的方法
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")
my=electriccar("tesla","model s",2016)
my.describe_battery()
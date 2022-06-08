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
my_new_car=car("audi","a4",2016)
print(my_new_car.describe())
my_new_car.update_odometer(234)
my_new_car.read_odometer()
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + 'miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cann't roll back an odoment.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''

    def __init__(self, battery_size=70):
        '''初始化电瓶车的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条电动车的容量信息'''
        print("This car has a " + str(self.battery_size)+'-KWh battery.')

class ElectricCar (Car):
    '''电动车的独到之处'''

    def __init__(self, make, model, year):
        ''' 
        电动汽车的独到之处
        初始化父类的属性，再初始化电动车的特有属性
        '''
        super().__init__(make, model, year)
        self.battery  = Battery()

my_tesla = ElectricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

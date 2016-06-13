class Car(object):
    def __init__(self, price=0, speed=0, fuel=0, mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        info = "Price: {} \n Speed: {}mph \n Fuel: {} \n Mileage: {}mpg \n Tax: {}"
        print info.format(self.price, self.speed, self.fuel, self.mileage, self.tax)


car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(20000000, 35, "Empty", 15)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()

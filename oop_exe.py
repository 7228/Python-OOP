
from pyrsistent import m


class Car():
    num_of_cars = 0

    def __init__(self,manufacturer,model,year,price,gas_in_tank):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        self.gas_in_tank = gas_in_tank

        Car.num_of_cars += 1

    def fuel_left(self,distance_km):
        per_km = 0.062
        self.total = per_km * distance_km
        self.tank = self.gas_in_tank - self.total

        if self.tank > 0:
            return(self.tank)
        else:
            return("Please refill your tank. Car is extremely low on fuel.")
    
    @property
    def display(self):
        return("{} - {} - {}".format(self.manufacturer,self.model,self.year))

    @display.setter
    def display(self,info):
        manufacturer,model,year = info.split("-")
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    @classmethod
    def construct(cls,car_info):
        manufacturer,model,year,price,gas_in_tank = car_info.split("-")
        return(cls(manufacturer,model,year,price,gas_in_tank))   


car_1 = Car("Renault","Scenic 1.9","2005","3000$",5)
print(car_1.fuel_left(16))
print(car_1.tank)
print(car_1.display)

car_1.display = "BMW-320-2002"
print(car_1.display)

car_2_info = "Yugo-45-1980-500$-3"

car_2 = Car.construct(car_2_info)
print(car_2.model)
print(Car.num_of_cars)


class BMW(Car):
    def __init__(self,manufacturer,model,year,price,gas_in_tank,country):
        super().__init__(manufacturer,model,year,price,gas_in_tank)

        self.country = country

    @property
    def display_country(self):
        print("{} {} was manufactured in {}.".format(self.manufacturer,self.model,self.country))

    @display_country.getter
    def display_country(self,name):
        nm = name.split()[0]
        self.country = nm

bmw_1 = BMW("BMW",320,2010,"4000$",10,"Germany")
print(bmw_1.model)
bmw_1.display_country = 'Serbia'
print(bmw_1.display_country)


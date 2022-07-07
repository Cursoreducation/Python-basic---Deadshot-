#1. Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
    #Method: fare. It should calculate the price of the trip. Formula: total_capacity * 100.
    #Example, total_capacity = 50 => fare = 5000

class Vehicle:
     def __init__(self, name, max_speed, total_capacity):
         self.name = name
         self.max_speed = max_speed
         self.total_capacity = total_capacity

     def fare(self):
        return self.total_capacity*100
        # print(f"Your tottal price is {self.total_capacity*100}")

#5. Override fare method for Bus class. Here we need to add an extra 10% to the fare.
    #Formula: total_fare + 10% of total_fare. Example, fare = 50 => total_fare = 5500
     def update_fare(self):
        return self.total_capacity*100 + self.total_capacity*100/10


bugatti_car = Vehicle("bugatti", 3000, 400)
lada_car = Vehicle("lada", 50, 50)

bugatti_car_fare = bugatti_car.fare()
lada_car_fare = lada_car.fare()
bugatti_car_upfare = bugatti_car.update_fare()
lada_car_upfare = lada_car.update_fare()

print(f"Bugatti car fare equals {bugatti_car_fare}., Lada care fare equals {lada_car_fare}")
print(f"New updeted total price for cars are {bugatti_car_upfare} for bugatti and {lada_car_upfare} for lada")
#2. Create classes Bus and Car that inherit Vehicle.
#3. Create 3 car objects and 2 bus objects.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

#6.Add used_capacity attribute for Bus.It means how many people are on the bus.
    # If used_capacity > total_capacity raise an error.

    def check_capacity(self):
        if self.used_capacity <= self.total_capacity:
            return True
        else:
            return "Error"

bus_1 = Bus('Bogdan', 50, 8, 5)
bus_2 = Bus('Etalon', 52, 10, 12)

print(bus_2.check_capacity())

#8.Create class Engine with attribute volume and method get_volume() that will return volume.

#9.Inherit Engine by Car class.
class Engine:
    def __init__(self, volume):
        self.volume = volume

    def get_volume(self):
        print(f"Engine's volume equals {self.volume}")


class Car(Vehicle, Engine):
    def __init__(self, name, max_speed, total_capacity, volume):
        Vehicle.__init__(self, name, max_speed, total_capacity)
        Engine.__init__(self, volume)


car_1 = Car('BMW', 200, 5, 5)
car_2 = Car('Audi', 180, 3, 6)
car_3 = Car('Chery', 190, 7, 9)
car_1.get_volume()
#4. Check:
     #if car_1 is instance of Car.
     #if car_2 is instance of Vehicle.
     #if bus_1 is instance of Car.
     #if bus_1 is instance of Vehicle.
print(isinstance(car_1, Car))
print(isinstance(car_2, Vehicle))
print(isinstance(bus_1, Car))
print(isinstance(bus_1, Vehicle))

#10.Check what is inheritance order of the Car class
print(Car.mro())
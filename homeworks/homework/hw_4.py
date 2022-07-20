# 1. Create a class Vehicle with Attributes: name, max_speed,
#    and total_capacity. Method: fare. It should calculate the price of the trip.
#    Formula: total_capacity * 100. Example, total_capacity = 50 => fare = 5000
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100

# 2. Create classes Bus and Car that inherit Vehicle.


class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity
        if self.used_capacity > self.total_capacity:
            raise Exception("Error")

    def __len__(self):
        return self.name

    def fare(self):
        return self.total_capacity * 110


class Engine:
    def __init__(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume


class Car(Vehicle, Engine):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)


# 3. Create 3 car objects and 2 bus objects

Car_1 = Car("Car_1", 130, 50)
Car_2 = Car("Car_2", 120, 55)
Car_3 = Car("Car_3", 125, 45)

Bus_1 = Bus("Bus_1", 100, 30, 8)
Bus_2 = Bus("Bus_2", 80, 30, 6)


# 4. Check: if car_1 is instance of Car.
#    if car_2 is instance of Vehicle.
#    if bus_1 is instance of Car.
#    if bus_1 is instance of Vehicle.

print(isinstance(Car_1, Car))
print(isinstance(Car_2, Vehicle))
print(isinstance(Bus_1, Car))
print(isinstance(Bus_1, Vehicle))

# 5. Override fare method for Bus class.
#    Here we need to add an extra 10% to the fare.
#    Formula: total_fare + 10% of total_fare. Example, fare = 50 => total_fare = 5500

# 6. Add used_capacity attribute for Bus. It means how many people are on the bus.
#    If used_capacity > total_capacity raise an error.

# 7. Write a magic method to Bus that would be triggered when len() function is called.
print(len(Bus_1.name))

# 8. Create class Engine with attribute volume and method get_volume() that will return volume.
# 9. Inherit Engine by Car class.

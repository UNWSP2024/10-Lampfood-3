#Elliott Morris, 4/9/2026, Car.py

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

def main():
    my_car = Car("Kia Sportage", 2010)

    for i in range(5):
        my_car.accelerate()
        speed = my_car.get_speed()
        print(speed)

    for i in range(5):
        my_car.brake()
        speed = my_car.get_speed()
        print(speed)

if __name__ == '__main__':
    main()

#1
class Elevator:
    def __init__(self,bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current = bottom_floor
    def go_to_floor(self, target_floor):
        while self.current < target_floor:
            self.floor_up()
        while self.current > target_floor:
            self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"Current floor is : {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"Current floor is : {self.current}")

h = Elevator(0,10)
h.go_to_floor(5)

#2
class Building():
    def __init__ (self, bottom_floors, top_floors, elevator_amount):
        self.bot = bottom_floors
        self.top = top_floors
        self.amount = elevator_amount
        self.elevator = []
        for i in range(elevator_amount):
            ele = Elevator(self.bot, self.top)
            self.elevator.append(ele)
            print(self.elevator)
            

    def run_elevator(self, elevator_number, destination_floor):
        self.elevator[elevator_number].go_to_floor(destination_floor)


    #3
    def fire_alarm(self):
        print("FIRE IS ONNNN")
        for i in self.elevator:
            i.go_to_floor(self.bot)
        print(f"All eles are at the bottom floor.")


home = Building(0,10,9)
home.run_elevator(0,7)
home.run_elevator(1,9)
home.fire_alarm()




#4
from random import randint
class RaceCar:
    def __init__(self,registration_number, max_speed2):
        self.registration_number = registration_number
        self.travelled_distance = 0
        self.current_speed = 0
        self.max_speed2 = max_speed2
    def accel(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed2:
            self.current_speed = self.max_speed2
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.distance = km
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            speed_change = randint(-10, 15)
            car.accel(speed_change)
            car.drive(1)


    def print_status(self):
        print(f"{'Regis num': <15} | {'Max speed' :<10} | {'Distance travelled': <12}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.registration_number:<15} | {car.max_speed2:<10} | {car.travelled_distance:<12}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
    

#main program
car_list = []
for i in range(1, 11):
    new_car = RaceCar(f'Car-{i}', randint(150, 200))
    car_list.append(new_car)
race_host = Race("Grand Demolition Derby", 8000, car_list)
hour = 0
while not race_host.race_finished():
    race_host.hour_passes()
    hour += 1

    if hour % 10 == 0:
        race_host.print_status()

race_host.print_status()















    

        
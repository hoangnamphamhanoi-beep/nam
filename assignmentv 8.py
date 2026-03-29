import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current = bottom_floor

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is at floor: {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is at floor: {self.current}")

    def go_to_floor(self, target_floor):
        # Validation to ensure target floor is within building range
        if target_floor > self.top or target_floor < self.bottom:
            print(f"Error: Floor {target_floor} is out of range.")
            return

        print(f"Moving to floor {target_floor}...")
        while self.current < target_floor:
            self.floor_up()
        while self.current > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom = bottom_floor
        self.top = top_floor
        self.elevators = []
        # Initialize the list of elevators
        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_index, destination_floor):
        if 0 <= elevator_index < len(self.elevators):
            print(f"\n--- Operating Elevator #{elevator_index} ---")
            self.elevators[elevator_index].go_to_floor(destination_floor)
        else:
            print(f"Error: Elevator index {elevator_index} is invalid.")

    def fire_alarm(self):
        print("\n!!! FIRE ALARM ACTIVATED !!! Returning all elevators to bottom floor.")
        for i, ele in enumerate(self.elevators):
            print(f"Elevator #{i}:")
            ele.go_to_floor(self.bottom)
        print("All elevators have reached the bottom floor safely.")


class RaceCar:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accel(self, change):
        # Keeps speed between 0 and max_speed using min/max
        self.current_speed = max(0, min(self.current_speed + change, self.max_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accel(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\nRace Status: {self.name}")
        print(f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Distance':<10}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:<12} | {car.max_speed:<10} | {car.travelled_distance:<10.1f} km")

    def race_finished(self):
        # Returns True if any car reaches or exceeds the total distance
        return any(car.travelled_distance >= self.distance for car in self.cars)


# --- MAIN PROGRAM ---

h_building = Building(0, 10, 3)
h_building.run_elevator(0, 7)
h_building.run_elevator(1, 9)
h_building.fire_alarm()

print("\n" + "=" * 15 + " STARTING GRAND DEMOLITION DERBY " + "=" * 15)
car_list = [RaceCar(f"Car-{i + 1}", random.randint(150, 200)) for i in range(10)]
derby_race = Race("Grand Demolition Derby", 8000, car_list)

hours_elapsed = 0
while not derby_race.race_finished():
    derby_race.hour_passes()
    hours_elapsed += 1



    if hours_elapsed % 10 == 0:
        print(f"\n--- Update: Hour {hours_elapsed} ---")
        derby_race.print_status()

# Final result
print(f"\n*** RACE FINISHED AFTER {hours_elapsed} HOURS ***")
derby_race.print_status()



def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


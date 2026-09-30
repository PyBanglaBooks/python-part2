class Engine:
    def __init__(self, cc):
        self.cc = cc
        self.running = False

    def start(self):
        self.running = True
        print(f"Engine ({self.cc} cc) started")

    def stop(self):
        self.running = False
        print("Engine stopped")


class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(cc)

    def drive(self):
        if not self.engine.running:
            self.engine.start()
        print(f"Driving {self.name}")

    def park(self):
        self.engine.stop()
        print(f"{self.name} is parked")


my_car = Car("Axio", 1500)
my_car.drive()
my_car.drive()
my_car.park()

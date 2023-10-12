class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

# Create two Car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

car1.start()
print(car1.is_running)  # Output: True
print(car2.is_running)  # Output: False

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, updated_owner):
        self.owner = updated_owner


vehicle1 = Vehicle(2004, "Toyota Rav4", "Arthur Victory")
vehicle1.update_owner("Rita Victory")
print(f"The new owner of {vehicle1.type} now belongs to {vehicle1.owner}")

vehicle2 = Vehicle(2023, "GMC Acadia", "Rita Victory")
vehicle2.update_owner("Andrew Victory")
print(f"The owner of {vehicle2.type} now belongs to {vehicle2.owner}")
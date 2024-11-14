#objects, a bundle of related attributes.
# class, blueprint used to design the structure and layout of an object.

from car import Car


car1 = Car('mustang',2024,'red',False)
car2 = Car('corvette',2025,'blue',True)
car3 = Car('charger',2026,'yellow',True)


car1.drive()
car2.stop()
car1.describe()
car2.describe()
car3.describe()




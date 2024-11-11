name = input("enter your name: ")
print(name ,"welcome to learning oop")


#oop is an approach for  modeling things in the real world.
#classes,used to create objects by instantiation,ie to create an object from that class.
# self is the instance on which the method is called.
#classes allows the creation of user defined data structures. 

class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog:  #capitalizewords notation
    def __init__(self,name,age):
        self.name = name    #creates an attribute called name and assigns the value of the name parameter to it.
        self.age  = age


tommy = Dog('Tommy',4)
pivy = Dog('Pivy',9)

tommy.age  #to access the instances created.
pivy.name
print(pivy.name)
print(tommy.age)


class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'the {self.color} car has {self.mileage: ,} miles.'
        

blue_car =Car(color='blue',mileage = 20000)
red_car = Car(color='red',mileage = 30000)   

for car in (blue_car,red_car):
    print(car)

def __init__(self,max):
    self.max-size = max
    self.innerlist=[]

def push(self,obj):
    self.innerlist.append(obj)
    if len(self.innerlist) > self.max_size:
        self.innerlist.pop(0)

def get_list(self):
    return self.innerlist




        


    




    


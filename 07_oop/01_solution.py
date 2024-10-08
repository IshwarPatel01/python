#oop is like bank and filing gererlised form..

# syntax 

#init ko construcor kaha jata hai 
class Car:
    total_car = 0
    def __init__(self,brand, model ):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1
    def get_brand(self):
        return self.__brand + " !"
    
    def fullname(self ):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
    


# class bana li hai ab object banayege

#standrised syntax hai py mei obj ke liye

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# # print(my_tesla.__brand)
# print(my_tesla.fuel_type())
# # print(my_tesla.model)
# # print(my_tesla.fullname())

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
# # print(safari.total_car)

# print(Car.total_car)

# my_Car =  Car("Toyota", "Corolla")
# # my_Car.model = "City"
# print(my_Car.model)
# # print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.fullname())

# print(my_Car.general_description())
# print()
# # kai jaga aap () lagate the kai jaga nae toh yeh class defination hain jisne bhi code likha hain

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.__brand)
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("tesla", "model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
















# remeber this attention to deailts about (specification)

# encapsulation concept ye hai ki uske andr kya hai ye mere chahne pe hii aapko pata lage , me chahu toh aapko pata lage , na chahu toh na lage 



#python kaafi jyada structured language hain

# learn setter by yourself


# polymorphism aise bhi karaya jata hai ki input value kya de rahe ho  eg + ke adr number de rahe toh calculate kar deta hai par string dete hai toh dono ko add kar deta hain



# @staticmethod hai decorators , yeh aapko method ki functionality ko enchance kar deta hain aur boht saari cheejhe hai jo aap kar pate ho decorators ki wajah se , decorator boht jaga use aata hain 
# multiple inheritance 





# # animal inheritance

# class Animal:
#     def __init__(self,type,nature):
#         self.type = type
#         self.nature = nature


#     def pet(self):
#         if self.nature == "friendly":
#             print("can be pet")

#         else:
#             print("Agar dikh jaye to Jaldi waha se hato!!!")



# class Dog(Animal):
#     def __init__(self,type , nature, sound):
#         super().__init__(type,nature)
#         self.sound = sound
#         print(f"dog sounds {self.sound}")
       


# class Lion(Animal):
#     def __init__(self, type, nature, sound):
#         super().__init__(type, nature)
#         self.sound = sound

#         print(f"lion sounds {self.sound}")


# dogeshwar = Dog("Domestic", "friendly", "woo woo")
# print("type :" ,dogeshwar.type)
# print("nature :" ,dogeshwar.nature)

# dogeshwar.pet()


# sheru = Lion("Wild","khunkhaar","dharrraaatttaa")
# print("type :" ,sheru.type)
# print("nature :" ,sheru.nature)
# sheru.pet()




# # car inheritance structure

# class Car:
#     def __init__(self,brand,model):
#         self._brand = brand
#         self.model = model
    
#     def get_brand(self):
#         return self._brand

#     def full_name(self):
#         return f"{self._brand} {self.model}"



# class ElectricCar (Car):
#     def __init__(self ,brand ,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size



# class HybridCar(Car):
#     def __init__(self,brand,model,hybrid_comb):
#         super().__init__(brand , model)
#         self.hybrid_comb = hybrid_comb



# E_car = ElectricCar("Tesla","MOdel X", "85kWh")
# print("Electric Car Specifications below :")
# print(E_car._brand)
# print(E_car.full_name())
# print("Battery Size" ,E_car.battery_size)


# H_car = HybridCar("Toyota" ,"Hyryder" ,"Full Hybrid (HEV)")
# print("\nHybrid car specifications below :")
# print(H_car.full_name())
# print("Hybrid Type" ,H_car.hybrid_comb)


# # basic bank transacton sysytem

# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
    
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount , "was debited from your Account ",self.acc_no,"xxxxx")
#         print(f"Total balance: {self.balance}")

#     def credit(self,money):
#         self.balance += money
#         print("Rs.",money , "was credited to your Acount ",self.acc_no,"xxxxx")
#         print(f"total balance : {self.balance}")


#     def tot_balance(self):
#         return self.balance


# acc1 = Account(5000,7899)
# print("Initial Balance is", acc1.balance)
# acc1.debit(2000)
# acc1.credit(50000)


# # use of @staticmethod 

# class Math:
    
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# mth = Math()
# print(mth.add(6,7))


# # use of @property decorator

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5)
# print(c.area)

# # use of @classmethod.

# class Book:
#     def __init__(self,title):
#         self.title = title

#     @classmethod
#     def chg_var(cls,chg_ttl):
#         return cls(chg_ttl)

# b = Book("Learn Python")
# print(b.title)

# b1 = Book.chg_var("Pyhton basics")
# print(b1.title)


# # accessing protected attributes (_)

# class Car:
#     def __init__(self):
#         self._engine = "V8"  # protected attribute

# class SportsCar(Car):
#     def show_engine(self):
#         print("Engine:", self._engine)  # allowed

# c = Car()  # allowed, but discouraged
# print(c._engine)

# c1 = SportsCar()
# c1.show_engine()  # allowed and encouraged



# # accessing private attributes(__)

# class Parent:
#     def __init__(self):
#         self._protected = "I am protected"
#         self.__private = "I am private"


#     def get_pvt(self):
#         print(self.__private)


# class Child(Parent):
#     def access_members(self):
        
#         print(self._protected)       # Allowed

#         print(self.__private)      #  Fails 


# child = Child()
# child.get_pvt() #  using (get) method inside base class  
# child.access_members()



# # operator overloading

# class Vector:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b, self.c + other.c)
    
#     def __str__(self):
#         return f"{self.a}a + {self.b}b + {self.c}c"
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# print(v1 + v2) 
# print(v1.b)
# print(v2.c)



# Polymorphism

class SchoolStudent:
    def __init__(self, Name, grade , stream):
        self.Name = Name
        self.grade = grade
        self.stream = stream

    def details(self):
        print(f"Student Name: {self.Name}, Grade: {self.grade}, Stream: {self.stream}")



class CollegeStudent(SchoolStudent):
    def __init__(self, Name, grade, stream, major):
        super().__init__(Name, grade, stream)
        self.major = major

    def details(self):
        print(f"Student Name: {self.Name}, Grade: {self.grade}, Stream: {self.stream}, Major: {self.major}")


s1 = SchoolStudent("Subham","11","PCM")
s1.details()


s2 = CollegeStudent("Subham","3","CSE","B.Tech")
s2.details()
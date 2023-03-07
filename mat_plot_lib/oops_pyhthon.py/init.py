class Laptop:
    def __init__(self,fname,lname,salary,city):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.city= city

    def details(self):
        print("details about employess")
        print("Name :",self.fname)
        print("surname :", self.lname)
        print("salary :",self.salary)












laptop1 = Laptop("Abhi","bhingole","44k","latur")
print(laptop1.fname)
print(laptop1.lname)

laptop1.details()
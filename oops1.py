class employee:
    #special methos\magic method-constructor
    def __init__(self):
        self.id =123
        self.salary= 50000
        self.designation = "SDE"


    def travel(self, destination):
        print(f"employee is traveling to {destination}")

#create an object/instance of the class
sam = employee()
print(sam.salary)
sam.travel("kerala") 
print(type(sam))       
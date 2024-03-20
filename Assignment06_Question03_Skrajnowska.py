class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def calculateSalary(self):
        self.salary = 10000
        
class HourlyEmployee(Employee):
    def __init__(self, name, position, rate):
        super().__init__(name, position)
        self.rate = rate
    def calculatePay(self,hours):
        return self.rate * hours

class SaleriedEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary = salary
    def calculatePay(self, years):
        return self.salary * years
 
class CommisionedEmployee(Employee):
    def __init__(self, name, position, percent):
        super().__init__(name, position)    
        self.percent = percent
    def calculatePay(self, amountSold):
        return self.percent / 100 * amountSold
    
def main():
    employees = [SaleriedEmployee("Bob","CEO",100000),HourlyEmployee("Steve", "Manager", 50), CommisionedEmployee("Joe", "Cashier", 5)]
    pay = [employees[0].calculatePay(2), employees[1].calculatePay(150), employees[2].calculatePay(150000)]
    
    print("Employee\tPosition\tPay")
    for i in range(len(employees)):
        print(employees[i].name,"\t\t",employees[i].position,"\t\t",pay[i])

main()
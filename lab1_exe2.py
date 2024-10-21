import json 

class Calculation: 
    def __init__(self): 
        self.history = {"History": []}
        self.file = open("history.json", "w") 

    def add(self):
        num_list = self.get_input_numbers()
        result = sum(num_list)
        self.store_result("add", num_list, result)
        print(f"Result: {result}")

    def sub(self):
        num_list = self.get_input_numbers()
        result = num_list[0] - sum(num_list[1:])
        self.store_result("sub", num_list, result)
        print(f"Result: {result}")
    
    def mul(self):      
        num_list = self.get_input_numbers()
        result = 1
        for num in num_list:
            result *= num
        self.store_result("mul", num_list, result)
        print(f"Result: {result}")

    def div(self):
        num_list = self.get_input_numbers()
        result = num_list[0]
        for num in num_list[1:]:
            if num == 0:
                print("Division by zero is not allowed.")
                return
            result /= num
        self.store_result("div", num_list, result)
        print(f"Result: {result}")
        

    def get_input_numbers(self):

        num_list = []
        count = int(input("How many numbers do you want to input? "))
        for _ in range(count):
            num = float(input("Enter a number: "))
            num_list.append(num)
        return num_list
    
    def store_result(self, operation, operands, result):

        operation_data = {
            "operation": operation,
            "operands": operands,
            "result": result
        }
        self.history["History"].append(operation_data)
        json.dump(self.history, self.file, indent=4)
        self.file.flush()

if __name__ == '__main__':
    print("Welcome to the calculator")
    calc = Calculation()
    condition = True
    while condition:
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            calc.add()
        elif choice == 2:
            calc.sub()
        elif choice == 3:
            calc.mul()
        elif choice == 4:
            calc.div()
        elif choice == 5:
            condition = False
        else:
            print("Invalid choice. Please try again.")
    


import json

class Calculation: 
    def __init__(self):
        self.history = {"History": []}
        self.file = open("output.json", "w")
        
    def add(self, op1, op2): 
        result = op1 + op2
        operation = f"add {op1} {op2}"
        self.history["History"].append({"operation": operation, "result": result})
        json.dump(self.history, self.file, indent=4)  # Make JSON readable with indent
        self.file.flush()  # Ensure the data is written immediately
        return result

    def sub(self, op1, op2): 
        result = op1 - op2
        operation = f"sub {op1} {op2}"
        self.history["History"].append({"operation": operation, "result": result})
        json.dump(self.history, self.file, indent=4)
        self.file.flush()
        return result
    
    def mul(self, op1, op2): 
        result = op1 * op2
        operation = f"mul {op1} {op2}"
        self.history["History"].append({"operation": operation, "result": result})
        json.dump(self.history, self.file, indent=4)
        self.file.flush()
        return result 
    
    def div(self, op1, op2): 
        if op2 == 0:  # Handle division by zero
            return "Division by zero is not allowed."
        result = op1 / op2
        operation = f"div {op1} {op2}"
        self.history["History"].append({"operation": operation, "result": result})
        json.dump(self.history, self.file, indent=4)
        self.file.flush()
        return result 

if __name__ == '__main__':
    print("Welcome to the calculator")
    calc = Calculation()  # Initialize the calculation object once
    condition = True 
    while condition: 
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to exit")
        choice = int(input("Enter your choice: "))

        if choice == 1: 
            op1 = float(input("Enter first number: "))
            op2 = float(input("Enter second number: "))
            print("Result:", calc.add(op1, op2))
        elif choice == 2: 
            op1 = float(input("Enter first number: "))
            op2 = float(input("Enter second number: "))
            print("Result:", calc.sub(op1, op2))
        elif choice == 3: 
            op1 = float(input("Enter first number: "))
            op2 = float(input("Enter second number: "))
            print("Result:", calc.mul(op1, op2))
        elif choice == 4: 
            op1 = float(input("Enter first number: "))
            op2 = float(input("Enter second number: "))
            print("Result:", calc.div(op1, op2))
        elif choice == 5: 
            condition = False 
        else: 
            print("Invalid choice")

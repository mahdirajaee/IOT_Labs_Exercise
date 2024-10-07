class calculation: 
    def __init__(self):
        self.history ={"History": []}
        self.f = open("output.json", "w")
        pass 

    def add(self, op1, op2): 
        result = int(input("Enter first number: ")) + int(input("Enter second number: "))
        self.history["History"].append({"result": result, "operation": "add"})
        json.dump(self.f, self.history)
        return result

    def sub(self, op1, op2): 
        result = int(input("Enter first number: ")) - int(input("Enter second number: "))
        with open("output.json", "w") as f: 
            f.write(str(result))
        return result
    
    def mul(self, op1, op2): 
        result = int(input("Enter first number: ")) * int(input("Enter second number: "))
        with open("output.json", "w") as f: 
            f.write(str(result))
        return result 
    
    def div(self, op1, op2): 
        result = int(input("Enter first number: ")) / int(input("Enter second number: "))
        with open("output.json", "w") as f: 
            f.write(str(result))
        return result 
 
if __name__ == '__main__':
    print("welcome to the calculator")
    condition = True 
    while condition: 
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to exit")
        choice = int(input("Enter your choice: "))
        calc = calculation()
        if choice == 1: 
            print(calc.add(1, 2))
        elif choice == 2: 
            print(calc.sub(1, 2))
        elif choice == 3: 
            print(calc.mul(1, 2))
        elif choice == 4: 
            print(calc.div(1, 2))
        elif choice == 5: 
            condition = False 
        else: 
            print("Invalid choice")
    


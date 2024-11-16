import requests

def get_operation():
    """Prompt user for the type of operation."""
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter the number corresponding to the operation: ")
    operations = {
        "1": "add",
        "2": "subtract",
        "3": "multiply",
        "4": "divide"
    }
    return operations.get(choice, None)

def get_operands():
    """Prompt user for two numerical operands."""
    try:
        op1 = float(input("Enter the first operand: "))
        op2 = float(input("Enter the second operand: "))
        return op1, op2
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return None, None

def make_request(operation, op1, op2):
    """Send a GET request to the CherryPy server."""
    url = f"http://localhost:8080/{operation}?op1={op1}&op2={op2}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the server: {e}")
        return None

if __name__ == '__main__':
    operation = get_operation()
    if not operation:
        print("Invalid operation selected.")
    else:
        op1, op2 = get_operands()
        if op1 is not None and op2 is not None:
            result = make_request(operation, op1, op2)
            if result:
                if 'error' in result:
                    print(result['error'])
                else:
                    print(f"Operation: {result['operation']}")
                    print(f"{result['op1']} {operation} {result['op2']} = {result['result']}")
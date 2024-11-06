import requests

BASE_URL = 'https://catalog-p4iot.onrender.com'

def fetch_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()       
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError:
        print("Received non-JSON response")
        return response.text

def main():
    print("Available commands:")
    print("all:     Return all the JSON")
    print("devices: Return all the devices")
    print("houses:  Return all the houses")
    print("users:   Return all the users")
    print("quit:    Exit")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "all":
            data = fetch_data('/all')
        elif command == "devices":
            data = fetch_data('/devices')
        elif command == "houses":
            data = fetch_data('/houses')
        elif command == "users":
            data = fetch_data('/users')
        elif command == "quit":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")
            continue

        if data:
            print("\nResponse:")
            print(data)

if __name__ == "__main__":
    main()

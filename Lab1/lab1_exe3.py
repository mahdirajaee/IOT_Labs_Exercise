import json
class Devices: 
    def __init__(self):
        self.devcies = {}

    #this will add the device to the dictionary
    def add_device(self, device_name, device_type):
        self.devices[device_name] = device_type
        print(f"Device {device_name} added successfully.")


    #this will search for the device by its name
    def searchByName(self, device_name):
        if device_name in self.devices:
            print(f"Device {device_name} found: {self.devices[device_name]}")
        else:
            print(f"Device {device_name} not found.")


    #this  will search for the device by its id
    def searchById(self, device_id):
        if device_id in self.devices.values():
            print(f"Device with id {device_id} found.")
        else:
            print(f"Device with id {device_id} not found.")

    def searchByService(self, service):
        devices = [device for device, device_service in self.devices.items() if device_service == service]
        if devices:
            print(f"Devices with service {service} found: {devices}")
        else:
            print(f"No devices found with service {service}.")
    
    def searchByMeasureType(self, measure_type):
        filecontent = open("catalog.json", "r").read()
        catalog = json.loads(filecontent)
        devices = [device for device, device_measure in self.devices.items() if device_measure == measure_type]
        if devices:
            print(f"Devices with measure type {measure_type} found: {devices}")
        else:
            print(f"No devices found with measure type {measure_type}.")

    def insertDevice(self, device_name, device_type):
        self.devices[device_name] = device_type
        print(f"Device {device_name} inserted successfully.")

    def printAll(self):
        print("Devices:")
        for device, device_type in self.devices.items():
            print(f"{device}: {device_type}")

    def exit(self):
        print("Exiting...")
        exit()

if __name__ == '__main__': 
    devices = Devices()
    while True:
        print("1. Add Device")
        print("2. Search by Name")
        print("3. Search by Id")
        print("4. Search by Service")
        print("5. Search by Measure Type")
        print("6. Insert Device")
        print("7. Print All Devices")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            device_name = input("Enter the device name: ")
            device_type = input("Enter the device type: ")
            devices.add_device(device_name, device_type)
        elif choice == '2':
            device_name = input("Enter the device name: ")
            devices.searchByName(device_name)
        elif choice == '3':
            device_id = input("Enter the device id: ")
            devices.searchById(device_id)
        elif choice == '4':
            service = input("Enter the service: ")
            devices.searchByService(service)
        elif choice == '5':
            measure_type = input("Enter the measure type: ")
            devices.searchByMeasureType(measure_type)
        elif choice == '6':
            device_name = input("Enter the device name: ")
            device_type = input("Enter the device type: ")
            devices.insertDevice(device_name, device_type)
        elif choice == '7':
            devices.printAll()
        elif choice == '8':
            devices.exit()
        else:
            print("Invalid choice. Please try again.")
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
    
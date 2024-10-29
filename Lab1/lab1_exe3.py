class Devices: 
    def __init__(self):
        self.devcies = {}


    def add_device(self, device_name, device_type):
        self.devices[device_name] = device_type
        print(f"Device {device_name} added successfully.")

    def searchByName(self, device_name):
        if device_name in self.devices:
            print(f"Device {device_name} found: {self.devices[device_name]}")
        else:
            print(f"Device {device_name} not found.")

    def searchById(self, device_id):
        if device_id in self.devices.values():
            print(f"Device with id {device_id} found.")
        else:
            print(f"Device with id {device_id} not found.")
            
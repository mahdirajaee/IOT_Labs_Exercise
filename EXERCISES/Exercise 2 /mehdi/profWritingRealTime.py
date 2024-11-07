import json 
import requests 

class CatalogeManagerConsumer: 
    def __init__(self): 
        self.url = 'https://catalog-p4iot.onrender.com'

    def all(self): 
        pass 

    def devcies(self): 
        pass

    def houses(self): 
        pass

    def users(self):
        pass 

    def quit(self): 
        pass 

    def menu(self): 
        string_to_print = "Available commands:\nall:     Return all the JSON\ndevices: Return all the devices\nhouses:  Return all the houses\nusers:   Return all the users\nquit:    Exit"
        while True: 
            print(string_to_print)
            user_input = input('select a command: ').strip().lower()
            if user_input == 'all': 
                self.all()
            elif user_input == 'devices':
                self.devices()

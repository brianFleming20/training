'''
Fake interface class creates an object then retreves that object attributes
'''

interface_data = []

class interface():

    def extend_interface(self):
        return interface_data


    def _interface(self,attribute):
        interface_data.clear()
        interface_data.extend(attribute)
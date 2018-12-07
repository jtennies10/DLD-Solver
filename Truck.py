"""Represents a Truck used by WGUPS 
    Each truck has a maximum package capacity of 16
    and an average speed of 18 miles per hour
    packages_on_board represents the packages on the truck"""
class Truck:
    PACKAGE_CAPACITY = 16
    TRUCK_SPEED = 18
    NUM_TRUCKS = 3
    NUM_DRIVERS = 2
    miles_driven = 0

    def __init__(self):
        self.package_ids_on_board = list()
    
    def add_package(self, package_id):
        if(len(self.package_ids_on_board) < 16):
            self.package_ids_on_board.append(package_id)

    def remove_package(self, package):
        self.package_ids_on_board.remove(package)

    def __str__(self):
        package_ids_as_str = ''
        for package_id in self.package_ids_on_board:
            package_ids_as_str += (str(package_id) + ' ')
        
        return package_ids_as_str

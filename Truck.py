"""Represents a Truck used by WGUPS 
    Each truck has a maximum package capacity of 16
    and an average speed of 18 miles per hour
    packages_on_board represents the packages on the truck"""
class Truck:
    PACKAGE_CAPACITY = 16
    TRUCK_SPEED = 18
    miles_driven = 0

    def __init__(self):
        self.packages_on_board = list()
    
    def add_package(self, package):
        if(len(self.packages_on_board) < 16):
            self.packages_on_board.append(package)

    def remove_package(self, package):
        self.packages_on_board.remove(package)

    def __str__(self):
        packages_as_str = ''
        for package in self.packages_on_board:
            packages_as_str += (str(package) + '\n')
        
        return packages_as_str
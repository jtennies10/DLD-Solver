"""Represents a Truck used by WGUPS 
    Each truck has a maximum package capacity of 16
    and an average speed of 18 miles per hour
    packages_on_board represents the packages on the truck"""
class Truck:
    PACKAGE_CAPACITY = 16
    TRUCK_SPEED = 18

    def __init__(self):
        self.packages_on_board = list()
    
    def add_package(self, package):
        if(len(self.packages_on_board) < 16):
            self.packages_on_board.append(package)

    def remove_package(self, package):
        self.packages_on_board.remove(package)

    #TODO: add __str__
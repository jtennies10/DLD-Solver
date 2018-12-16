""" Joshua Tennies Student ID:#000885921"""

"""Represents a Truck used by WGUPS 
    Each truck has a maximum package capacity of 16
    and an average speed of 18 miles per hour
    packages_on_board represents the packages on the truck"""
class Truck:
    PACKAGE_CAPACITY = 16
    TRUCK_SPEED_MPH = 18
    NUM_TRUCKS = 3
    NUM_DRIVERS = 2
    miles_driven = 0

    """Truck constructor with no parameters"""
    def __init__(self):
        self.package_ids_on_board = list()

    """
    Returns the list of package ids the Truck is 
    carrying
    """
    def get_package_ids_on_board(self):
        return self.package_ids_on_board
    
    """
    Attempts to add a package id to the Truck, returning 
    True if successful and False if not
    """
    def add_package_id(self, package_id):
        if(len(self.package_ids_on_board) < self.PACKAGE_CAPACITY):
            self.package_ids_on_board.append(package_id)
            return True

        return False

    """
    Removes a given package id from the Truck
    """
    def remove_package_id(self, package_id):
        self.package_ids_on_board.remove(package_id)


    """
    Defines the special function __str__ which 
    returns a formatted string containing the attributes of
    a Truck object
    """
    def __str__(self):
        package_ids_as_str = ''
        for package_id in self.package_ids_on_board:
            package_ids_as_str += (str(package_id) + ' ')
        
        return package_ids_as_str

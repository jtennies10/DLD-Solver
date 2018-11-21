


"""Represents a Truck used by WGUPS 
    Each truck has a maximum package capacity of 16
    and an average speed of 18 miles per hour"""
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



"""Represents a Delivery object
    Every delivery object has unique properties"""
class Delivery:
    def __init__(self, package_id, address, city, state, zip,
    delivery_deadline, weight_in_kilograms, special_notes,
    delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight_in_kilograms = weight_in_kilograms
        self.special_notes = special_notes
        self.delivery_status = delivery_status
    
    def update_delivery_status(self, new_status):
        self.delivery_status = new_status
        




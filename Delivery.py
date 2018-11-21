"""Represents a Delivery object
    Every delivery object has unique properties
    """
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

    #TODO: add __str__
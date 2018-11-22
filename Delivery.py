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

    def __str__(self):
        delivery_as_str = ''
        delivery_as_str += (str(self.package_id) + ' ')
        delivery_as_str += (self.city + ', ')
        delivery_as_str += (self.state + ' ')
        delivery_as_str += (self.zip + ' ')
        delivery_as_str += ('Deadline:' 
        + self.delivery_deadline + ' ')
        delivery_as_str += (str(self.weight_in_kilograms) + 'kg ')
        delivery_as_str += ('Notes:' + self.special_notes + ' ')
        delivery_as_str += ('Status:' + self.delivery_status)

        return delivery_as_str

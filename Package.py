"""Represents a Delivery object
    Every delivery object has unique properties
    """
class Package:
    def __init__(self, package_id, address, city, state, zip,
    package_deadline, weight_in_kilograms, 
    special_notes, package_status, distance_list_id):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.package_deadline = package_deadline
        self.weight_in_kilograms = weight_in_kilograms
        self.special_notes = special_notes
        self.package_status = package_status
        self.distance_list_id = distance_list_id
    
    def set_distance_list_id(self, distance_id):
        self.distance_list_id = distance_id


    def update_delivery_status(self, new_status):
        self.package_status = new_status

    def __str__(self):
        package_as_str = ''
        package_as_str += ('Package id: ' + str(self.package_id) + ' ')
        package_as_str += ('Distance list id: ' + str(self.distance_list_id) + ' ')
        package_as_str += (self.address + ' ')
        package_as_str += (self.city + ', ')
        package_as_str += (self.state + ' ')
        package_as_str += (self.zip + ' ')
        package_as_str += ('Deadline:' + self.package_deadline + ' ')
        package_as_str += (str(self.weight_in_kilograms) + 'kg ')
        package_as_str += ('Notes:' + self.special_notes + ' ')
        package_as_str += ('Status:' + self.package_status + ' ')

        return package_as_str

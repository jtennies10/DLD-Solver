"""
Defines the Package class,
which is used to structure the information for 
any given package that needs delivered
"""
class Package:
    """Constructor for a Package object"""
    def __init__(self, package_id, address, city, state, zip,
    package_deadline, weight_in_kilograms, 
    special_notes, distance_list_id):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.package_deadline = package_deadline
        self.weight_in_kilograms = weight_in_kilograms
        self.special_notes = special_notes
        self.distance_list_id = distance_list_id
        self.delivered_hours = 24
        self.delivered_minutes = 60
    
    """Returns the package id"""
    def get_package_id(self):
        return self.package_id

    """Returns the package's corresponding distance list id"""
    def get_distance_list_id(self):
        return self.distance_list_id

    """Sets the package's distance list id"""
    def set_distance_list_id(self, distance_id):
        self.distance_list_id = distance_id

    """
    Checks to see if the package has a delivery deadline
    Returning True if so and False if not
    """
    def has_deadline(self):
        if 'EOD' not in self.package_deadline:
            return True
        
        return False

    """Sets the time a package is set to be delivered"""
    def set_delivered_time(self, hours, minutes):
        self.delivered_hours = hours
        self.delivered_minutes = minutes

    """
    Defines the special function __str__ which 
    returns a formatted string containing the attributes of
    a Package object
    """
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
        

        return package_as_str

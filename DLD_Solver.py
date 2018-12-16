""" Joshua Tennies Student ID:#000885921"""

"""
The main controller for the program, instantiates objects,
gathers user input, and controls the flow of the program
"""

from Truck import *
import ExcelReader
import RouteCalculator

"""
Checks to see if a passed in hour is valid
@return True if valid, False if not
"""
def is_hours_valid(hours):
    if hours >= 8 and hours <= 23:
        return True

    return False

"""
Checks to see if a passed in minute is valid
@return True if valid, False if not
"""
def is_minutes_valid(minutes):
    if minutes >= 0 and minutes <= 59:
        return True

    return False



#read in distance matrix data into a two dimensional list
distance_matrix = ExcelReader.read_in_distances()

#read in package data and store in table  
packages_table = ExcelReader.read_in_packages(distance_matrix)   

#initialize the trucks used to deliver 
#the packages
trucks_in_optimal_route = list()
for i in range(0,Truck.NUM_TRUCKS):
    trucks_in_optimal_route.append(Truck())

#calculate the full route
totalMiles = RouteCalculator.calculate_near_optimal_route(
    trucks_in_optimal_route, distance_matrix, packages_table)

#create hours and minutes variables that store user inputted
#hours and minutes
hours = 0
minutes = 0

#prompt user for hours and minutes to see package statuses
#based on the entered times, quit if -1 entered for hours
while True:
    print('Enter hours and minutes below to see each package\'s status at that time')
    hours = int(input('Hours(24hr format, -1 to quit):'))
    if hours == -1:
        break
    if not is_hours_valid(hours):
        print('Invalid hours. Please enter hour between 8 and 23')
        continue
    minutes = int(input('Minutes:'))
    if not is_minutes_valid(minutes):
        print('Invalid minutes. Please enter minutes between 0 and 59')
        continue


    #call packages_at_time using current hours and minutes
    RouteCalculator.packages_at_time(packages_table, distance_matrix, trucks_in_optimal_route, hours, minutes)
    







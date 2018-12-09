from Truck import *
from Package import *
from DirectHashTable import *
import ExcelReader
import RouteCalculator


def is_hours_valid(hours):
    if hours >= 8 and hours <= 23:
        return True

    return False

def is_minutes_valid(minutes):
    if minutes >= 0 and minutes <= 59:
        return True

    return False



#read in distance matrix data into a two dimensional list
distance_matrix = ExcelReader.read_in_distances()

#read in package data and store in table  
packages_table = ExcelReader.read_in_packages(distance_matrix)   

#print(packages_table)
#print(len(distance_matrix))


# table_size = packages_table.size()
#initialize the trucks used to deliver 
#the packages
trucks_in_optimal_route = list()
for i in range(0,Truck.NUM_TRUCKS):
    trucks_in_optimal_route.append(Truck())

#calculate the full route
totalMiles = RouteCalculator.calculate_near_optimal_route(
    trucks_in_optimal_route, distance_matrix, packages_table)
for truck in trucks_in_optimal_route:
    print(str(truck) + '\n')
print(str(totalMiles))


hours = 0
minutes = 0

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


    #create function to step through the 
    #route and update package statuses
    print(RouteCalculator.packages_at_time(
        packages_table, distance_matrix, hours, minutes))







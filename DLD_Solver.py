from Truck import *
from Package import *
from DirectHashTable import *
import ExcelReader
import sys

#read in distance matrix data into a two dimensional list
distance_matrix = ExcelReader.read_in_distances()

#read in package data and store in table  
packages_table = ExcelReader.read_in_packages(distance_matrix)   

#print(packages_table)

#instantiate the hours and minutes for the beginning of the day
hour_of_day = 8
minutes_of_hour = 0

table_size = packages_table.size()
minimum_distance = float(sys.maxsize)
optimal_route = list()
optimal_route.append(0) #the first object is always the hub

#first solution, using a greedy algorithm
#that gets an approximate solution in O(n^3)
last_distance_id = 0
inc = 0
while inc < table_size:
    inc += 1
    nextMinMovement = float(sys.maxsize)
    nextMovementId = -1
    for package in packages_table:
        print(package)
        print(str(last_distance_id))
        if package.get_distance_list_id() == -1:
            continue
        if package.get_distance_list_id() >= last_distance_id:
            currentMovement = float(distance_matrix[package.get_distance_list_id()][last_distance_id+2])
            if currentMovement < nextMinMovement and optimal_route.count(package.get_package_id()) < 1:
                print('true')
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()
                print(str(nextMovementId))
        else:
            currentMovement = float(distance_matrix[last_distance_id][package.get_distance_list_id()+2])
            if  currentMovement < nextMinMovement and optimal_route.count(package.get_package_id()) < 1:
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()

    last_distance_id = nextMovementId
    optimal_route.append(nextMovementId)
    minimum_distance += nextMinMovement

print(optimal_route)
print(str(minimum_distance))

        













    





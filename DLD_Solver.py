from Truck import *
from Package import *
from DirectHashTable import *
import ExcelReader
import RouteCalculator


#read in distance matrix data into a two dimensional list
distance_matrix = ExcelReader.read_in_distances()

#read in package data and store in table  
packages_table = ExcelReader.read_in_packages(distance_matrix)   

print(packages_table)
print(len(distance_matrix))

#instantiate the hours and minutes for the beginning of the day
hour_of_day = 8
minutes_of_hour = 0

table_size = packages_table.size()

trucks_in_optimal_route = list()
for i in range(0,Truck.NUM_TRUCKS):
    trucks_in_optimal_route.append(Truck())

totalMiles = RouteCalculator.calculate_near_optimal_route(
    trucks_in_optimal_route, table_size, distance_matrix, packages_table)
for truck in trucks_in_optimal_route:
    print(str(truck) + '\n')
print(str(totalMiles))









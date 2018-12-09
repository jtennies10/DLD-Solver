from Truck import *
from Package import *
from DirectHashTable import *
import ExcelReader
import RouteCalculator


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











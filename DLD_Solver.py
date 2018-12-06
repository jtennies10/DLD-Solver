from Truck import *
from Delivery import *
from DirectHashTable import *
import ExcelReader

#read in distance matrix data into a two dimensional list
distance_matrix = ExcelReader.read_in_distances()

#test distance matrix to see if read in successful
print(distance_matrix)

#read in package data and store in table  
packages_table = ExcelReader.read_in_packages()   

#test package table to see if read in successful
print(packages_table)

#instantiate the hours and minutes for the beginning of the day
hour_of_day = 8
minutes_of_hour = 0

#test Truck and Delivery
t1 = Truck()
t2 = Truck()

d1 = Delivery(1, '17 Foreman st', 
'Eldred', 'PA', '16731', '10:00 am', 30, '', 'waiting')

print(d1)

print(t1)

t2.add_package(d1)

print(t2)











    





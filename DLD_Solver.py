from Truck import *
from Delivery import *
from DirectHashTable import *
import xlrd

"""
Reads in the package data from the excel file.
Excel interaction code adapted from 
https://www.geeksforgeeks.org/reading-excel-file-using-python/
"""

def read_in_packages():
    temp_packages_table = DirectHashTable()

    loc = ("WGUPS Package File.xlsx")

    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    
    for i in range(8, sheet.nrows-1):
        package_id = sheet.cell_value(i, 0)
        address = sheet.cell_value(i, 1)
        city = sheet.cell_value(i, 2)
        state = sheet.cell_value(i, 3)
        zipcode = str(sheet.cell_value(i, 4))
        delivery_deadline = str(sheet.cell_value(i, 5))
       	weight_in_kg = sheet.cell_value(i, 6)
        special_notes = sheet.cell_value(i, 7)
        delivery = Delivery(package_id, address, city, state, zipcode,
                            delivery_deadline, weight_in_kg, 
                            special_notes, 'waiting')
        temp_packages_table.add_element(package_id, delivery)

    return temp_packages_table

#TODO:pip install xlrd
#read in package data and store in table  
packages_table = read_in_packages()   

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











    





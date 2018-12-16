""" Joshua Tennies Student ID:#000885921"""

"""
Reads in the data from the excel files associated with the project using the xlrd module
Excel interaction code adapted from 
https://www.geeksforgeeks.org/reading-excel-file-using-python/
"""

from DirectHashTable import *
from Package import *
import xlrd


"""
Reads in the package data from the WGUPS Package File
Each row in the file creates a Package object which retains
the given row's information
Each package is added to the temp_packages_table

@return a DirectHashTable of all the packages
"""
def read_in_packages(distance_matrix):
    temp_packages_table = DirectHashTable()

    loc = "WGUPS Package File.xlsx"

    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    
    for i in range(8, sheet.nrows):
        package_id = sheet.cell_value(i, 0)
        address = sheet.cell_value(i, 1)
        address = address.replace('South', 'S')
        city = sheet.cell_value(i, 2)
        state = sheet.cell_value(i, 3)
        zipcode = str(sheet.cell_value(i, 4))
        package_deadline = sheet.cell_value(i, 5)
        if package_deadline != 'EOD':
            package_deadline = time_as_str(package_deadline)
        

       	weight_in_kg = sheet.cell_value(i, 6)
        special_notes = sheet.cell_value(i, 7)
        #deal with wrong address by setting the 
        #correct address and adding the time to 
        #special_notes
        if special_notes == 'Wrong address listed':
            address = '410 S State St'
            special_notes = special_notes + ', not corrected until 10:20 AM'



        distance_list_id = -1

        #parse through the distance matrix and find the distance list with
        #an address that matches the address of the current package
        for distance_list in distance_matrix:
            if distance_list[1].find(address) >= 0:
                distance_list_id = distance_matrix.index(distance_list)
                break
        
        
        current_package = Package(package_id, address, city, state, zipcode,
                            package_deadline, weight_in_kg, special_notes, 
                            distance_list_id)
        temp_packages_table.add_element(package_id, current_package)

    return temp_packages_table


"""
Reads in the distance matrix from WGUPS Distance Table
@return the two-dimensional list of distances
"""
def read_in_distances():
    distance_matrix = list()
    loc = "WGUPS Distance Table.xlsx"

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(7, sheet.nrows):
        currentRow = sheet.row_values(i)
        currentRow[1] = currentRow[1].replace('South', 'S')
        distance_matrix.append(currentRow)

    return distance_matrix

"""
Excel stores times as fractions of a 24 hour day
The below method converts the passed in fraction into 
a string
@return the time as string
"""
def time_as_str(excel_time):
    time = excel_time * 24
    hours = int(time)

    minutes = time % 1
    minutes *= 60
    minutes = int(minutes)

    time_str = str(hours) + ':' + str(minutes)

    if hours < 10: #pad hours with a zero
        time_str = '0' + time_str
    
    if minutes < 10: #pad minutes with a zero
        time_str = time_str[:3] + '0' + time_str[3:]

    return time_str

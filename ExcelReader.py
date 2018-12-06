"""
Reads in the data from the excel files associated with the project using the xlrd module
Excel interaction code adapted from 
https://www.geeksforgeeks.org/reading-excel-file-using-python/
"""

from DirectHashTable import *
from Package import *
import xlrd

def read_in_packages():
    temp_packages_table = DirectHashTable()

    loc = "WGUPS Package File.xlsx"

    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    
    for i in range(8, sheet.nrows-1):
        package_id = sheet.cell_value(i, 0)
        address = sheet.cell_value(i, 1)
        city = sheet.cell_value(i, 2)
        state = sheet.cell_value(i, 3)
        zipcode = str(sheet.cell_value(i, 4))
        package_deadline = str(sheet.cell_value(i, 5))
       	weight_in_kg = sheet.cell_value(i, 6)
        special_notes = sheet.cell_value(i, 7)
        current_package = Package(package_id, address, city, state, zipcode,
                            package_deadline, weight_in_kg, 
                            special_notes, 'waiting')
        temp_packages_table.add_element(package_id, current_package)

    return temp_packages_table

def read_in_distances():
    distance_matrix = list()
    loc = "WGUPS Distance Table.xlsx"

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(7, sheet.nrows-1):
        distance_matrix.append(sheet.row_values(i))

    return distance_matrix
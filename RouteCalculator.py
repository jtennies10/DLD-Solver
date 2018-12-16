""" Joshua Tennies Student ID:#000885921"""

import sys
#import truck
from Truck import *


"""
Given a list of packages, calculates the route to take with those packages
in a greedy manner, this algorithm is meant for grouped packages such as 
those that must be delivered together or can only be on truck 2
@return the list of package in order of the route to take
"""
def calculate_greedy_route(greedy_list, packages_table, distance_matrix):
    calculated_route = list() 
    inc = 0

    #loop through greedy_list finding the next best package to deliver
    #and add it to calculated_route, also remove that package from the 
    #greedy_list
    while len(greedy_list) > 0:
        inc += 1
        last_distance_id = 0
        nextMinMovement = float(sys.maxsize)
        nextMovementId = -1
        for package_id in greedy_list:

            currentMovement = int()

            package = packages_table.search(package_id)

            #search the distance matrix based on which distance id is greater,
            #because searching the smaller id's row for the larger id column
            #will yield an error
            if package.get_distance_list_id() >= last_distance_id:
                currentMovement = float(
                    distance_matrix[package.get_distance_list_id()][last_distance_id+2])

            else:
                currentMovement = float(
                    distance_matrix[last_distance_id][package.get_distance_list_id()+2])

            #check if the given package is closer than the currently 
            #stored next movement
            if  (currentMovement < nextMinMovement):
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()

        last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
        calculated_route.append(nextMovementId)
        greedy_list.remove(nextMovementId)

    return calculated_route

"""
Adds onto the current_driver's delivery time based on the delivery_distance
"""
def add_delivery_time(driver_times, current_driver, delivery_distance):
    #retrieve the driver's current time
    current_driver_hours = driver_times[current_driver][0]
    current_driver_minutes = driver_times[current_driver][1] 
    
    #calculate the delivery time in minutes
    delivery_time = round(delivery_distance / Truck.TRUCK_SPEED_MPH * 60) 
    
    current_driver_minutes += delivery_time 
    
    #check to see if adding the delivery time on made minutes exceed 59,
    #if so convert minutes to hours as necessary
    if current_driver_minutes >= 60:  
        current_driver_hours += int(current_driver_minutes / 60)
        current_driver_minutes %= 60
    

    #set the driver_times to the updated times
    driver_times[current_driver][0] = current_driver_hours
    driver_times[current_driver][1] = current_driver_minutes
        
"""
Checks to see if a given package notes is deliverable based
on what time the package is delayed until  or has the wrong address until
and what is the time of the current_driver
"""
def is_package_deliverable(package_notes, driver_times, current_driver):
    #get the starting index of the time in the package_notes
    time_start = package_notes.index('until ') + 6

    fixed_hour = 0
    fixed_minute = 0 
    if len(package_notes) - time_start == 7: #hours is a single digit
        fixed_hour = int(package_notes[time_start:time_start+1])
        fixed_minute = int(package_notes[time_start+2:time_start+4])
    else: #hours is two digits
        fixed_hour = int(package_notes[time_start:time_start+2])
        fixed_minute = int(package_notes[time_start+3:time_start+5])

    #retrieve driver's current time
    driver_hour = driver_times[current_driver][0]
    driver_minute = driver_times[current_driver][1]

    if fixed_hour > driver_hour: 
        return False
    elif fixed_hour == driver_hour and fixed_minute >= driver_minute:
        return False
    else: #package can be delivered
        return True
    

"""
Calculates the near optimal route of the trucks using a greedy approach
that factors in time deadlines and each type of special note into creating the route
@return the total miles driven
"""
def calculate_near_optimal_route(trucks_in_optimal_route, distance_matrix, packages_table):
    
    minimum_distance = float() #holds the total miles of the route
    GROUPED_TOGETHER_STR = 'Must be delivered with '

    #create a list holding all the package ids that will be depleted
    #over time
    remaining_package_ids = list(range(1,len(packages_table.table)+1))

    #create two lists to hold grouped package ids and truck two only
    #package ids
    grouped_package_ids = list()
    truck_two_packages_only = list()

    #iterate through the packages, adding each package to grouped_package_ids
    #or truck_two_packages_only if necessary
    for i in remaining_package_ids:
        package = packages_table.search(i)
        current_special_notes = package.special_notes
        if GROUPED_TOGETHER_STR in current_special_notes:
            #if package is not already in grouped packages, 
            #add the package and its associated packages
            if i not in grouped_package_ids:
                grouped_package_ids.append(i)
            
            associated_package_ids = current_special_notes[
                len(GROUPED_TOGETHER_STR):len(current_special_notes)]
            associated_package_ids = associated_package_ids.split(', ') 

            for j in associated_package_ids:
                if int(j) not in grouped_package_ids:
                    grouped_package_ids.append(int(j)) 
            
        elif 'truck 2' in package.special_notes:
            truck_two_packages_only.append(i)  

    #greedy algorithm both the grouped_package_ids
    #and the truck_two_packages_only
    grouped_package_ids = calculate_greedy_route(
        grouped_package_ids, packages_table, distance_matrix)
    truck_two_packages_only = calculate_greedy_route(
        truck_two_packages_only, packages_table, distance_matrix)

    #create a list holding the time of day each driver is at
    driver_times = list()
    for driver in range(0, Truck.NUM_DRIVERS):
        driver_times.append([8,0]) #add each drivers time to the list, initialized as 8:00

    
    #greedy algorithm all the packages, keeping track of time throughout
    #to see if a package can be added or must be added, add
    #grouped or truck 2 lists altogether when appropriate
    
    #iterate through each set of trucks, incrementing by the number of drivers
    #to symbolize the fact each driver can be moving at the same time
    inc = 0
    while inc < Truck.NUM_TRUCKS:
        inc += Truck.NUM_DRIVERS
        
        last_distance_id = 0
        
        #iterate through the number of packages from 0 to 
        #the truck's package capacity
        for package_i in range(0, Truck.PACKAGE_CAPACITY):
            
            #check if any packages remain, if not then break the loop
            if not len(remaining_package_ids) > 0: 
                break

            #iterate through each driver currently in route and add
            #the next appropriate package to their route
            for current_driver in range(0,Truck.NUM_DRIVERS):
                #get index of current truck and make sure it is valid
                current_truck_index = current_driver + (inc - Truck.NUM_DRIVERS)
                
                if current_truck_index >= Truck.NUM_TRUCKS:
                    continue

                #get the number of packages on the truck currently
                packages_on_truck = len(trucks_in_optimal_route[
                    current_truck_index].get_package_ids_on_board())

                #if current truck is full skip to next iteration
                #if not get the distance id of the last package on the route
                if packages_on_truck >= Truck.PACKAGE_CAPACITY:
                    continue
                elif packages_on_truck > 0:
                    last_distance_id = packages_table.search(trucks_in_optimal_route[current_driver]
                        .get_package_ids_on_board()[packages_on_truck-1]).get_distance_list_id()
                else:
                    last_distance_id = 0

                #check to see if the current truck is truck two and if adding all the truck two
                #only packages will fill the truck, if so add them
                if (current_truck_index+1 == 2 and 
                    packages_on_truck+len(truck_two_packages_only)==Truck.PACKAGE_CAPACITY): #add the packages for truck_two only
                    nextMinMovement = float(sys.maxsize)

                    t2_index = 0
                    while(t2_index < len(truck_two_packages_only)):
                        truck_two_id = truck_two_packages_only[t2_index]
                        trucks_in_optimal_route[current_truck_index].add_package_id(truck_two_id)
                        remaining_package_ids.remove(truck_two_id)

                        #retrieve nextMinMovement from the distance matrix based on 
                        #which distance id is larger to prevent errors
                        if package.get_distance_list_id() >= last_distance_id:
                            nextMinMovement = float(
                                distance_matrix[package.get_distance_list_id()][last_distance_id+2])

                        else:
                            nextMinMovement = float(
                                distance_matrix[last_distance_id][package.get_distance_list_id()+2])
                    
                        #add the distance, delivery time, increment t2_index, and update last_distance_id
                        minimum_distance += nextMinMovement
                        add_delivery_time(driver_times, current_driver, nextMinMovement)
                        packages_table.search(truck_two_id).set_delivered_time(
                            driver_times[current_driver][0], driver_times[current_driver][1])
                        last_distance_id = packages_table.search(truck_two_id).get_distance_list_id()
                        t2_index += 1

                else: 
                    nextMinMovement = float(sys.maxsize)
                    nextMovementId = -1

                    #iterate throught the packages remaining
                    #to find the next best package
                    for package_id in remaining_package_ids: 

                        currentMovement = int()
                        package = packages_table.search(package_id)

                        #check to see if this package can only be on truck two,
                        #if so end this iteration and continue to the next
                        if 'truck 2' in package.special_notes: continue

                        #check if this package is delayed or has the wrong address,
                        #if so and it is not deliverable yet, continue onto the next
                        #iteration
                        if ('Delayed on flight' in package.special_notes 
                            or 'Wrong address listed' in package.special_notes):
                            if not is_package_deliverable(package.special_notes, driver_times, current_driver):
                                continue

                        #get the distance from the previous package to this one 
                        #based on distance list ids
                        if package.get_distance_list_id() >= last_distance_id:
                            currentMovement = float(
                                distance_matrix[package.get_distance_list_id()][last_distance_id+2])

                        else:
                            currentMovement = float(
                                distance_matrix[last_distance_id][package.get_distance_list_id()+2])
                        
                        #if the currentMovement is cheaper of the package has a deadline that
                        #is sooner than nextMinMovement, set it to be the next package to be delivered
                        #precedence is given to deadline over distance
                        if  (currentMovement < nextMinMovement or package.has_deadline()):
                            if (nextMovementId != -1 and 
                                packages_table.search(nextMovementId).has_deadline()): #compare deadlines
                                if package.package_deadline < packages_table.search(
                                    nextMovementId).package_deadline:
                                    nextMinMovement = currentMovement
                                    nextMovementId = package.get_package_id()
                            else:
                                nextMinMovement = currentMovement
                                nextMovementId = package.get_package_id()    


                    #check to see if the current minimum package is part of 
                    #grouped_package_ids, if so add all the packages to the current truck
                    #if not then add the package and continue iterating as normal
                    if nextMovementId in grouped_package_ids: 
                        for grouped_id in grouped_package_ids:
                            trucks_in_optimal_route[current_truck_index].add_package_id(grouped_id)
                            remaining_package_ids.remove(grouped_id)

                            package = packages_table.search(grouped_id)

                            #get distance based on the distance list ids of each package
                            if package.get_distance_list_id() >= last_distance_id:
                                nextMinMovement = float(
                                    distance_matrix[package.get_distance_list_id()][last_distance_id+2])

                            else:
                                nextMinMovement = float(
                                    distance_matrix[last_distance_id][package.get_distance_list_id()+2])
                            
                            minimum_distance += nextMinMovement
                            add_delivery_time(driver_times, current_driver, nextMinMovement)
                            packages_table.search(grouped_id).set_delivered_time(
                                driver_times[current_driver][0], driver_times[current_driver][1])
                            last_distance_id = packages_table.search(grouped_id).get_distance_list_id()
                    
                    else: #package was not part of the grouped list and can just add the single package
                        
                        trucks_in_optimal_route[current_truck_index].add_package_id(nextMovementId)
                        remaining_package_ids.remove(nextMovementId)
                        minimum_distance += nextMinMovement
                        add_delivery_time(driver_times, current_driver, nextMinMovement)
                        packages_table.search(nextMovementId).set_delivered_time(
                            driver_times[current_driver][0], driver_times[current_driver][1])


        #add the distances for each driver to return to the hub
        for current_driver in range(0, Truck.NUM_DRIVERS):
            current_truck_index = current_driver + (inc - Truck.NUM_DRIVERS)
            if current_truck_index >= Truck.NUM_TRUCKS:
                continue

            #retrieve the last_package_id from the truck in the route
            last_package_id = trucks_in_optimal_route[current_truck_index].get_package_ids_on_board()[
                len(trucks_in_optimal_route[current_truck_index].get_package_ids_on_board())-1]

            #get the last_distance_id and add the return time to the minimum distance
            #and the driver_time
            last_distance_id = packages_table.search(last_package_id).get_distance_list_id()
            return_to_hub_distance = distance_matrix[last_distance_id][2]
            minimum_distance += return_to_hub_distance
            add_delivery_time(driver_times, current_driver, return_to_hub_distance)

    return round(minimum_distance, 1)

"""
Displays each package and its delivery status based on the passed
in hours and minutes
"""
def packages_at_time(packages_table, distance_matrix, trucks_in_optimal_route, hours, minutes):

    print('\n\nTruck package lists at: ' + str(hours) + ':' + str(minutes) + '\n')

    for i in range(0, len(trucks_in_optimal_route)):
        print('Truck ' + str(i+1) + ': ' + str(trucks_in_optimal_route[i]))

    print('\n\nPackage statuses at: ' + str(hours) + ':' + str(minutes) + '\n')

    for package in packages_table:

        print(package)
        if package.delivered_hours < hours:
            print('Status: Delivered\n')
        elif package.delivered_hours == hours:
            if package.delivered_minutes <= minutes:
                print('Status:Delivered\n')
            else:
                print('Status:Not Yet Delivered\n')
        else:
            print('Status:Not Yet Delivered\n')




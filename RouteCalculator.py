import sys
#import truck
from Truck import *



def calculate_greedy_route(greedy_list, packages_table, distance_matrix):
    calculated_route = list()
    inc = 0
    while len(greedy_list) > 0:
        inc += 1
        last_distance_id = 0
        nextMinMovement = float(sys.maxsize)
        nextMovementId = -1
        for package_id in greedy_list:
            #print(package_id)
            # print(str(last_distance_id))

            currentMovement = int()
            #print(str(package_id))
            package = packages_table.search(package_id)
            # if package is None: break

            if package.get_distance_list_id() >= last_distance_id:
                currentMovement = float(
                    distance_matrix[package.get_distance_list_id()][last_distance_id+2])

            else:
                currentMovement = float(
                    distance_matrix[last_distance_id][package.get_distance_list_id()+2])
            
            #print(str(currentMovement))
            if  (currentMovement < nextMinMovement ):
                # and trucks_in_optimal_route[i].get_package_ids_on_board().count(
                #     package.get_package_id()) < 1):
                #print('true')
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()

        # print(str(nextMovementId))
        last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
        calculated_route.append(nextMovementId)
        greedy_list.remove(nextMovementId)
        #minimum_distance += nextMinMovement
        # print('\n\n\n' + str(nextMinMovement))
        # print(str(minimum_distance) + '\n\n\n')

        # print(remaining_package_ids)

    return calculated_route

def add_delivery_time(drivers_times, current_driver, delivery_distance):
    current_driver_hours = drivers_times[current_driver][0]
    current_driver_minutes = drivers_times[current_driver][1] 
    
    #calculate the delivery time in minutes
    #time = distance * 1/TRUCK_SPEED_MPH * 60 minutes
    delivery_time = round(delivery_distance * (1/Truck.TRUCK_SPEED_MPH) * 60) 
    print(str(delivery_time))
    current_driver_minutes += delivery_time 
    if current_driver_minutes >= 60: #negate the 
        current_driver_hours += int(current_driver_minutes / 60)
        current_driver_minutes %= 60
    
    drivers_times[current_driver][0] = current_driver_hours
    drivers_times[current_driver][1] = current_driver_minutes
        
    


def calculate_near_optimal_route(trucks_in_optimal_route, distance_matrix, packages_table):
    
    minimum_distance = float() #holds the total miles of the route
    GROUPED_TOGETHER_STR = 'Must be delivered with '

    remaining_package_ids = list(range(1,len(packages_table.table)+1))

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

    # print(grouped_package_ids)
    # print(truck_two_packages_only)

    #create a list holding the time of day each driver is at
    driver_times = list()
    for driver in range(0, Truck.NUM_DRIVERS):
        driver_times.append([8,0]) #add each drivers time to the list, initialized as 8:00

    # add_delivery_time(driver_times, 0, 18)
    # add_delivery_time(driver_times, 0, 20)

    # print(driver_times)

    #greedy algorithm all the packages, keeping track of time throughout
    #to see if a package can be added or must be added, add
    #grouped or truck 2 lists altogether when appropriate
    
    #iterate through each set of trucks, incrementing by the number of drivers
    #to symbolize the fact each driver can be moving at the same time
    inc = 0
    while inc < Truck.NUM_TRUCKS:
        inc += Truck.NUM_DRIVERS
        
        last_distance_id = 0
        
        for i in range(0,Truck.NUM_DRIVERS):
            #TODO:check if this is truck 2 
            current_truck_index = i + (inc - Truck.NUM_DRIVERS)

            packages_on_truck = 0
            while packages_on_truck < Truck.PACKAGE_CAPACITY and len(remaining_package_ids) > 0:
                
                nextMinMovement = float(sys.maxsize)
                nextMovementId = -1
                for package_id in remaining_package_ids: #fix to iterate on each item in a list
                    #print(package_id)
                    # print(str(last_distance_id))

                    currentMovement = int()
                    # print(str(package_id))
                    package = packages_table.search(package_id)
                    if package is None: break

                    if package.get_distance_list_id() >= last_distance_id:
                        currentMovement = float(
                            distance_matrix[package.get_distance_list_id()][last_distance_id+2])

                    else:
                        currentMovement = float(
                            distance_matrix[last_distance_id][package.get_distance_list_id()+2])
                    
                    #print(str(currentMovement))
                    if  (currentMovement < nextMinMovement ):
                        # and trucks_in_optimal_route[i].get_package_ids_on_board().count(
                        #     package.get_package_id()) < 1):
                        #print('true')
                        nextMinMovement = currentMovement
                        nextMovementId = package.get_package_id()

                # print(str(nextMovementId))
                last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
                trucks_in_optimal_route[current_truck_index].add_package_id(nextMovementId)
                remaining_package_ids.remove(nextMovementId)
                minimum_distance += nextMinMovement

                packages_on_truck += 1

                # print('\n\n\n' + str(nextMinMovement))
                # print(str(minimum_distance) + '\n\n\n')

                # print(remaining_package_ids)

        
            # TODO:add miles to return to office
        print('returning home')
        minimum_distance += distance_matrix[last_distance_id][2]

    return round(minimum_distance, 1)


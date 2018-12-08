import sys
#import truck
from Truck import *

TIME_SENSITIVE_WEIGHT = 5
GROUPED_TOGETHER_WEIGHT = 4
TRUCK_TWO_ONLY_WEIGHT = 3
DELAYED_WEIGHT = 2
WRONG_ADDRESS_WEIGHT = 1

#adds grouped weight if not already added
def add_grouped_package_weight(current_package_weight):
    
    if int(current_package_weight / TIME_SENSITIVE_WEIGHT) == 1:
        current_package_weight %= 5
        
    if current_package_weight / GROUPED_TOGETHER_WEIGHT == 1: #package weight was already added
        return 0
    else: #grouped weight has not yet been added
        return GROUPED_TOGETHER_WEIGHT

def calculate_near_optimal_route(trucks_in_optimal_route, table_size, distance_matrix, packages_table):
    #using a greedy algorithm
    #that gets an approximate solution in O(n^3)
    

    minimum_distance = float()

    #create a list of tuples holding a package id and its given 
    #weight based on the factors below
    remaining_package_ids = list()
    for i in range(1, len(packages_table.table)+1):
        remaining_package_ids.append([i, 0])

    

    GROUPED_TOGETHER_STR = 'Must be delivered with '
    
    
    for package in packages_table:
        current_deadline = package.package_deadline
        current_special_notes = package.special_notes
        current_package_id = package.get_package_id()
        #print(str(current_package_id)) 
        #print(current_special_notes)
        package_weight = 0
        #assign package to correct nested list based on conditions
        if 'EOD' not in current_deadline:
            #print('time-sens')
            #add time_sensitive_weight
            package_weight += TIME_SENSITIVE_WEIGHT

        #check for a special note, there can only be one    
        if current_special_notes.find(GROUPED_TOGETHER_STR) >= 0:
            
            #add to grouped_together, ISSUE OF NOT ADDING WEIGHT TO ALL
            package_weight += add_grouped_package_weight(package_weight)
            grouped_packages = current_special_notes[
                len(GROUPED_TOGETHER_STR):len(current_special_notes)]
            
            grouped_packages = grouped_packages.split(', ') 
            for i in grouped_packages: #call add_grouped_packaged_weight on each item
                #print(i)
                #print(str(remaining_package_ids[int(i)-1][1]))
                #print('looping')
                remaining_package_ids[int(i)-1][1] += add_grouped_package_weight(
                    remaining_package_ids[int(i)-1][1])

            #print(remaining_package_ids)


        elif 'truck 2' in current_special_notes:
            #print('truck two')
            #add to truck_two
            package_weight += TRUCK_TWO_ONLY_WEIGHT
        elif 'Delayed' in current_special_notes:
            #add to delayed
            package_weight += DELAYED_WEIGHT
        elif 'Wrong address listed' in current_special_notes:
            #add to wrong_address
            package_weight += WRONG_ADDRESS_WEIGHT

        #add tuple to list 
         
        remaining_package_ids[current_package_id-1][1] += package_weight




    print(remaining_package_ids)




    for i in range(0,len(trucks_in_optimal_route)):
        inc = 0
        last_distance_id = 0

        while inc < Truck.PACKAGE_CAPACITY and len(remaining_package_ids) > 0:
            inc += 1
            nextMinMovement = float(sys.maxsize)
            nextMovementId = -1
            for package_id in remaining_package_ids: #fix to iterate on each item in a list
                #print(package_id)
                # print(str(last_distance_id))

                currentMovement = int()
                print(str(package_id))
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

            print(str(nextMovementId))
            last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
            trucks_in_optimal_route[i].add_package_id(nextMovementId)
            remaining_package_ids.remove(nextMovementId)
            minimum_distance += nextMinMovement
            # print('\n\n\n' + str(nextMinMovement))
            # print(str(minimum_distance) + '\n\n\n')

            print(remaining_package_ids)

        
            #TODO:add miles to return to office
        print('returning home')
        minimum_distance += distance_matrix[last_distance_id][2]

    return round(minimum_distance, 1)


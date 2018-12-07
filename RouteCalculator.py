import sys
#import truck
from Truck import *

def calculate_near_optimal_route(trucks_in_optimal_route, table_size, distance_matrix, packages_table):
    #using a greedy algorithm
    #that gets an approximate solution in O(n^3)
    

    minimum_distance = float()

    #create a list that holds all package ids, broken into lists representing 
    #special instructions and sensitivities, reference variables are then declared
    #to refer to each list in remaining_package_ids
    remaining_package_ids = [[],[],[],[],[],[]]
    TIME_SENSITIVE_INDEX = 0
    GROUPED_TOGETHER_INDEX = 1
    TRUCK_TWO_ONLY = 2
    DELAYED = 3
    WRONG_ADDRESS = 4
    OTHER = 5
    
    
    for package in packages_table:
        current_time = package.time
        current_special_notes = package.special_notes
        #assign package to correct nested list based on conditions

        #  remaining_package_ids.append(package.get_package_id())

    #print(remaining_package_ids)




    for i in range(0,len(trucks_in_optimal_route)):
        inc = 0
        last_distance_id = 0

        while inc < Truck.PACKAGE_CAPACITY and len(remaining_package_ids) > 0:
            inc += 1
            nextMinMovement = float(sys.maxsize)
            nextMovementId = -1
            for package_id in remaining_package_ids:
                # print(package)
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
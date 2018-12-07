import sys
import Truck

def calculate_near_optimal_route(trucks_in_optimal_route, table_size, distance_matrix, packages_table):
    #using a greedy algorithm
    #that gets an approximate solution in O(n^3)
    last_distance_id = 0
    inc = 0

    minimum_distance = float()

    #create a list that originally holds all the package ids of every
    #package in packages_table
    remaining_package_ids = list()
    for package in packages_table:
        remaining_package_ids.append(package.get_package_id())

    print(remaining_package_ids)

    while inc < table_size:
        inc += 1
        nextMinMovement = float(sys.maxsize)
        nextMovementId = -1
        for package_id in remaining_package_ids:
            # print(package)
            # print(str(last_distance_id))

            currentMovement = int()
            package = packages_table.search(package_id)

            if package.get_distance_list_id() >= last_distance_id:
                currentMovement = float(
                    distance_matrix[package.get_distance_list_id()][last_distance_id+2])

            else:
                currentMovement = float(
                    distance_matrix[last_distance_id][package.get_distance_list_id()+2])
            
            #print(str(currentMovement))
            if  (currentMovement < nextMinMovement 
                and trucks_in_optimal_route[0].get_package_ids_on_board().count(
                    package.get_package_id()) < 1):
                print('true')
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()

        
        last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
        trucks_in_optimal_route[0].add_package_id(nextMovementId)
        minimum_distance += nextMinMovement
        # print('\n\n\n' + str(nextMinMovement))
        # print(str(minimum_distance) + '\n\n\n')

    #TODO:add miles to return to office

    return round(minimum_distance, 1)
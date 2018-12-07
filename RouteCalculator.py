import sys

def calculate_near_optimal_route(trucks_in_optimal_route, table_size, distance_matrix, packages_table):
    #using a greedy algorithm
    #that gets an approximate solution in O(n^3)
    last_distance_id = 0
    inc = 0

    minimum_distance = float()

    while inc < table_size:
        inc += 1
        nextMinMovement = float(sys.maxsize)
        nextMovementId = -1
        for package in packages_table:
            # print(package)
            # print(str(last_distance_id))

            currentMovement = int()
            if package.get_distance_list_id() >= last_distance_id:
                currentMovement = float(distance_matrix[package.get_distance_list_id()][last_distance_id+2])

            else:
                currentMovement = float(distance_matrix[last_distance_id][package.get_distance_list_id()+2])
            
            print(str(currentMovement))
            if  currentMovement < nextMinMovement and trucks_in_optimal_route.count(package.get_package_id()) < 1:
                print('true')
                nextMinMovement = currentMovement
                nextMovementId = package.get_package_id()

        
        last_distance_id = packages_table.search(nextMovementId).get_distance_list_id()
        trucks_in_optimal_route[0].add_package(nextMovementId)
        minimum_distance += nextMinMovement
        print('\n\n\n' + str(nextMinMovement))
        print(str(minimum_distance) + '\n\n\n')

    return round(minimum_distance, 1)
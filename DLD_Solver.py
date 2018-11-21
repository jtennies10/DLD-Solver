from Truck import *
from Delivery import *

#program control here

#test Truck and Delivery
t1 = Truck()
t2 = Truck()

d1 = Delivery(1, '17 Foreman st', 
'Eldred', 'PA', '16731', '10:00 am', 30, '', 'waiting')

print(t1.packages_on_board)

t2.add_package(d1)

print('t2: ' + t2.packages_on_board)






    





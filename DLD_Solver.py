from Truck import *
from Delivery import *
from DirectHashTable import *

#program control here

#test Truck and Delivery
t1 = Truck()
t2 = Truck()

d1 = Delivery(1, '17 Foreman st', 
'Eldred', 'PA', '16731', '10:00 am', 30, '', 'waiting')

print(d1)

print(t1)

t2.add_package(d1)

print(t2)






    





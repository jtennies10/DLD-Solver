from Truck import *
from Delivery import *
from DirectHashTable import *
from datetime import *


#instantiate the hours and minutes for the beginning of the day
hour_of_day = 8
minutes_of_hour = 0


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






    





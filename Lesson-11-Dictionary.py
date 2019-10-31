

#!/bin/python3.6
import os

print(os.name)


print("-------------------------------")
print("----Lesson-11-Dictionary-------")
print("-------------------------------")

#    (----Items---)
#    (key)   (value)


enemy = {
    'loc_x': 80,
    'loc_y': 50,
    'color': 50,
    'health': 100,
    'name': 'Mort'
}

print("Location X = " + str(enemy['loc_x']))

enemy['rank'] = 'Arm'
print(enemy)
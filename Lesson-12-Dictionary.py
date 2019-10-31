


enemy = {
    'loc_x': 80,
    'loc_y': 50,
    'color': 50,
    'health': 100,
    'name': 'Mort'
}


# Создадим масив

all_enemy = []
all_enemy.append(enemy)

for x in range(0,10):
    all_enemy.append(enemy.copy())

for x in all_enemy:
    print(all_enemy)


all_enemy[5]['health'] = 30
print("-----------------")
for ene in all_enemy:
    print (ene)






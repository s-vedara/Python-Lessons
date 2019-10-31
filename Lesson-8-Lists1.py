

##Массивы


cities = ['qwer', 'asdf', 'zxc']
print(cities)
print(len(cities))      ##Длина масива
print(cities[1])    #Показать с массива, считается с нуля
print(cities[-1])    #Показать с конца массива первый,
print(cities[1].title())    #Показать + укажем чтобы показывал с большой буквы
cities[2] = 'Tula'  ##Изменить масив
print(cities)

cities.append('Kursk')  ##Добавить в конец
print(cities)

cities.insert(2, 'Feo') ##Добавить где-то
print(cities)

del cities[-1] ##Удалить
print(cities)

cities.remove('Feo')    ##Удалить по имени
print(cities)

cities.sort()       ## Отсортировать
print(cities)

cities.reverse()       ## Отсортировать в обратном порядке
print(cities)



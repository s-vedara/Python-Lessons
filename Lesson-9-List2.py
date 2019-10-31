


cars = ['qwer', 'asdf', 'zxc']

for x in cars:
    print(x.upper())

mynumber_list = list(range(0, 10))
print(mynumber_list)

print ("=================")
for x in mynumber_list:
    x = x * 2
    print(x)

print("Max number is:" + str(max(mynumber_list)))
print("Min number is:" + str(min(mynumber_list)))
print("Sum number is:" + str(sum(mynumber_list)))


mycars = cars[:]  ## Сделать копию масива, знак : от начала до конца.
# mycars = cars     соеденить один к другому



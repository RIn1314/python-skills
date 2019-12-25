from pprint import pprint as pp

# x的10次方
data = {'powers': [x ** 10 for x in range(10)]}
# x的10次方
items2 = [x ** 2 for x in range(1, 10) if x % 2]
item = {'x*x': [x ** 2 for x in range(1, 10)]}
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))

global ids
ids = 20

globals()['ids'] = 100
print(ids)

print(data)
pp(items2)
pp(item)
pp(items1)

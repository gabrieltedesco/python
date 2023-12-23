#LISTS
my_list = ["banana", "cherry"]
my_list2 = list(my_list)
my_list2.append("apple")
my_list.clear()
list_comp = [i**2 for i in range(1, 5)]

#TUPLES
my_tuple = ("banana", "cherry")

#DICTIONARIES
my_dict = {"fruit1": "banana", "fruit2":"cherry"}
my_dict["fruit3"] = "apple"
del my_dict["fruit3"]
for key, value in my_dict.items():
    print(key, value)

#SETS
my_set = set([1, 2, 3, 1, 2])
my_set.add(3)
my_set.discard(4)
odds = {1, 3, 5, 7}
evens = {2, 4, 6, 8}
u = odds.union(evens)
i = odds.intersection(evens)

#STRINGS
my_string = "hello world"
my_string.strip().lower()
print(my_string[5:10:2])
print(my_string.find('w'))
print(my_string.count('w'))
new_list = my_string.split(" ")
new_string = ' '.join(new_list) 
print(f'the answer is {my_string}')

#COLLECTIONS
from collections import Counter, namedtuple, deque
var1 = "aaaaaabbbbccc"
my_counter = Counter(var1)
print(my_counter.most_common())

my_namedtuple = namedtuple('Point', 'x,y', )
pt = my_namedtuple(1, -4)

my_deque = deque()
my_deque.append(2)
my_deque.appendleft(1)
my_deque.extend([3, 4, 5])
my_deque.rotate(1)

#ITERTOOLS
from itertools import product, permutations, combinations, accumulate, groupby
var2 = [1, 2, 3, 4]
var3 = [3]
my_product = product(var2, var3, repeat=1)
print(list(my_product))
my_permutation = permutations(var2)
print(list(my_permutation))
my_combination = combinations(var2, 2)
print(list(my_combination))
my_accumulate = accumulate(var2)
print(list(my_accumulate))
import operator
my_accumulate2 = accumulate(var2, func=operator.mul)
print(list(my_accumulate2))
my_groupby = groupby(var2, key=lambda x: x<3)
for key, value in my_groupby:
    print(key, list(value))

#LAMBDA FUNCTIONS
add10 = lambda x: x+10
print(add10(5))
multiply = lambda x,y: x*y
print(multiply(4, 5))
points2D = [(1, 2), (15, 1), (5, 1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

var4 = [1, 2, 3, 4, 5]
my_map = map(lambda x: x+2, var4)
my_filter = filter(lambda x: x%2==0, var4)
from functools import reduce
my_reduce = reduce(lambda x,y: x*y, var4) #uso como fatorial de um valor

#EXCEPTIONS
#2:04:00



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



#EXCEPTIONS AND ERRORS
var5 = -5
if var5 < 0:
    raise ValueError
try:
    var5 = 5/0
except Exception as e:
    print(f'an error hapenned because {e}')
else:
    print("everything is fine")
finally:
    print("cleaning up")

class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")



#LOGGING
import logging

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.warning('this is a warning')
logger.error('this is an error')



#JSON
#read example.json and example.py

#RANDOM NUMBERS
import random
var7 = random.uniform(1, 10)
var7 = random.randint(1, 10)
var7 = random.choice(var2)
var7 = random.sample(var2, 3)
random.shuffle(var2)
random.seed(1) #used to reproduce your data

import secrets
#used for passwords, security tokens and account authetication
var8 = secrets.randbelow(10)
var8 = secrets.randbits(8) #00000000 to 11111111
var8 = secrets.choice(var2)
#also you can import the numpy module



#DECORATORS
#function and class decorators
import functools
def StartEnd(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@StartEnd
def print_name(): 
    print('Alex')

print_name()


def StartEnd2(func):

    @functools.wraps(func) #used to clarify for python when "help" is used
    def wrapper(*args, **kwargs):
        print('Start') #Do anything before the function
        var9 = func(*args, **kwargs)
        print('End') #Do anything after the function
        return var9
    return wrapper

@StartEnd2
def add5(x): 
    return x+5

var9 = add5(5)
print(var9)


def repeat(num_times): #when decorators use arguments 
    def decorator_repeat(func): 
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet("Alex")

#finally, you can also make nested decorators above the function
#you can apply class decorators in functions, it's used if we want to maintain and update a state. in order to use the "wrapper function", we use the "class method"
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()



#GENERATORS
#defined like a normal function, but generate items only when you for it
#uses yield keyword instead of the return keyword
def my_generator():
    yield 1

gen = my_generator()
var10 = next(gen) #runs the function until the first yield statement
print(var10)

#you can use them as inputs to other functions that take iterables
print(sum(gen))
print(sorted(gen))

#thay save a lot of memory when you work with large data
#classic example is the Fibonacci sequence
def firstn_gen(n):
    control = 0
    while n != control:
        yield control
        control += 1

def firstn(n):
    nums = []
    control = 0
    while control < n:
        nums.append(control)
        control += 1
    return nums

print(firstn(10)) #8697464
print(firstn_gen(10)) #120

#Generetor Expressions: 
my_generator2 = (i for i in range(10) if i % 2 == 0)
list(my_generator2)



#THREADING NAD MULTIPROCESSING
"""
Process: An instance of a program (e.g a Python interpreter)
+ Takes advantage of multiple CPUs and cores
+ Separate memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is stated independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process -> avoids GIL limitation
- Heavyweight
- Starting a process is slower than starting a thread.
- More memory
- IPC (inter-process communication) is more complicated

Threads: An entity within a process that can be scheduled (also known as "leightweight process) A process can spawn multiple threads.
+ All threads within a process share the same memory
+ Leightweight
+ Starting a thread is faster than starting a process
- Great for 10-bound tasks
- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions, when threads wants to modify the same varaible at the same time
"""

from multiprocessing import Process
import os

processes = []
number_processes = os.cpu_count()

#create processes
for i in range(number_processes):
    p = Process(targer)
4:02:00
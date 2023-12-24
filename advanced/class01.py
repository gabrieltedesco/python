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



#THREADING AND MULTIPROCESSING
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

Threads: An entity within a process that can be scheduled (also known as leightweight process) A process can spawn multiple threads.
+ All threads within a process share the same memory
+ Leightweight
+ Starting a thread is faster than starting a process
- Great for 10-bound tasks
- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions, when threads wants to modify the same varaible at the same time
"""



#MULTIPROCESSING
#example 1
from multiprocessing import Process
import os
def square_numbers():
    for i in range(100):
        i*i

processes = []
number_processes = os.cpu_count()

#create processes
for i in range(number_processes):
    p = Process(target=square_numbers)
    processes.append(p)

#start
for p in processes:
    p.start()

#join
for p in processes:
    p.join()

print("end main")


#example 2
from multiprocessing import Process, Value, Array, Lock
import time

def add100(number, lock):    
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1 #some operation can get lost here because of race conditions
            #this is the process to share a single value

if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0)
    print(f"number at the beginnig is {shared_number.value}")

    #create processes and assign a function
    p1 = Process(target=add100, args=(shared_number, lock))
    p2 = Process(target=add100, args=(shared_number, lock))

    #start all processes
    p1.start()
    p2.start()

    #wait all the processes to finish by blocking the main program
    #join 
    p1.join()
    p2.join()

    print(f"number at end is {shared_number.value}")
    print("end main")

#in multithreading, you can share data with a global variable because they live in the same memory space. in multiprocessing, they need special shared memory to share data
#there are two shared memory objects: value and array


#example 3
from multiprocessing import Process, Value, Array, Lock
import time

def add100(numbers, lock):    
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for i in range(len(numbers)):
                numbers[i] += 1
                #this is the process to share a multiple value
                #increasing each number by 200

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print(f"array at the beginnig is {shared_array[:]}")

    #create processes and assign a function
    p1 = Process(target=add100, args=(shared_array, lock))
    p2 = Process(target=add100, args=(shared_array, lock))

    #start all processes
    p1.start()
    p2.start()

    #wait all the processes to finish by blocking the main program
    #join 
    p1.join()
    p2.join()

    print(f"array at the end is {shared_array[:]}")
    print("end main")

#in multithreading, you can share data with a global variable because they live in the same memory space. in multiprocessing, they need special shared memory to share data
#there are two shared memory objects: value and array


#example 4
from multiprocessing import Process
from multiprocessing import Queue
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":
    
    numbers = range(1, 6)
    my_queue = Queue()
    p1 = Process(target=square, args=(numbers, my_queue))
    p2 = Process(target=make_negative, args=(numbers, my_queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    #there is no method queue.join()
    while not my_queue.empty():
        print(my_queue.get())


#you can also use a queue to exchange elements between processes
#it works the same way in multiprocessing and multithreading
#the module used is not "queue", but "multiprocessing"


#example 5
from multiprocessing import Pool

def cube(number):
    return number**3

if __name__ == "__main__":
    
    numbers = range(10)
    my_pool = Pool()
    #we want to create multiple processes that should acess or execute a function
    #the methods are: map, apply, join, close
    result = my_pool.map(cube, numbers)
    #automatically allocate the maximum number of available processes and create different processes that your machine can run, and then split this itrable into an equal sized chunks and submit this to the function in parallel
    #pool.apply(cube, numbers[0]) makes the same process, but for only one number to the function
    my_pool.close()
    my_pool.join()

    print(result)

#also there is "process pool" to manage multiple process
#So a process pool object controls a pool of worker processes to which chops can be submitted.
#basically, a pool takes care of a lot of things for you
#if you have interest, there are also asynchronous calls to this map and apply functions 



#THREADING
#example 1
from threading import Thread

#sharing data
database_value = 0

def square_numbers2():
    for i in range(100):
        i*i

threads = [] 
number_threads = os.cpu_count()

#create threads
for i in range(number_threads):
    t = Thread(target=square_numbers2)
    threads.append(t)

#start
for t in threads:
    t.start()

#join
for t in threads:
    t.join()

print("end main")


#example 2
from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value

    with lock:
        local_copy = database_value
    #processing
        local_copy +=1
        time.sleep(0.1) #this line allows race condition, that is solved by locking the state of thread 1 until it modifies the database_value
        database_value = local_copy


if __name__ == "__main__":
    lock = Lock()
    print("start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('end value', database_value)
    print("end main")


#example 3
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(n_queue, lock):
    while True:
        value = my_queue.get()
        #processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        my_queue.task_done()

if __name__ == "__main__":

    my_queue = Queue()
    lock = Lock()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(my_queue, lock))
        thread.daemon = True #used to stop all the threads when the main thread die
        thread.start()
    
    for i in range(1, 21):
        my_queue.put(i)
    my_queue.join()


    print("end main")


#if you use my_queue.put(), you add a new element to the queue
#if you use my_queue.get(), the first element of the queue is removed
#if you use my_queue.join(), this blocks until all items in the queue have been processed



#FUCTIONS ARGUMENTS
#function arguments and function parameters 
"""
- The difference between arguments (values passed for these parameters while calling a function) and parameters (used inside parentheses where definig a function)
- Positional (func(1, 2, 3)) and keyword arguments (func(a=1, b=2, c=3)) when calling a function
- Default arguments when defining a function (def func(a, b, c, d=4))
- Variable-length arguments (*args and **kwargs) when defining a function (def func(a, b, c, *args, **kwargs)), that args are in a tuple and kwags are in a dictionary. a example is (func(1, 2, 3, 4, 5, six=6, seven=7))
- Container unpacking into function arguments when the arguments required to a function is inside a list, like my_list = [1, 2, 3], so the calling of the function is func(*my_list)
- Local vs. global arguments is where that variable can be acessed and modified, functions, by defalut, have local scope variables. but mutable objects, like a list, can be modified inside a function
"""



#DEEP COPYING
#you have to take care when making copies of variables, because immutable types can works fine, but mutable types references the same value
#shallow copy: one level deep, only references of nested child objects, can be done with: var.copy(), list(var), var[:]
#deep copy: full independent copy, can be done with: 
import copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy [0][1] = -10
print(cpy)
print(org)
#this is necessary in nested lists, that are two levels deep
#it can also be used for objects
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Company:
    def __init__(self, boss, employee): 
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)
company = Company (p1, p2)

company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) 
print(company.boss.age)



#CONTEXT MANAGER
#they allow you to allocate and release resources when you want to
with open('notes.txt', 'w') as file:
    file.write('hello world')
#the with statement (context manager) will sure to correctly close our file again, and this avoids a code like this:
file open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()
#in general, context manager can be used to open/close databases and with "lock" method in threads. also, to implement in your own classes, we have to implement the "enter" and "exit" methods:
class ManagedFile():
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('doing something')
    file.write('hello world')
    file.somemethod() #this doesn't work, it just raises an exception

print('continuing...')



#POO 
#https://youtu.be/Ej_02ICOIgs
#PYTORCH
#https://www.youtube.com/playlist?list=PLWKjhJtqVAbm5dir5TLEy2aZQMG7cHEZp
#COMPUTER VISION
#https://youtu.be/01sAkU_NvOY
#always use python roadmap to guide your studies



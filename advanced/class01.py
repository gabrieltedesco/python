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
print (my_set)


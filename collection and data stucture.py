"""tuple = (1,2,3,'a','b','c')

my_list = [4,5,6]
tuple = tuple(my_list)

print(tuple)"""

"""my_tuple = 1,2,3

x,y,z = my_tuple
print(x)
print(y)
print(z)
print(my_tuple)"""

"""my_tuple = (1,2,3,'a','b','c')
print(my_tuple[0])
print(my_tuple[3])"""

"""tuple1 = (10,9,8)
tuple2 = (1,2,3)

concat_tuple = tuple1 + tuple2
print(concat_tuple)"""

"""tupp= (4,5)
repeated_tupp = tupp * 3
print(repeated_tupp)"""

"""my_tupp = (1,2,3)
print( 1 in my_tupp)
print('a' in my_tupp)"""

"""my_tup = (1, 2, 3)
my_tup[0] = 3
print(my_tup)"""

#conversion tupple to list
"""tup = (1,2,3)
new_tup = list(tup)

#list to tuppple
my_list = [5,6,7]
new_list = tuple(my_list)

print(f"conversion tupple: {new_tup}")
print(f"conversion list: {new_list}")"""

#add elements
"""my_set = {3,6,9}
my_set.add(12)
print(f"set: {my_set}")"""

"""my_set = {3,6,9}
my_set.update([3,23,34,56])
print(f"many: {my_set}")"""

#removing elements
"""my_s = {1,2,3,4,5}
my_s.remove(3)
my_s.discard(2)
popped = my_s.pop()
print(my_s)"""

#set union
"""my_set1 ={1,2,3}
my_set2 = {5,1,6,7}

union_set = my_set1.union(my_set2)
print(union_set)"""

#set intersection
"""my_set1 ={1,2,3}
my_set2 = {5,1,6,7}

union_set = my_set1.intersection(my_set2)
print(union_set)"""

#set difference
"""my_set1 ={1,2,3}
my_set2 = {5,1,6,7}

union_set = my_set1.difference(my_set2)
print(union_set)"""

#symmetric difference
"""my_set1 ={1,2,3}
my_set2 = {5,1,6,7}

union_set = my_set1.symmetric_difference(my_set2)
print(union_set)"""

#set membership test
"""my_set1 ={1,2,3}
my_set2 = {1,2,3,4,5,6,7}

print(my_set1.issubset(my_set2))
print(my_set2.issuperset(my_set1))"""

#issubset- all elements of one set exist in another set
#issuperset - one set contains all elements of another set

#dictionary
"""person = {"name": "marie", "age": 28, "occupation": "nurse"}

if "name" in person:
    print("Name exist in person")"""

#iteration nad looping
"""person = {"name": "marie", "age": 28, "occupation": "nurse"}
for key in person:
    print(key, person[key])"""

#dictionary comprehension
"""umbers = [1,2,3,4,5]
squares = {num: num*num for num in numbers}
print(squares)"""

#Dictionary Comprehension

fruits = ["apple","banana","orange","apple","grape","banana"]
fruit_count={}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit,0) + 1
print(fruit_count)
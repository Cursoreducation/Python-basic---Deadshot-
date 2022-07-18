#1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f"{id(int_a)}, {id(str_b)}, {id(set_c)}, {id(lst_d)}, {id(dict_e)}")

#2_Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)

print(id(lst_d))

#3_Define the type of each object from step 1.
print(f"{type(int_a)}, {type(str_b)}, {type(set_c)}, {type(lst_d)}, {type(dict_e)}")

#4_Check the type of the objects by using isinstance
print(f"{isinstance(int_a,int)}, {isinstance(str_b, str)}, {isinstance(set_c, set)}\n, "
     f"{isinstance(lst_d, list)}, {isinstance(dict_e, dict)}")

#5_With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(2, 3))

#6_By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(2, 3))

#7_By using keyword arguments into the curly braces.
print("Anna has {a} apples and {p} peaches.".format(a='2', p='3'))

#8*_With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:^5} apples and {1:^3} peaches.".format(2, 3))

#9_With f-strings and variables
n_apples = 2
n_peaches = 3

print(f"Anna has {n_apples} apples and {n_peaches} peaches.")

#10_With % operator
print("Anna has %s apples and %s peaches." % ('5', '6'))

#11*_With variable substitutions by name (hint: by using dict)
print("Anna has %(number_apples)s apples and %(number_peaches)s peaches." % {'number_apples': '7','number_peaches': 8})

#12_Convert (1) to list comprehension
#lst = []
#for num in range(10):
   #if num % 2 == 1:
       #lst.append(num ** 2)
   #else:
       #lst.append(num ** 4)
#print(lst) #[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst) #[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

#13_Convert (2) to regular for with if-else
#list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#print(list_comprehension) #[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
list_comprehension_1 = []
for num in range(10):
   if num % 2 == 0:
       list_comprehension_1.append(num // 2)
   else:
       list_comprehension_1.append(num * 10)
print(list_comprehension_1) #[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

#14_Convert (3) to dict comprehension.
#d = {}
#for num in range(1, 11):
#   if num % 2 == 1:
#       d[num] = num ** 2
#print(d) #{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d) #{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#15*_Convert (4) to dict comprehension.
#d = {}
#for num in range(1, 11):
#   if num % 2 == 1:
#       d[num] = num ** 2
#   else:
#       d[num] = num // 0.5
#print(d) #{1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

d = {num:num ** 2  if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d) #{1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

#16_Convert (5) to regular for with if.
#dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#print(dict_comprehension) #{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

dict_comprehension = {}
for x in range(10):
   if x**3 % 4 == 0:
       dict_comprehension[x] = x ** 3
print(dict_comprehension) #{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

#17*_Convert (6) to regular for with if-else.
#dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#print(dict_comprehension) #{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
dict_comprehension = {}
for x in range (10):
   if  x**3 % 4 == 0:
       dict_comprehension[x] = x ** 3
   else:
       dict_comprehension[x] = x
print(dict_comprehension) #{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

#18_Convert (7) to lambda function
#def foo(x, y):
#   if x < y:
#      return x
#   else:
#       return y
#print(foo(7, 8))

foo = lambda x, y: x if x < y else y
print(foo(7, 8))

#19*_Convert (8) to regular function
#foo = lambda x, y, z: z if y < x and x > z else y
#print(foo(3,5,7))

def foo(x, y, z):
   if y < x and x > z:
       return z
   else:
       return y
print(foo(3, 5, 7))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))

#21_Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse= True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x + y, list_A, list_B)))

#24_Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))

#25_Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0, range (-10, 10))))

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_2, list_1)))

#TASK_1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))
#TASK_2
lst_d.append(4)
lst_d.append(5)
print(lst_d)

#TASK_3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#TASK_4
result_a=isinstance(int_a, list)
print(result_a)
result_b=isinstance(str_b, str)
print(result_b)
result_c=isinstance(set_c, set)
print(result_c)
result_d=isinstance(lst_d, list)
print(result_d)
result_e=isinstance(dict_e, dict)
print(result_e)

#TASK_5
print('Anna has {} apples and {} peaches.'.format(4, 3))

#TASK6
print('Anna has {1} apples and {0} peaches.'.format(3, 4))

#TASK7
print('Anna has {var} apples and {bar} peaches.'.format(bar=3, var=4))

#TASK8
print('Anna has {var:5} apples and {bar:3} peaches.'.format(bar=3, var=4))

#TASK9
apples = 4
peaches = 3
print(f'Anna has {apples} apples and {peaches} peaches.')

#TASK10
print('Anna has %s apples and %s peaches.' % (apples,peaches))

#TASK11
lst = [("apples", "4"),
       ("peaches", "3")]

dictionary = {}
for tup in lst:

    key = tup[0]
    value = tup[1]

    dictionary[key] = value

print(dictionary)

#TASK12

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [x**2 if x % 2 == 1 else x**4 for x in numbers]
print(new_list)

#TASK13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)

print(lst)

#TASK14

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
dict_new = {x: x**2 for x in numbers_1 if x % 2 ==1}
print(dict_new)

#TASK15

dict_new_1 = {x: x**2 if x % 2 == 1 else x // 0.5 for x in numbers_1}
print (dict_new_1)

#TASK16

d_1 = {}
for x in range(10):
    if x**3 % 4 == 0:
        d_1[x] = x**3
print(d_1)

#TASK17
d = {}
for x in range (10):
    if x**3 % 4 == 0:
        d[x]=x**3
    else:
        d[x]=x

print(d)


#TASK18

new_lam = lambda x, y: x if x < y else y
print(new_lam(1,3))

#TASK19

def foo2 (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print(foo2(1,2,3))

#TASK20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort = sorted(lst_to_sort )
print(lst_to_sort)

#TASK21
lst_to_sort = sorted(lst_to_sort, reverse=True)
print(lst_to_sort)

#TASK22
print(list(map(lambda x: x * 2, lst_to_sort)))

#TASK23
list_A = [2, 3, 4]
list_B = [5, 6, 7]


def raise_list(lst, powers):
    result = []
    for index in range(len(lst)):
        result.append(lst[index] ** powers[index])
    return result

print(raise_list(list_A, list_B))

#TASK24
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))

#TASK25
b = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x < 0, b)))


#TASK26
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

values = list(filter(lambda x: x in list_1, list_2))
print ("Intersection of list_1 and list_2 is: ",values)
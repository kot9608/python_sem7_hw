# '47. У вас есть код, который вы не можете менять
# (так часто бывает, когда код в глубине программы 
#  используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом 
# - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи 
# вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, 
# чтобы transformed_values получился копией values.

# def fib(number):
#     if number in (1, 2):
#         return 1
#     return fib(number - 1) + fib(number - 2)



def transformation(x):
   return x

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
print('tr_v',transormed_values)
print(values)

lstres1=[i for i in values]
values = [1, 2, 3, 4, 5]
print(lstres1)




####################################

def transformation(x):
    return x


values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # или любой другой список
transormed_values = list(map(transformation, values))
print(transormed_values)

transormed_values = list(map(lambda x: x, values))
print(transormed_values)


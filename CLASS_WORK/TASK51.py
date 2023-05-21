# '51. Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# В качестве примера характеристики можно взять проверку четности из лекции, а можно придумать свою.

# Ввод:
# 1 2 3 4 5
# lambda: x%2 == 0
# Вывод:
# False

def same_by(characteristic, objects):
    if list(filter(characteristic, objects))==objects:
        return True
    return False

data = [2, 4, 5]
res = map(int, data) #преобразовали текст в инт в списке
res = list(filter(lambda x: x%2==0, res)) # в список загнали только четные числа
# print(res)
res = list(filter(lambda x:(x,x**2), res))

def char(x):
    return x%2==0

print(same_by(char, data))



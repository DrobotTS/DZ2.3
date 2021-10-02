print('1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число')

from random import randint
value = randint(1, 200)
new_value = (value)/2 if value < 100 else -(value)
print(f"Result: {new_value}, Our number: {value}" )

##############################################

print('2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0')

from random import randint
value = randint(1, 200)
new_value = 1 if value < 100 else 0
print(f"Result: {new_value}, Our number: {value}")

##############################################

print('3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае -False')

from random import randint
value = randint(1, 200)
new_value = True if value < 100 else False
print(f"Result: {new_value}, Our number: {value}")

##############################################

print('4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.')

print("Print something")
my_str = str(input())
for symbol in my_str:
    print(symbol.upper())

##############################################

print('5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.')

print("Print something")
my_str = str(input())
for symbol in my_str:
    print(symbol.lower())

##############################################

print('6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.')

print("Print something")
my_str = str(input())
result = my_str + my_str if len(my_str) < 5 else my_str
print(f"Phrase: {my_str}, Result: {result}")

##############################################

print('7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.')

print("Print something")
my_str = str(input())
result = my_str[::-1] if len(my_str) < 5 else my_str
print(f"Phrase: {my_str}, Result: {result}")
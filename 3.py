'''a = []
maxc = 0
for i in range(5):
    a.append(float(input()))
print(a)
for i in range(len(a)):
    if (a[i] - int(a[i]))> maxc :
        maxc = (a[i] - int(a[i]))
print(maxc)

array = []

# Заполнение массива с клавиатуры
for i in range(5):
    num = float(input("Введите число: "))
    array.append(num)

max_fractional_part = 0

# Поиск наибольшей дробной части
for num in array:
    fractional_part = num - int(num)
    if fractional_part > max_fractional_part:
        max_fractional_part = fractional_part

print("Наибольшая дробная часть:", max_fractional_part)'''


# Глобальная переменная для хранения наибольшей дробной части
max_decimal_part = 0

def find_max_decimal_part():
    global max_decimal_part

# Заполнение массива с клавиатуры
array = []
for i in range(5):
    num = float(input("Введите число: "))
    array.append(num)

# Проверка наибольшей дробной части
decimal_part = num % 1
if decimal_part > max_decimal_part:
    max_decimal_part = decimal_part

print("Наибольшая дробная часть:", max_decimal_part)

# Вызов функции
find_max_decimal_part()

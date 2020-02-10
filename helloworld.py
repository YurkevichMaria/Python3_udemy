# print("hello world")
# print("hello python!")
# print("I wii be a python developer")
# print(3 * 7)
# print(4 ** 3)
# print(29%5)
#
# # Создайте переменные, описывающие автомобиль - модель, цвет, год, количество дверей.
# # Поместите в них значения. Затем поменяйте цвет автомобиля, присвоив ниже в коде
# # новое значение соответствующей переменной. Выведите на экран все значения.
# # При создании имён переменных используйте подходящие по смыслу слова.
# # Воспользуйтесь Google переводчиком, если нужно.
# model_of_car = 'bmw'
# color_of_car = 'black'
# year_of_car ='2018'
# number_of_doors_in_car = 5
# color_of_car = 'pink'
# print (model_of_car, color_of_car, year_of_car, number_of_doors_in_car)
#
#
# # Создайте переменные, в которые будете помещать возраст людей.
# # Также создайте переменную, в которой будет храниться количество людей.
# # Вычислите и выведите на экран средний возраст человека исходя из данных о возрасте этих пятерых людей.
# # Если не знаете формулу вычисления среднего арифметического значения, воспользуйтесь поиском информации в интернете.
# age_of_people = 258
# number_of_people =10
# average_age_of_people = age_of_people / number_of_people
# print(average_age_of_people)
#
#
# # Создайте переменные, поместите в них значения - имя, фамилию и возраст.
# # Выведите на экран следующее предложение: "Hi! My name is имя фамилия, I'm возраст years old."
# # Используйте конкатенацию переменных и строк.
# first_name = 'Maria'
# last_name = 'Yurkevich'
# age = '24'
# space = ' '
# my_string = 'Hi! My name is ' + first_name + space + last_name + ', I\'m' + space + age + space + 'years old.'
# print(my_string)
#
#
# str1 = '\n\n\t\tBaa, baa, black sheep,'
# str2 = '\n\t\tHave you any wool?'
# str3 = '\n\t\tYes sir, yes sir,'
# str4 = '\n\t\tThree bags full'
# str5 = '\n\n\t\tOne for the master,\n\t\tOne for the dame,\n\t\tAnd one for the little boy\n\t\tWho lives down the lane'
# song = str1 + str2 + str3 + str4 + str5 + str1 + str2 + str3 + str4
# print (song)






###########INDEXING AND SLICING

# # Выведите на печать вторую букву l из строки 'Hello Python!'
# # Присвойте строку переменной, затем выведите на печать букву
# my_string = 'Hello Python!'
# print(my_string[3])
#
# # Выведите на печать вторую букву l из строки 'Hello Python!'
# # Сделайте это без присваивания строки переменной, в одной строке кода.
# print('Hello Python!'[3])
#
# # Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
# print('Hello Python!'[0:2])
# print(my_string[0:2])
# print(my_string[:2:1])
#
# # Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа.
# # Выведите новую строку на печать
# my_substring = my_string[6] + 'a' + my_string[len(my_string)-5:len(my_string)-3]
# print(my_substring)



###########STRING PROPERTIES AND METHODS

# # Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации частей строки и отсутствующего символа.
# # Выведите новую строку на печать
# my_string = 'Hello Python!'
# my_substring = my_string[6] + 'a' + my_string[len(my_string)-5:len(my_string)-3]
# print(my_substring)
#
# # Создайте строку 'zzzzzzz' при помощи умножения и выведите её на экран
# multipl_string = 'z' * 7
# print(multipl_string)
#
# # Сделайте все буквы строки из предыдущего вопроса заглавными и выведите её на экран
# print(multipl_string.upper())


###########STRING FORMATTING

# # Создайте таблицу из десятичных дробных чисел с дробной частью разного размера.
# # В таблице должно быть 4 столбца и 2 строки. При помощи метода format()  выведите числа на экран так,
# # чтобы всё число занимало 15 символов, а дробная часть 4 символа
# print('''{0:15.4f},{1:15.4f},{2:15.4f},{3:15.4f},
# {4:15.4f},{5:15.4f},{6:15.4f},{7:15.4f}'''.\
#       format(1123.2458798987,45789.4546465454,32.8789451,1.654646541,\
#              854.6468787,7.46464654,6967897.4687987,232323.5))


###########LIST
# # Создайте список, содержащий разные типы данных
# some_list = [123, 'hello', 98.7485, "Python", 'mylist8']
#
# # Создайте список, извлеките из него элементы с 1 по 3, поместите их в новый список и распечатайте
# new_list = some_list[0:2]
# print(new_list)




###########DICTIONARIES

# # Создайте объект dictionary, содержащий пары ключей и значений, выведите на экран одно значение
# my_dictionary = {'key1': 'value1', 'key2': 150, 'key3': ['v1','v2', 10]}
# print (my_dictionary['key3'])
# print (my_dictionary['key3'][0])
#
# # Создайте объект dictionary, описывающий компьютер
# computer_dict = {
#     'screen': 2,
#     'mouse': 1,
#     'keyboard': 1
# }


###########TUPLES
# Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные.
# Выведите переменные вызвав функцию print() один раз
# computer_tuple = ('Windows 10', '23.8" Full HD 10-point multi-touch', '9 Intel Core i3-9100T')
# operating_system, screen, processor = computer_tuple
# print (operating_system, screen, processor)



###########SETS
# # Создайте множество при помощи функции set() из текста, чтобы получить уникальные символы, содержащиеся в тексте.
# # Присвойте результат переменной. Выведите переменную на экран. Выведите тип значения переменной на экран.
# # При необходимости найдите информацию в интернете
# my_set = set('I will know python very well!')
# print (my_set)
# print (type(my_set))


###########BOOLEANS
# # Создайте 2 переменных, содержащие числовые значения. Сравните их при помощи всех операторов сравнения и
# # выведите результат на экран
# x1 = 24
# x2 = 25
# print(x1 == x2)
# print(x1 != x2)
# print(x1 > x2)
# print(x1 >= x2)
# print(x1 < x2)
# print(x1 <= x2)
#
# # Сравните две одинаковых буквы, но одна из них должна быть заглавной, при помощи операторов сравнения ">" и
# # выведите результат на экран. Выведите на экран ASCII код каждой из букв
# w1, w2 = 'Q', 'q'
# print(w1)
# print(w2)
# print(w1 > w2)
# print(w1, '-', ord(w1), w2, '-', ord(w2))











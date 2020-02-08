print("hello world")
print("hello python!")
print("I wii be a python developer")
print(3 * 7)
print(4 ** 3)
print(29%5)

# Создайте переменные, описывающие автомобиль - модель, цвет, год, количество дверей.
# Поместите в них значения. Затем поменяйте цвет автомобиля, присвоив ниже в коде
# новое значение соответствующей переменной. Выведите на экран все значения.
# При создании имён переменных используйте подходящие по смыслу слова.
# Воспользуйтесь Google переводчиком, если нужно.
model_of_car = 'bmw'
color_of_car = 'black'
year_of_car ='2018'
number_of_doors_in_car = 5
color_of_car = 'pink'
print (model_of_car, color_of_car, year_of_car, number_of_doors_in_car)


# Создайте переменные, в которые будете помещать возраст людей.
# Также создайте переменную, в которой будет храниться количество людей.
# Вычислите и выведите на экран средний возраст человека исходя из данных о возрасте этих пятерых людей.
# Если не знаете формулу вычисления среднего арифметического значения, воспользуйтесь поиском информации в интернете.
age_of_people = 258
number_of_people =10
average_age_of_people = age_of_people / number_of_people
print(average_age_of_people)


# Создайте переменные, поместите в них значения - имя, фамилию и возраст.
# Выведите на экран следующее предложение: "Hi! My name is имя фамилия, I'm возраст years old."
# Используйте конкатенацию переменных и строк.
first_name = 'Maria'
last_name = 'Yurkevich'
age = '24'
space = ' '
my_string = 'Hi! My name is ' + first_name + space + last_name + ', I\'m' + space + age + space + 'years old.'
print(my_string)


str1 = '\n\n\t\tBaa, baa, black sheep,'
str2 = '\n\t\tHave you any wool?'
str3 = '\n\t\tYes sir, yes sir,'
str4 = '\n\t\tThree bags full'
str5 = '\n\n\t\tOne for the master,\n\t\tOne for the dame,\n\t\tAnd one for the little boy\n\t\tWho lives down the lane'
song = str1 + str2 + str3 + str4 + str5 + str1 + str2 + str3 + str4
print (song)

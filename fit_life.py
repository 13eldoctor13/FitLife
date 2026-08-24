# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в user_age (не забудь преобразовать в число)
print('Вас приветствует Fit Life!')
user_name = input('Как Вас зовут? ')
user_age = int(input('Сколько Вам лет? '))
def age_compare():
    pass


# 2. Сбор данных
def height_compare():
    pass


# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах) и сохрани в user_height (тип float)
user_weight = float(input('Сколько Вы весите?(в кг.) '))
user_height = float(input('Ваш рост?(в метрах) '))

    
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
def bmi_result():
    if bmi <= 18.5:
        return 'У Вас недостаточный вес'
    elif 18.5 < bmi <= 24.9:
        return 'У Вас нормальный вес'
    elif 24.9 < bmi <= 29.9:
        return 'У Вас предожирение'
    elif 29.9 < bmi <= 34.9:
        return 'У Вас ожирение 1ой степени'
    elif 34.9 < bmi <= 39.9:
        return 'У Вас ожирение 2ой степени'
    else:
        return 'У Вас тяжолое ожирение'    
   

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_neededVb
water_needed = (user_weight * 30) / 1000

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
def get_year_word(user_age):
    if user_age % 100 in [11, 12, 13, 14]:
        return 'лет'
    age = user_age % 10
    if age == 1:
        return 'год'
    elif age in [2, 3, 4]:
        return 'года'
    else:
        return 'лет'


print(f'Привет, {user_name}!')
print(f'В {user_age} {get_year_word(user_age)}:')
print(f'Твой ИМТ: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_needed} л.')
print("Расчет окончен. Будьте здоровы!")
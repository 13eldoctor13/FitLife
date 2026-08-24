# Проект FitLife - MVP версия 1.0
# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в user_age (не забудь преобразовать в число)
print('Вас приветствует Fit Life!')
user_name = input('Как Вас зовут? ').strip()
if len(user_name) > 0:
    print(f'Здравствуй {user_name}!')
else:
    print('Введите имя')
    user_name = input('Как Вас зовут? ').strip()

user_age = input('Сколько Вам лет? ').strip()
if len(user_age) > 0:
    age_input = int(user_age)
    print('Прекрасный возраст!')
else:
    print('Введите Ваш возраст')
    user_age = input('Сколько Вам лет? ').strip()

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах) и сохрани в user_height (тип float)
user_weight = input('Сколько Вы весите?(в кг.) ')
if len(user_weight) > 0:
    weight_input = float(user_weight)
else:
    print('Проверте правильность ввода (в кг.)')
    user_weight = input('Сколько Вы весите?(в кг.) ')
user_height = input('Ваш рост?(в метрах) ')
if len(user_height) > 0:
    height_input = float(user_height)
    if 0 < height_input <= 3:
        height_input = float(user_height)
    else:
        print('Проверте правильность ввода(Пример: 1.83)')
        user_height = input('Ваш рост?(в метрах) ')
else:
    user_height = input('Ваш рост?(в метрах) ')
    
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
if user_age >= 18:
    if bmi <= 18.5:
        print ('У Вас недостаточный вес')
    elif 18.5 < bmi <= 24.9:
        print ('У Вас нормальный вес')
    elif 24.9 < bmi <= 29.9:
        print ('У Вас предожирение')
    elif 29.9 < bmi <= 34.9:
        print ('У Вас ожирение 1ой степени')
    elif 34.9 < bmi <= 39.9:
        print ('У Вас ожирение 2ой степени')
    else:
        print ('У Вас тяжолое ожирение')
else:
    

#Код заимствован с https://lit-baby.ru Для детей до 18 лет.
def calculate_child_bmi(weight_kg, height_m):                                     
    """Рассчитывает стандартный индекс массы тела."""
    if height_m <= 0:
        raise ValueError("Рост должен быть больше нуля.")
    return round(weight_kg / (height_m ** 2), 1)

def interpret_child_bmi(bmi, age_years):
    """
    Упрощенная интерпретация ИМТ для детей и подростков (10-16 лет).
    В реальной медицине используются точные таблицы ВОЗ с шагом в 1 месяц.
    """
    # Границы нормы: (дефицит_массы, ожирение)
    # Данные усреднены для демонстрации логики кода
    percentile_grid = {
        10: (14.0, 22.5),
        12: (14.5, 24.5),
        14: (15.5, 26.0),
        16: (16.5, 28.0),
        18: (18.5, 25.0)  # Границы для переходного возраста
    }
    
    # Находим ближайший по возрасту порог для сравнения
    closest_age = min(percentile_grid.keys(), key=lambda x: abs(x - age_years))
    underweight_limit, obesity_limit = percentile_grid[closest_age]
    
    if bmi < underweight_limit:
        return f"Дефицит массы тела (норма для {closest_age} лет: > {underweight_limit})"
    elif bmi > obesity_limit:
        return f"Избыточный вес / Ожирение (норма для {closest_age} лет: < {obesity_limit})"
    else:
        return "Нормальный вес"

# --- Пример использования программы ---
try:
    child_age = 12       # Возраст ребенка (лет)
    child_weight = 34.0  # Вес в килограммах
    child_height = 1.45  # Рост в метрах

    # Расчет
    bmi_result = calculate_child_bmi(child_weight, child_height)
    verdict = interpret_child_bmi(bmi_result, child_age)

    # Вывод результатов
    print(f"Возраст ребенка: {child_age} лет")
    print(f"Рассчитанный ИМТ: {bmi_result}")
    print(f"Заключение: {verdict}")

except ValueError as e:
    print(f"Ошибка ввода данных: {e}") 



       
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
print(f'Твой ИМТ: {round(bmi_calc(), 1)}')
print(f'Рекомендуемая норма воды: {water_needed} л.')
print("Расчет окончен. Будьте здоровы!")
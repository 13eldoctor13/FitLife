# Проект FitLife - MVP версия 1.0

ML_PER_KG = 30
WATER_L = 1000


print('Вас приветствует Fit Life!')

user_name = input('Как Вас зовут? ').strip()

if len(user_name) > 0:
    print(f'Здравствуй {user_name}!')
else:
    print('Как Вас зовут?')

try:
    user_age = int(input('Сколько Вам лет? ').strip())
    print('Прекрасный возраст для заботы о здоровье!')
except ValueError:
    print('Сколько Вам лет?')

user_weight = input('Сколько Вы весите?(в кг.) ').strip()

if user_weight.replace('.', '', 1).isdigit():
    weight_input = float(user_weight)
else:
    print('Проверьте правильность ввода (55.5 кг.)')

user_height = input('Ваш рост?(в метрах) ').strip()

if user_height.replace('.', '', 1).isdigit():
    height_input = float(user_height)
else:
    print('Проверьте правильность ввода(Пример: 1.83)')


bmi = weight_input / (height_input ** 2)

water_needed = (weight_input * ML_PER_KG) / WATER_L


print(f'Привет, {user_name}!')
print(f'В {user_age}')
print(f'Твой ИМТ: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_needed} л.')
print("Расчет окончен. Будьте здоровы!")

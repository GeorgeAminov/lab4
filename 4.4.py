color1=input("Введите первый цвет: ").lower()
color2=input("Введите второй цвет: ").lower()
colors=("красный", "синий", "жёлтый")
if color1 not in colors or color2 not in colors:
    print("Введён не корректный цвет")
elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("Получился фиолетовый")
elif (color1 == "красный" and color2 == "жёлтый") or (color1 == "жёлтый" and color2 == "красный"):
    print("Получился оранжевый")
elif (color1 == "синий" and color2 == "жёлтый") or (color1 == "жёлтый" and color2 == "синий"):
    print("Получился зелёный")
elif color1 == color2:
    print("Получился", color1)
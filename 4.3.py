yr=int(input("Введите год: "))
if yr % 4 == 0 and yr % 100 != 0:
    print("Год", yr, "- високосный")
elif yr % 400 == 0:
    print("Год", yr, "- високосный")
else:
    print("Этот год не високосный")

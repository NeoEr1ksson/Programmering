print("rabat på bussbiljetterna")

age = input()
age = int(age)

if age < 20:
    print("junior 21kr")

elif age >= 20 and age < 65:
    print("vuxan 32kr")

elif age >=65:
    print(" senior 21kr")
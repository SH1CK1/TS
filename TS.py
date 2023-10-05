from math import sqrt
name = []
distance = []
data = [
    [61.02613, 69.09714, 'Аэропорт Ханты-Мансийска'],
    [59.65583, 74.63, "Заповедник 'Югорский' ('Юганский')"],
    [61.36028, 63.54661, "Заповедник 'Малая Сосьва'"],
    [60.98024, 69.00779, "Ханты-Мансийский археопарк"],
    [60.99522, 69.03862, "Самаровский Чугас"],
    [60.95103, 76.81137, "Сибирские Увалы"],
    [60.95833, 68.55, "Луговское местонахождение мамонтовой фауны"],
    [61.25306, 73.18806, "Урочище 'Барсова Гора'"],
    [62.75958, 65.47021, "Городище Шеркалы-1"],
    [60.08895, 65.01394, "Этностойбище Силава"],
    [61.08982, 69.46024, "Шапшинские кедровники"]
]

x_1 = data[0][0]
y_1 = data[0][1]
name.append(data[0][2])
del data[0]
while len(data) != 0:
    for i in range(0, len(data)):
        distance.append(sqrt((data[i][0] - x_1)**2 + (data[i][1] - y_1)**2))
    name.append(data[distance.index(min(distance))][2])
    x_1 = data[distance.index(min(distance))][0]
    y_1 = data[distance.index(min(distance))][1]
    del data[distance.index(min(distance))]
    distance.clear()

for i in range(len(name)):
    print(str(i + 1) +') ' + name[i])
print(str(len(name) + 1) +')' + "Аэропорт Ханты-Мансийска")
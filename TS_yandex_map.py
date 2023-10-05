import requests
import json
api_key = "f10b1d0e-efc4-4939-a39c-913c95f223c5"
name = []
distance = []
data = [[61.02613, 69.09714, "Аэоропорт"],[59.65583, 74.63, "Заповедник 'Югорский' ('Юганский')"],[61.36028, 63.54661, "Заповедник 'Малая Сосьва'"],[60.98024, 69.00779, "Ханты-Мансийский археопарк"],[60.99522, 69.03862, "Самаровский Чугас"],[60.95103, 76.81137, "Сибирские Увалы"],[60.95833, 68.55, "Луговское местонахождение мамонтовой фауны"],[61.25306, 73.18806, "Урочище 'Барсова Гора'"],[62.75958, 65.47021, "Городище Шеркалы-1"],[60.08895, 65.01394, "Этностойбище Силава"],[61.08982, 69.46024, "Шапшинские кедровники"]]
x, y = float(data[0][0]), float(data[0][1])
name.append(data[0][2])
del data[0]
while len(data) != 0:
    start_point = str(x) + ' ' + str(y)
    for i in range(0, len(data)):
        end_point = str(data[i][0]) + ' ' + str(data[i][1])
        url = f"https://api-maps.yandex.ru/services/route/2.0/json?apikey={api_key}&lang=ru_RU&origin={start_point}&destination={end_point}&routing_mode=auto"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            S = data["route"]["distance"]
            distance.append(S / 1000)
    name.append(data[distance.index(min(distance))][2])
    x_1 = data[distance.index(min(distance))][0]
    y_1 = data[distance.index(min(distance))][1]
    del data[distance.index(min(distance))]
    distance.clear()

for i in range(len(name)):
    print(str(i + 1) +') ' + name[i])
print(str(len(name) + 1) +')' + "Аэропорт Ханты-Мансийска")


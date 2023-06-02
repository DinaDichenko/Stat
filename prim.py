import csv
import random
import numpy as np

# Открываем CSV-файл для записи
with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Записываем заголовки столбцов
    writer.writerow(['Площадь дома (кв.м)', 'Количество комнат', 'Удаленность от центра', 'Цена дома'])
    
    # Генерируем 100 элементов данных
    for _ in np.arange(100):
        # Генерируем случайные значения признаков
        area = random.randint(80, 300)
        rooms = random.randint(1, 5)
        distance = random.randint(1, 20)
        
        # Вычисляем цену дома на основе указанных зависимостей
        price = area * 2000
        if distance > 10:
            price += price * 0.1
        
        # Записываем сгенерированные данные в CSV-файл
        writer.writerow([area, rooms, distance, price])

print("CSV-файл успешно создан!")

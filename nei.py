import numpy as np
import csv

# Входные данные
data = []
with open('dataset.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Пропускаем заголовок
    for row in csv_reader:
        data.append([float(value) for value in row])

data = np.array(data)
X = data[:, :-1] # Признаки
y = data[:, -1] # Целевая переменная

# Разделение данных на обучающую и тестовую выборки
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Нормализация данных (если необходимо)
#X_train_norm = (X_train - X_train.mean(axis=0)) / X_train.std(axis=0)
#X_test_norm = (X_test - X_train.mean(axis=0)) / X_train.std(axis=0)

# Добавление столбца единиц для учета свободного члена
X_train = np.concatenate((np.ones((X_train.shape[0], 1)), X_train), axis=1)
X_test = np.concatenate((np.ones((X_test.shape[0], 1)), X_test), axis=1)

# Определение модели и обучение
theta = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

# Предсказание цены дома на тестовых данных
y_pred = X_test @ theta

# Оценка производительности модели
mse = np.mean((y_test - y_pred) ** 2)
r2 = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - y_test.mean()) ** 2))

print("Среднеквадратичная ошибка (MSE):", mse)
print("Коэффициент детерминации (R^2):", r2)


# Новая ситуация
new_data = np.array([[160, 3, 5]])

# Добавление столбца единиц
new_data = np.concatenate((np.ones((new_data.shape[0], 1)), new_data), axis=1)

# Предсказание цены дома в новой ситуации
new_prediction = new_data @ theta

print("Предсказанная цена дома в новой ситуации:", new_prediction)
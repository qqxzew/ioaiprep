# Операция	Что делает
# a.reshape(2, 3)	Меняет форму на (2, 3)
# a.reshape(-1, 1)	Делает столбец
# a.reshape(1, -1)	Делает строку
# a.T	Транспонирует
# a.ravel()	Превращает в 1D
# np.concatenate(...)	Соединяет по существующей оси
# np.stack(...)	Создаёт новую ось
# np.vstack(...)	Складывает вертикально
# np.hstack(...)	Соединяет горизонтально
# a[:, None]	Добавляет ось в конце для 1D
# a[None, :]	Добавляет ось в начале для 1D
# A @ B	Матричное умножение

import numpy as np

a =np.random.randint(0, 10 , size=(10,))
b = np.random.randint(0, 10, size=(10,))
c = np.random.randint(0, 10, size=(10,))
print(a, b, c)
b = np.stack((a, b, c), axis=1) # Создаёт новую ось
a_back, b_back, c_back = b.T
print(a_back, b_back, c_back)


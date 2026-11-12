# # import numpy as np, time
# # a = np.random.default_rng(0).random(1_000_000)

# # t = time.perf_counter()
# # s = 0.0
# # for x in a:
# #     s += x * x
# # print("for:  ", time.perf_counter() - t)

# # t = time.perf_counter()
# # s2 = (a * a).sum()
# # print("numpy:", time.perf_counter() - t)

# 3. Как подогнать форму
# Инструмент	Что делает
# x[:, None]	(n,) → (n,1), то есть столбец. То же самое x[:, np.newaxis] или x.reshape(-1, 1)
# x[None, :]	(n,) → (1,n), то есть строка
# keepdims=True	M.mean(axis=1) даёт (3,), а с keepdims=True даёт (3,1). Такая форма сразу готова для broadcasting обратно с M. Вот зачем keepdims был в 1.3
# None в любом месте	X[:, :, None] добавляет ось в конец
import numpy as np

# #37
# Z = np.zeros((5, 5))
# Z += np.arange(5)
# print(Z)

#47
# a = 1/(x[:, None] - y[None, :])
#52
# a = np.random.randint(100, size=(100, 2))
# print(a)
# x = a[:, 0]
# y = a[:, 1]
# b = np.sqrt((x[:, None] - x[None, :]) ** 2 + (y[:, None] - y[None, :]) ** 2)
#58
# a = np.random.randint(10, size=(5, 5))
# b = np.mean(a, axis=1, keepdims=True)
# print(a)
# print(b)
# c = a - b
# print(c)
#71
# a = np.random.randint(10, size=(5, 5, 3))
# b = np.random.randint(10, size=(5, 5))
# b = b.reshape(5, 5, 1)
# print(a*b)
#own
a = np.random.uniform(-1, 1, size=(1000, 2))
x = a[:, 0]
y = a[:, 1]
b = np.sqrt((x) ** 2 + (y) ** 2)
c = np.mean(b<=1)
print(c*4)

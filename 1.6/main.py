# rng.uniform(low, high, size)	дробные числа, все значения в диапазоне одинаково вероятны	rng.uniform(-1, 1, 1000) — точки из задачи про π
# rng.normal(loc, scale, size)	дробные числа по колоколу: большинство около loc, а scale — разброс (стандартное отклонение)	рост людей: rng.normal(175, 7, 1000)
# rng.integers(low, high, size)	целые числа, high не включается, как в range	кубик: rng.integers(1, 7, 10)
# rng.choice(варианты, size, p=...)	выбор из списка, p — вероятности вариантов	rng.choice(["win", "loss"], 10, p=[0.7, 0.3])

# Про normal надо помнить одно: примерно 68% значений попадают в диапазон loc ± scale. Для роста это 168–182 см, а вот 200+ встретится очень редко.

# Про choice: по умолчанию значения могут повторяться. С replace=False каждый вариант выпадет максимум один раз.
import numpy as np
# a = np.arange(10).astype(float)
# a[2] = np.nan
# print(a)
# print(np.mean(a))
# print(np.nanmean(a))
#57
a = np.zeros(10*10)
print(a)
rng = np.random.default_rng(0)
b = rng.choice(99, 3, replace=False)
print(b)
c = a
c[b] = 1
c = c.reshape(10, 10)
print(c)
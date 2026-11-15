
import pandas as pd

# df.loc[
#     (УСЛОВИЕ_1) & (УСЛОВИЕ_2),
#     ["столбец1", "столбец2"]
# ].sort_values("столбец1")
# в своём датасете найди строки, где категория X и признак выше среднего, и топ-10 по целевой колонке.
df = pd.read_csv("cooking.csv")
a = df.loc[(df['cooking_type'] == 'boiling'), ['cooking_type', 'cooking_time', 'power']]
print(a)
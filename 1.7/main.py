import pandas as pd
# pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
#               'Sue': ['Pretty good.', 'Bland.']},
#              index=['Product A', 'Product B'])


# a = pd.read_csv("cooking.csv")
# print(a.shape)
# print(a.head(2))
# pd.save_c
# Команда	Что делает
# pd.read_csv("data.csv")	Загружает CSV-файл в DataFrame
# df.head()	Показывает первые 5 строк
# df.info()	Структура таблицы, типы и пропуски
# df.describe()	Статистика: среднее, min, max и др.
# df.dtypes	Тип каждого столбца
# df.to_csv("new.csv", index=False)	Сохраняет таблицу в CSV
# df["age"]	Возвращает столбец как Series
df = pd.read_csv("cooking.csv")
def quick_look(df):
    print(df.shape)
    print(df.info)
    print(df.describe())
    print(df.dtypes)
    print(df.sample(3))
    print(df.isna().mean() * 100)

quick_look(df)
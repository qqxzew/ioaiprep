import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cooking.csv")

# df.hist(bins=30, figsize=(10, 8))      # все числовые колонки сразу
# plt.show()
# sns.countplot(x="cooking_type", data=df)   # для категорий hist не работает, нужен countplot
# plt.show()
# for col in ["weight", "ingridients", "power"]:
#     sns.scatterplot(x=col, y="cooking_time", data=df)
#     plt.show()
# sns.boxplot(x="cooking_type", y="cooking_time", data=df)
# plt.show()
# df["inv_power"] = 1 / df["power"]
# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
# plt.show()
df.hist(bins=30)                                    # распределения всех колонок
sns.scatterplot(x="признак", y="цель", data=df)     # связь признака с целью
sns.boxplot(x="категория", y="цель", data=df)       # цель по категориям
sns.heatmap(df.corr(numeric_only=True), annot=True) # корреляции
plt.show()

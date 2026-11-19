import numpy as np
import pandas as pd

# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# df = pd.DataFrame(data, index=labels)

# #15 
# # df = df.groupby("animal")["age"].mean()
# #17
# # df = df["animal"].value_counts()
# #21
# # df = df.pivot_table(index="animal", columns="visits",
# #                     values="age", aggfunc="mean")
#27
# df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
#                    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

# # df = df.sort_values("vals", ascending=False).groupby("grps").head(2)
#28
# df = pd.DataFrame(np.random.RandomState(8765).randint(1, 101, size=(100, 2)), columns=["A", "B"])
# bins = np.arange(0, len(df) + 10, 10)
# df['group'] = pd.cut(np.arange(len(df)), bins=bins, right=False)
# df = df.groupby("group")["B"].sum()
#31
df = pd.DataFrame({"vals": np.random.RandomState(31).randint(-30, 30, size=15),
                   "grps": np.random.RandomState(31).choice(["A", "B"], 15)})
pos = df["vals"].where(df["vals"] >= 0)
df["group_mean"] = pos.groupby(df["grps"]).transform("mean")
df["patched_vals"] =  np.where(df["vals"]>=0, df["vals"], df["group_mean"])
print(df)
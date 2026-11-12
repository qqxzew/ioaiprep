import numpy as np
import pandas as pd

rng = np.random.default_rng(17)
#first column, weight

weight = rng.normal(500, 150, 1000)
#second column, count of ingidients
ingridients = rng.integers(3, 15, 1000)
#third collumn, power
power = rng.integers(1, 10, 1000)
#cooking type
cooking_type = rng.choice(["baking", "frying", "boiling"], 1000, p=[0.01, 0.69, 0.30])

#additional categories
bonus = np.where(cooking_type == "baking", 20, 0) + np.where(cooking_type == "boiling", 10, 0)
noise = rng.normal(0, 5, 1000)


COOKING_TIME = 0.05 * weight + 2 * ingridients + 60/power + bonus + noise

#nan for 5% of weight
n_missing = int(weight.size * 0.05)
indices = rng.choice(weight.size, size=n_missing, replace=False)
weight[indices] = np.nan

pd.DataFrame({
    "weight": weight,
    "ingridients": ingridients,
    "power": power,
    "cooking_type": cooking_type,
    "cooking_time": COOKING_TIME
}).to_csv("project1/cooking.csv", index=False)  
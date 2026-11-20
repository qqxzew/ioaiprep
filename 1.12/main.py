# import numpy as np
import pandas as pd

# rng = np.random.default_rng(17)

# menu = pd.DataFrame({
#     "dish":   ["borsch", "varenyky", "pizza", "burger", "pancakes", "soup"],
#     "method": ["boiling", "boiling", "baking", "frying", "frying", "boiling"],
#     "price":  [120, 150, 220, 190, 90, 80],
# })
# menu.to_csv("menu.csv", index=False)

# def make_orders(start, cols):
#     rows = []
#     for day in range(60):
#         date = pd.Timestamp(start) + pd.Timedelta(days=day)
#         n = rng.poisson(25 + day * 0.3 + (15 if date.dayofweek >= 5 else 0))
#         for _ in range(n):
#             hour = rng.choice([11, 12, 13, 14, 17, 18, 19, 20], p=[.08, .2, .2, .07, .1, .15, .14, .06])
#             t = date + pd.Timedelta(hours=int(hour), minutes=int(rng.integers(0, 60)))
#             rows.append([t.strftime("%d.%m.%Y %H:%M"), rng.choice(menu["dish"]), rng.integers(1, 4)])
#     return pd.DataFrame(rows, columns=cols)

# make_orders("2026-09-01", ["time", "dish", "qty"]).to_csv("/plzen.csv", index=False)
# make_orders("2026-09-01", ["Cas", "Jidlo", "Pocet"]).to_csv("/praha.csv", index=False)
plzen = pd.read_csv("/home/qqxzew/Projects/ioaiprep/1.12/plzen.csv")
praha = pd.read_csv("/home/qqxzew/Projects/ioaiprep/1.12/praha.csv")
menu = pd.read_csv("/home/qqxzew/Projects/ioaiprep/1.12/menu.csv")
praha = praha.rename(columns={"Cas": "time", "Jidlo": "dish", "Pocet": "qty"})
cities = pd.concat([plzen, praha], ignore_index=True)
cities = pd.merge(cities, menu, on="dish", how="left")
cities["revenue"] = cities["qty"] * cities["price"]
cities["time"] = pd.to_datetime(cities["time"], format="%d.%m.%Y %H:%M")
cities["hours"] = cities["time"].dt.hour # количество заказов по часам
cities["time"].dt.dayofweek     # день недели числом: 0 = понедельник, 6 = воскресенье
cities["time"].dt.day_name()    # день недели словом: "Monday"
cities["time"].dt.date          # только дата без времени
daily = cities.set_index("time")["revenue"].resample("D").sum()
import matplotlib.pyplot as plt
daily.plot()
daily.rolling(7).mean().plot()
plt.show()

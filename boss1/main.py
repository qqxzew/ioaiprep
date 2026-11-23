import pandas as pd
import numpy as np

listings = pd.read_csv('project_final1/listings.csv')
listings = listings.drop_duplicates()
listings["brand"] = listings["brand"].str.strip()
listings["brand"] = listings["brand"].str.lower()

listings["price"] = listings["price"].astype(str)
listings["price"] = listings["price"].str.replace("Kč", "")
listings["price"] = listings["price"].str.replace(" ", "")
listings["price"] = pd.to_numeric(listings["price"], errors='coerce')
listings = listings.dropna(subset=["price"])
listings = listings[listings["price"].between(1000, 200000)]
listings["price"] = listings["price"].astype(int)

listings["ram"] = listings["ram"].str.lower()
listings["ram"] = listings["ram"].str.replace("gb", "")
listings["ram"] = listings["ram"].str.replace(" ", "")
listings["ram"] = pd.to_numeric(listings["ram"], errors='coerce')
listings = listings.dropna(subset=["ram"])
listings["ram"] = listings["ram"].astype(int)

listings["ssd_gb"] = listings["ssd_gb"].fillna(listings["ssd_gb"].median())
listings["ssd_gb"] = listings["ssd_gb"].astype(int)

listings["condition_code"] = listings["condition"].map({"poškozený": 0, "použitý": 1, "zánovní": 2, "nový": 3})

sellers = pd.read_csv('project_final1/sellers.csv')
listings = listings.merge(sellers, on='seller_id', how='left')

listings["rating_missing"] = listings["rating"].isna().astype(int)
listings["rating"] = listings["rating"].fillna(listings["rating"].mean())

listings["age_years"] = 2026 - listings["year"]
listings["posted"] = pd.to_datetime(listings["posted"], format="%d.%m.%Y")
listings["days_listed"] = (pd.Timestamp("2026-11-23") - listings["posted"]).dt.days

listings = listings.rename(columns={"ram": "ram_gb", "rating": "seller_rating"})
cols = ["listing_id", "brand", "price", "ram_gb", "ssd_gb", "condition_code", "city", "seller_rating",
        "rating_missing", "age_years", "days_listed"]
listings = listings[cols].sort_values("listing_id")
listings.to_csv('project_final1/clean.csv', index=False)

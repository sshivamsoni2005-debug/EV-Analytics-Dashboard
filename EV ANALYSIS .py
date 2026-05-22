import pandas as pd
import matplotlib.pyplot as plt

# =========================
# STEP 1: LOAD DATA
# =========================

car = pd.read_csv(r"c:\Users\LENOVO\Downloads\ev_car_India_dataset.csv")

sales = pd.read_csv(
    r"c:\Users\LENOVO\Downloads\ev_sales_by_makers_and_cat_15-24 (1).csv",
    engine="python",
    sep=None,
    encoding="latin1",
    on_bad_lines="skip"
)

final_data = pd.read_csv(
    r"c:\Users\LENOVO\Downloads\final_dataset.csv",
    engine="python",
    sep=None,
    encoding="latin1",
    on_bad_lines="skip"
)

# =========================
# STEP 2: CLEAN DATA
# =========================

car.columns = car.columns.str.strip().str.lower().str.replace(" ", "_")
sales.columns = sales.columns.str.strip().str.lower().str.replace(" ", "_")
final_data.columns = final_data.columns.str.strip().str.lower().str.replace(" ", "_")

# =========================
# STEP 3: SALES ANALYSIS
# =========================

sales_clean = sales.drop(columns=['2015','2016','2017','2018','2019'], errors='ignore')

sales_yearly = sales_clean[["2020","2021","2022","2023","2024"]].sum()

print("Yearly Sales:")
print(sales_yearly)

plt.figure()
plt.plot(sales_yearly.index, sales_yearly.values, marker='o')
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.title("EV Sales Growth (2020–2024)")
plt.grid()
plt.show()

# SAVE CLEANED SALES
sales.to_csv("sales_cleaned.csv", index=False)

# =========================
# STEP 4: CAR DATA ANALYSIS
# =========================

car = car.dropna(subset=["brand", "range"])

max_range = car.loc[car.groupby("brand")["range"].idxmax()]
max_range = max_range.sort_values(by="range", ascending=False)

print("\nTop EV Cars by Range:")
print(max_range[["brand", "model", "price", "range"]].head(5))

plt.figure()
plt.bar(max_range["brand"], max_range["range"])
plt.xticks(rotation=45)
plt.xlabel("Brand")
plt.ylabel("Max Range")
plt.title("Best Range by Brand")
plt.grid()
plt.show()

# SAVE CLEANED CAR DATA
car.to_csv("car_cleaned.csv", index=False)

# =========================
# STEP 5: CHARGING STATIONS ANALYSIS
# =========================

final_data = final_data.fillna(0)

drop_cols = [
    "two_wheeler","s.no","three_wheeler","four_wheeler",
    "goods_vehicles","public_service_vehicle",
    "special_category_vehicles","ambulance/hearses",
    "construction_equipment_vehicle","other","grand_total"
]

final_data = final_data.drop(columns=drop_cols, errors='ignore')

final_data = final_data.sort_values("total-charging-stations", ascending=False)

top10_states = final_data.head(10)

print("\nTop 10 States by Charging Stations:")
print(top10_states[["state_name","total-charging-stations"]])

plt.figure(figsize=(12,6))
plt.bar(top10_states["state_name"], top10_states["total-charging-stations"])
plt.xticks(rotation=45, ha='right')
plt.xlabel("State")
plt.ylabel("Charging Stations")
plt.title("Top 10 States by Charging Infrastructure")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# SAVE CLEANED FINAL DATA
final_data.to_csv("final_cleaned.csv", index=False)
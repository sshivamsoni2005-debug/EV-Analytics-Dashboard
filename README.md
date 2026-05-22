# EV Market Analysis Dashboard

## Project Overview

This is an end-to-end Electric Vehicle data analysis project created using Excel, Python, Pandas, Matplotlib, and Power BI.

The dataset was downloaded from Kaggle and contained multiple EV-related files. The project focuses on analyzing EV market performance, EV sales growth, brand-wise performance, model comparison, price and range analysis, and state-wise charging station infrastructure.

The final output is an interactive Power BI dashboard that provides meaningful insights into the Indian EV market.

---

## Tools & Technologies Used

- Excel
- Python
- Pandas
- Matplotlib
- Power BI
- Kaggle Dataset

---

## Project Workflow

1. Downloaded EV datasets from Kaggle.
2. Imported the dataset files into Python.
3. Cleaned and transformed the data using Pandas.
4. Removed unnecessary columns and handled missing values.
5. Performed EV sales, car model, brand, range, price, and charging station analysis.
6. Created basic visualizations using Matplotlib.
7. Built interactive dashboards in Power BI.
8. Designed KPI cards, slicers, bar charts, scatter charts, map visuals, and market share charts.

---

## Business Questions Answered

This project answers the following key business questions:

1. How has EV sales growth changed from 2020 to 2024?
2. Which EV brands have the highest market share?
3. Which EV models offer the best range?
4. Which brands provide higher power and battery capacity?
5. What is the relationship between EV price and driving range?
6. Which states have the highest number of charging stations?
7. Is EV charging infrastructure growing equally across all states?
8. Which states need more EV charging infrastructure?
9. Which EV models are positioned as premium vehicles based on price, power, and range?
10. How can EV market data help understand future EV adoption trends?

---

## Dashboard Preview

### EV Market Analysis Dashboard

![EV Market Analysis Dashboard](images/ev_market_anal)

### EV Sales & Charging Station Dashboard

![EV Sales Charging Dashboard](images/ev_sales_charging_dashboard.png)

---

## Key Insights

- Total EV sales reached approximately 3M in the analyzed period.
- EV sales showed strong growth from 2020 to 2024.
- The dashboard indicates EV sales grew by around 400% from 2020 to 2024.
- Maharashtra has the highest number of charging stations.
- Tamil Nadu, Delhi, Karnataka, and Kerala are also among the top states for charging infrastructure.
- The average EV price is around ₹28.77 lakh.
- The maximum EV range in the dataset is 663 KM.
- The maximum power value is 503 kW.
- The average battery capacity is around 52.68.
- MG and Tata hold a strong share in the EV market.
- Higher range EVs generally have a higher average price.
- Charging infrastructure is not equally distributed across all states.

---

## Dashboard Features

- Brand filter
- Model filter
- State filter
- Range filter
- Price filter
- KPI cards
- EV sales trend chart
- Price and range analysis
- Top states by charging stations
- Charging station map
- Market share by brand
- Model-wise range comparison
- Brand-wise average price analysis

---

## Files Included

```text
EV-Market-Analysis-Dashboard/
│
├── data/
│   ├── raw/
│   │   ├── ev_car_India_dataset.csv
│   │   ├── ev_sales_by_makers_and_cat_15-24.csv
│   │   └── final_dataset.csv
│   │
│   └── cleaned/
│       ├── sales_cleaned.csv
│       ├── car_cleaned.csv
│       └── final_cleaned.csv
│
├── python/
│   └── EV_ANALYSIS.py
│
├── powerbi/
│   └── EV_Dashboard.pbix
│
├── images/
│   ├── ev_market_analysis_dashboard.png
│   └── ev_sales_charging_dashboard.png
│
└── README.md

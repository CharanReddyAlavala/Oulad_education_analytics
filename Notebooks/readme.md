# 📊 Student Performance Data Pipeline (Databricks)

## 🚀 Overview

This project implements an **end-to-end data pipeline using Databricks** following the **Medallion Architecture (Bronze → Silver → Gold)**.

The pipeline processes student data to generate **business insights and dashboards** such as:

* Course performance
* Pass & dropout rates
* Risk analysis
* Top-performing students

---

## 🏗️ Architecture

```
Bronze Layer → Silver Layer → Gold Layer → Dashboard
```

### 🥉 Bronze Layer (`bronze_layer.ipynb`)

* Ingests raw CSV data
* Stores data in Delta tables
* No transformations (raw format)

### 🥈 Silver Layer (`silver_layer.ipynb`)

* Cleans and transforms data
* Handles nulls and duplicates
* Joins multiple datasets
* Creates enriched dataset:
  `student_enriched`

### 🥇 Gold Layer (`gold_layer.ipynb`)

* Creates business-level aggregated tables:

  * `course_performance`
  * `pass_rate`
  * `dropout_rate`
  * `risk_distribution`
  * `top_students`
  * `at_risk_students`

---

## 📂 Project Structure

```
Notebooks/
│
├── bronze_layer.ipynb     # Raw data ingestion
├── silver_layer.ipynb     # Data cleaning & transformation
├── gold_layer.ipynb       # Business metrics & KPIs
└── readme.md              # Project documentation
```

---

## 📊 Key Features

✔ Medallion Architecture implementation
✔ End-to-end data pipeline
✔ Delta Lake storage
✔ Data cleaning & transformation
✔ Business KPI generation
✔ Dashboard-ready datasets

---

## 📈 KPIs Generated (Gold Layer)

| KPI                | Description                |
| ------------------ | -------------------------- |
| Course Performance | Avg score, total students  |
| Pass Rate          | % of students passed       |
| Dropout Rate       | % of students withdrawn    |
| Risk Distribution  | High vs Low risk students  |
| Top Students       | Top 5 per course           |
| At Risk Students   | Students needing attention |

---

## 📊 Dashboard Insights

The Gold layer supports dashboards with:

* KPI cards (Total Students, Avg Score, Pass %, Dropout %)
* Bar charts (Course performance)
* Stacked charts (Pass vs Dropout)
* Pie chart (Risk distribution)
* Tables (Top students, At-risk students)

---

## 🛠️ Technologies Used

* Databricks (SQL + PySpark)
* Delta Lake
* SQL Warehouse (Free Edition)
* Medallion Architecture

---

## ⚠️ Notes

* Free Databricks version supports **SQL Warehouse only**
* Gold layer is implemented using **SQL for dashboard compatibility**
* Avoid using `count()` without alias (use `student_count`)

---

## 🎯 Conclusion

This project demonstrates how to build a **scalable data pipeline** and convert raw data into **actionable business insights** using Databricks.

---



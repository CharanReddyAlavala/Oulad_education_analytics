
# 📊 OULAD Education Analytics Lakehouse Project

## 📌 Project Overview
This project builds a **Lakehouse architecture using Databricks** on top of the **Open University Learning Analytics Dataset (OULAD)**. The goal is to create a unified data platform to analyze **student performance, engagement, and dropout trends**.

The pipeline follows the **Medallion Architecture**:
- 🥉 Bronze Layer → Raw data ingestion  
- 🥈 Silver Layer → Data cleaning & transformation  
- 🥇 Gold Layer → Business KPIs & analytics  

---

## 🎯 Business Problem
Educational institutions face challenges such as:
- Fragmented data across multiple systems  
- Difficulty tracking student performance  
- No early identification of at-risk students  

This project provides a **single source of truth** for better analytics and decision-making.

---

## 📂 Dataset Information
- **Source**: Open University, UK  
- **Dataset**: OULAD  
- **Format**: CSV (7 Tables)

### 📊 Tables Used
- `courses`
- `studentInfo`
- `assessments`
- `studentAssessment`
- `studentRegistration`
- `vle`
- `studentVle`

### 📈 Data Volume
- 10M+ activity records  
- 173K+ assessment records  

---

## 🏗️ Architecture (Medallion)
### 🥉 Bronze Layer (Raw)
- Ingest CSV files  
- Store as Delta tables  
- Add audit columns:
  - `ingestion_timestamp`
  - `source_file`

### 🥈 Silver Layer (Cleaned)
- Handle null values  
- Remove duplicates  
- Standardize categories  
- Join all datasets  
- Add derived columns:
  - `risk_flag`
  - `enrollment_duration`
  - `weighted_score`

### 🥇 Gold Layer (Analytics)
- KPI table creation  
- SQL + PySpark analytics  
- Window functions:
  - `ROW_NUMBER`
  - `RANK`
  - `LAG`, `LEAD`

---

## ⚙️ Technologies Used
- Databricks  
- PySpark  
- Delta Lake  
- SQL (CTEs & Analytics)  
- Apache Spark  

---

## 🔄 Pipeline Workflow
1. Load raw CSV data into Bronze layer  
2. Clean and transform data in Silver layer  
3. Join datasets and apply business logic  
4. Perform incremental loads using `MERGE`  
5. Apply Delta Lake features:
   - Time Travel  
   - Schema Evolution  
6. Generate KPI tables in Gold layer  

---

## 📈 Key KPIs
- ✅ Pass Rate by Module  
- ✅ Dropout Rate Analysis  
- ✅ Average Assessment Score  
- ✅ Engagement Score  
- ✅ At-Risk Students  
- ✅ Submission Rate  
- ✅ Top VLE Content  
- ✅ Executive Summary  

---

## 🚀 Features
- Delta Lake operations (INSERT, UPDATE, DELETE)  
- Incremental loading using MERGE  
- Schema Evolution  
- Time Travel queries  
- Window Functions for analytics  
- Large-scale data processing  

---

## 👥 Team Roles
| Role | Responsibility |
|------|--------------|
| Ingestion Engineer | Bronze layer data loading |
| Transformation Engineer | Silver layer processing |
| Analytics Engineer | Gold layer KPI creation |

---

## 📁 Project Structure  
---
OULAD-Lakehouse-Project/
│
├── bronze/
├── silver/
├── gold/
├── sql/
├── notebooks/
└── README.md

## 🧪 How to Run
1. Upload dataset to Databricks (DBFS)  
2. Run Bronze notebooks  
3. Execute Silver transformations  
4. Run Gold analytics queries  
5. View results using SQL  

---

## 📊 Business Impact
- Identifies at-risk students early  
- Improves course performance tracking  
- Enables data-driven decisions  
- Supports student success strategies  

---

## 📌 Conclusion
This project demonstrates how **Databricks Lakehouse architecture** can transform raw educational data into **actionable insights** using modern data engineering techniques.

---

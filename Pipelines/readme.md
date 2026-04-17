
🎓 OULAD Education Analytics Pipeline (Databricks ETL)
📌 Project Overview

This project implements a scalable ETL pipeline using Databricks to analyze student performance using the OULAD (Open University Learning Analytics Dataset).

The pipeline follows the Medallion Architecture (Bronze → Silver → Gold) to transform raw educational data into meaningful insights such as:

Student performance
Pass rates
Dropout analysis
Risk prediction
🏗️ Architecture

The pipeline is built using Databricks Delta Live Tables (DLT) and structured into three layers:

Bronze  →  Silver  →  Gold
(Raw)      (Clean)    (Analytics)
📂 Project Structure
project-folder/
│
├── bronze_layer.ipynb     # Raw data ingestion
├── silver_layer.ipynb     # Data cleaning & transformation
├── gold_layer.ipynb       # Business insights & aggregations
│
└── README.md              # Documentation
⚙️ Technologies Used
Platform: Databricks
Processing Engine: Apache Spark
Language: Python (PySpark)
Storage: Delta Tables
Pipeline: Delta Live Tables (DLT)
📊 Dataset
Dataset: OULAD (Open University Learning Analytics Dataset)
Data Includes:
Student information
Courses & modules
Assessments
Virtual Learning Environment (VLE) interactions
🔄 Pipeline Explanation
🥉 Bronze Layer (Raw Data)
Ingests raw CSV data into Delta tables
No transformations applied
Tables:
bronze_students
bronze_courses
bronze_assessments
bronze_vle

👉 Output: Raw Delta tables

🥈 Silver Layer (Cleaned Data)
Handles missing values and duplicates
Joins datasets (students, courses, assessments)
Applies schema enforcement and transformations
Tables:
silver_students
silver_courses
silver_assessments
silver_vle

👉 Output: Cleaned and structured data

🥇 Gold Layer (Analytics & Insights)
Generates business-level insights
Aggregations and KPIs:
gold_pass_rate
gold_dropout
gold_risk_distribution
gold_top_students

👉 Output: Analytics-ready tables for reporting

📈 Key Features
End-to-end ETL pipeline
Scalable data processing with Spark
Modular notebook-based design
Real-time pipeline monitoring in Databricks
Supports incremental and full refresh
▶️ Pipeline Execution
Open Databricks Workspace
Navigate to Jobs & Pipelines
Select the pipeline
Click Run Pipeline

📌 Pipeline supports:

Full recompute
Incremental updates
📊 Use Cases
Student performance analysis
Dropout prediction systems
Educational data analytics
Dashboard integration (Power BI / Tableau)
🚀 Future Enhancements
Integrate ML model for risk prediction
Build real-time dashboard
Automate alerts for at-risk students

# 📂 Raw Data – Student Performance Dataset

## 📌 Overview

This directory contains the **raw CSV datasets** used as input for the data pipeline.
These files are ingested into the **Bronze layer** without any transformations.

---

## 📁 Dataset Files

### 🔹 1. studentInfo.csv

**Description:** Student demographic and final result data

**Columns:**

* `id_student` – Unique student ID
* `gender`, `age_band`, `region`
* `highest_education`, `imd_band`
* `num_of_prev_attempts`, `studied_credits`
* `disability`
* `final_result` (Pass / Fail / Withdrawn)

---

### 🔹 2. studentRegistration.csv

**Description:** Student course enrollment details

**Columns:**

* `id_student`
* `code_module` – Course
* `code_presentation` – Session
* `date_registration`, `date_unregistration`

---

### 🔹 3. courses.csv

**Description:** Course metadata

**Columns:**

* `code_module`
* `code_presentation`
* `module_presentation_length`

---

### 🔹 4. assessments.csv

**Description:** Assessment structure per course

**Columns:**

* `id_assessment`
* `code_module`, `code_presentation`
* `assessment_type`
* `date`, `weight`

---

### 🔹 5. studentAssessment.csv

**Description:** Student scores in assessments

**Columns:**

* `id_student`, `id_assessment`
* `date_submitted`
* `score`, `is_banked`

---

### 🔹 6. vle.csv

**Description:** Student interaction with learning platform (VLE)

**Columns:**

* `id_site`
* `code_module`, `code_presentation`
* `activity_type`
* `week_from`, `week_to`

---

## 🔗 Data Relationships (Important)

```id="rel123"
studentInfo          → id_student
studentRegistration  → id_student + course
studentAssessment    → id_student + id_assessment
assessments          → id_assessment
courses              → code_module + code_presentation
vle                  → code_module + code_presentation
```

---

## 🔄 Data Flow

```id="flow456"
Raw Data → Bronze Layer → Silver Layer → Gold Layer → Dashboard
```

---

## ⚠️ Data Quality Notes

* Data is **unprocessed (raw)**
* Possible issues:

  * Missing values
  * Duplicate records
  * Inconsistent formats

👉 These are handled in the **Silver layer**

---

## 🎯 Purpose of Dataset

This data is used to:

* Analyze student performance
* Calculate pass & dropout rates
* Identify at-risk students
* Study learning behavior (VLE)
* Build dashboards and insights

---



📂 Raw Dataset – Student Performance Data
📌 Overview

This folder contains the raw input datasets (CSV files) used in the data pipeline.
These files are directly ingested into the Bronze Layer in Databricks without any transformation.

📁 Files Included
1. studentInfo.csv

Contains demographic and academic information about students.

Key Columns:

id_student – Unique student ID
gender – Gender of student
region – Geographic region
highest_education – Education level
imd_band – Socio-economic band
age_band – Age group
num_of_prev_attempts – Previous attempts
studied_credits – Credits taken
disability – Disability status
final_result – Final outcome (Pass/Fail/Withdrawn)
2. studentRegistration.csv

Tracks student enrollment details.

Key Columns:

id_student
code_module – Course ID
code_presentation – Session
date_registration
date_unregistration
3. courses.csv

Contains course metadata.

Key Columns:

code_module
code_presentation
module_presentation_length
4. assessments.csv

Defines assessments for each course.

Key Columns:

id_assessment
code_module
code_presentation
assessment_type
date
weight
5. studentAssessment.csv

Stores student scores in assessments.

Key Columns:

id_assessment
id_student
date_submitted
is_banked
score
6. vle.csv

Contains Virtual Learning Environment (VLE) activity data.

Key Columns:

id_site
code_module
code_presentation
activity_type
week_from
week_to
🔄 Data Flow
Raw CSV Files → Bronze Layer → Silver Layer → Gold Layer → Dashboard
⚠️ Notes
Data is raw and uncleaned
May contain:
Null values
Duplicates
Inconsistent formats
Cleaning and transformations are handled in the Silver Layer
🎯 Purpose

This dataset is used to:

Analyze student performance
Identify at-risk students
Evaluate course effectiveness
Build dashboards and insights

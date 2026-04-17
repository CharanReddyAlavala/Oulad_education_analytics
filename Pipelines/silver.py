import dlt
from pyspark.sql.functions import *

# ---------------------------
# CLEAN TABLES
# ---------------------------

@dlt.table
def silver_student_info():
    return dlt.read("bronze_student_info") \
        .dropDuplicates() \
        .fillna({"studied_credits": 0, "num_of_prev_attempts": 0})

@dlt.table
def silver_student_registration():
    return dlt.read("bronze_student_registration").dropDuplicates()

@dlt.table
def silver_assessments():
    return dlt.read("bronze_assessments") \
        .withColumn("weight", col("weight").cast("double"))

@dlt.table
def silver_student_assessments():
    return dlt.read("bronze_student_assessments") \
        .withColumn("score", coalesce(col("score"), lit(0)))

@dlt.table
def silver_courses():
    return dlt.read("bronze_courses").dropDuplicates()

# ✅ VLE FIX (aggregate to avoid duplication)
@dlt.table
def silver_vle():
    return dlt.read("bronze_vle") \
        .groupBy("code_module", "code_presentation") \
        .agg(count("*").alias("total_vle_activity"))

# ---------------------------
# FINAL JOIN (CONNECTED FLOW)
# ---------------------------

@dlt.table
def silver_student_enriched():

    si = dlt.read("silver_student_info")
    
    # Drop duplicate columns from student_registration before joining
    sr = dlt.read("silver_student_registration") \
        .drop("code_module", "code_presentation")
    
    sa = dlt.read("silver_student_assessments")
    
    # Drop duplicate columns from assessments before joining
    a = dlt.read("silver_assessments") \
        .drop("code_module", "code_presentation")

    # ✅ Select only needed columns from courses
    c = dlt.read("silver_courses") \
        .select("code_module", "module_presentation_length")

    # ✅ VLE already aggregated → safe
    v = dlt.read("silver_vle")

    df = si.alias("si") \
        .join(sr.alias("sr"), ["id_student"], "left") \
        .join(sa.alias("sa"), ["id_student"], "left") \
        .join(a.alias("a"), ["id_assessment"], "left") \
        .join(c.alias("c"), ["code_module"], "left") \
        .join(v.alias("v"), ["code_module", "code_presentation"], "left") \
        .fillna({"total_vle_activity": 0})

    return df.withColumn(
        "risk_flag",
        when((col("score") < 40) | (col("final_result") == "Fail"), "High Risk")
        .otherwise("Low Risk")
    )

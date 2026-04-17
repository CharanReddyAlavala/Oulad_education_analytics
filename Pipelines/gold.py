import dlt
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# ---------------------------
# SOURCE (Silver Layer)
# ---------------------------

# No spark.sql, no manual table reads
# Always use dlt.read()

# ---------------------------
# 1. COURSE PERFORMANCE
# ---------------------------

@dlt.table
def gold_course_performance():
    df = dlt.read("silver_student_enriched")

    return df.groupBy("code_module").agg(
        count("*").alias("total_students"),
        avg("score").alias("avg_score"),
        sum(when(col("final_result") == "Pass", 1).otherwise(0)).alias("passes"),
        sum(when(col("final_result") == "Withdrawn", 1).otherwise(0)).alias("dropouts"),
        avg("total_vle_activity").alias("avg_vle_activity")   # ✅ VLE included
    )

# ---------------------------
# 2. PASS RATE
# ---------------------------

@dlt.table
def gold_pass_rate():
    df = dlt.read("silver_student_enriched")

    return df.groupBy("code_module").agg(
        (sum(when(col("final_result") == "Pass", 1).otherwise(0)) / count("*") * 100)
        .alias("pass_percentage")
    )

# ---------------------------
# 3. DROPOUT RATE
# ---------------------------

@dlt.table
def gold_dropout_rate():
    df = dlt.read("silver_student_enriched")

    return df.groupBy("code_module").agg(
        (sum(when(col("final_result") == "Withdrawn", 1).otherwise(0)) / count("*") * 100)
        .alias("dropout_percentage")
    )

# ---------------------------
# 4. RISK DISTRIBUTION
# ---------------------------

@dlt.table
def gold_risk_distribution():
    return dlt.read("silver_student_enriched") \
        .groupBy("risk_flag").count()

# ---------------------------
# 5. TOP STUDENTS
# ---------------------------

@dlt.table
def gold_top_students():
    df = dlt.read("silver_student_enriched")

    window_spec = Window.partitionBy("code_module").orderBy(desc("score"))

    return df.withColumn("rank", row_number().over(window_spec)) \
             .filter(col("rank") <= 5)
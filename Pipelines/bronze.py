import dlt
from pyspark.sql.functions import *

BASE_PATH = "/Volumes/workspace/default/raw_data/Delta Force/"

def read_csv(file):
    return spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("multiLine", "true") \
        .option("escape", "\"") \
        .load(BASE_PATH + file)

@dlt.table
def bronze_student_info():
    return read_csv("studentInfo.csv")

@dlt.table
def bronze_student_registration():
    return read_csv("studentRegistration.csv")

@dlt.table
def bronze_assessments():
    return read_csv("assessments.csv")

@dlt.table
def bronze_student_assessments():
    return read_csv("studentAssessment.csv")

@dlt.table
def bronze_courses():
    return read_csv("courses.csv")

@dlt.table
def bronze_vle():
    return read_csv("vle.csv")
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit


spark = SparkSession.builder.getOrCreate()

def addCol(df):
    df = df.withColumn("new_col", lit("a"))
    return df

df = spark.sql("SELECT * FROM default.target")

df2 = addCol(df)

df2.show()
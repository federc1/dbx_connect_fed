# Databricks notebook source
from pysparkapp.target_query import addCol

# COMMAND ----------

df = spark.createDataFrame([
    ("fed","1")
    ], ["person","value"])

# COMMAND ----------

df.show()

# COMMAND ----------

df2 = addCol(df=df)

# COMMAND ----------

df2.show()

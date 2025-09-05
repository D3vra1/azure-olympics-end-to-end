# Databricks notebook source
from pyspark.sql.functions import col,column
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DataType

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": "c3cca929-7330-4f13-8261-e4c6dfa9f694",
  "fs.azure.account.oauth2.client.secret": "I_M8Q~FpvQa-pMaPqVvflRUrYHe2ITBwlKyPqaLG",
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/63663f15-a5e2-4a86-a039-1b4071a27147/oauth2/token"
}

dbutils.fs.mount(
  source = "abfss://tokyo-olympics-data@tokyoolympicsdatadev.dfs.core.windows.net/",
  mount_point = "/mnt/tokyoolympic",
  extra_configs = configs
)


# COMMAND ----------

# MAGIC %fs
# MAGIC ls "mnt/tokyoolympic"

# COMMAND ----------

athletes = spark.read.format("csv").option("inferschema","true").option("header","true").load("/mnt/tokyoolympic/raw-data/athletes.csv")
coaches = spark.read.format("csv").option("inferschema","true").option("header","true").load("/mnt/tokyoolympic/raw-data/coaches.csv")
EntriesGender = spark.read.format("csv").option("inferschema","true").option("header","true").load("/mnt/tokyoolympic/raw-data/EntriesGender.csv")
medals = spark.read.format("csv").option("inferschema","true").option("header","true").load("/mnt/tokyoolympic/raw-data/medals.csv")
teams = spark.read.format("csv").option("inferschema","true").option("header","true").load("/mnt/tokyoolympic/raw-data/teams.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema

# COMMAND ----------

coaches.show()

# COMMAND ----------

coaches.printSchema

# COMMAND ----------

EntriesGender.printSchema

# COMMAND ----------

EntriesGender.show()

# COMMAND ----------

EntriesGender = EntriesGender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("Male").cast(IntegerType()))\
    .withColumn("Total",col("Total").cast(IntegerType()))

# COMMAND ----------

EntriesGender.printSchema

# COMMAND ----------

medals.show()
medals.printSchema

# COMMAND ----------

teams.show()
teams.printSchema

# COMMAND ----------

top_gold_medal_countries = (
    medals.orderBy("Gold", ascending=False)
          .select("TeamCountry", "Gold")
)

top_gold_medal_countries.show(10)


# COMMAND ----------

# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = EntriesGender.withColumn(
    'Avg_Female', EntriesGender['Female'] / EntriesGender['Total']
).withColumn(
    'Avg_Male', EntriesGender['Male'] / EntriesGender['Total']
)
average_entries_by_gender.show()

# COMMAND ----------

athletes.write.mode('overwrite').option("header",'true').csv("/mnt/tokyoolympic/transformed-data/athletes")

# COMMAND ----------

coaches.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/coaches")
EntriesGender.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/EntriesGender")
medals.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/medals")
teams.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/teams")

# COMMAND ----------

athletes.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/athletes")

coaches.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/coaches")

EntriesGender.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/EntriesGender")

medals.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/medals")

teams.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/teams")

# COMMAND ----------

df = spark.read.csv("/mnt/tokyoolympic/transformed-data/athletes", header=True)
df.show(5)

# COMMAND ----------

dbutils.secrets.get

# COMMAND ----------

dbutils.secrets.help()
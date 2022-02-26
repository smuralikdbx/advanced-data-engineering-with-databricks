# Databricks notebook source
# MAGIC %run ./_databricks-academy-helper $lesson="2.08"

# COMMAND ----------

# MAGIC %run ./_utility-functions

# COMMAND ----------

DA.cleanup()
DA.init()

# COMMAND ----------

# Create the user datasets
create_date_lookup()              # Create static copy of date_lookup
print()

init_source_daily()               # Create the data factory
DA.daily_stream.load_through(3)   # Load one new day for DA.paths.source_daily
DA.process_bronze()               # Process through the bronze table

# COMMAND ----------

DA.conclude_setup()


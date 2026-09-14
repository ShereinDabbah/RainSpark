# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0193efe7-a63f-4c2d-9bc7-792b1cc4588c",
# META       "default_lakehouse_name": "Lakehouse1",
# META       "default_lakehouse_workspace_id": "608c0dc8-605a-4c36-8c66-d7773b569434",
# META       "known_lakehouses": [
# META         {
# META           "id": "0193efe7-a63f-4c2d-9bc7-792b1cc4588c"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Create (or overwrite) a table from a CSV file in Lakehouse Files
notebookutils.lakehouse.loadTable(
    {
        "relativePath": "Files/lakehouse_random_data.csv",  # path under Lakehouse Files
        "pathType": "File",
        "mode": "Overwrite",                 # or "Append"
        "recursive": False,
        "formatOptions": {
            "format": "Csv",
            "header": True,
            "delimiter": ","
        }
    },
    "my_table",      # target table name in Lakehouse1
    "Lakehouse1",    # lakehouse name
    None             # workspace id (None = current workspace)
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

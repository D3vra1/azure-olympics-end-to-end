# Tokyo Olympics – End-to-End Azure Data Engineering

An end-to-end pipeline on the Tokyo Olympics dataset using **Azure Data Lake (Gen2), Azure Data Factory, Azure Databricks (PySpark), Synapse Analytics (SQL)**, and  **Power BI**.

## 📐 Architecture

```mermaid
flowchart LR
    A[Raw Data (CSV/Parquet)] --> B[Azure Data Factory]
    B --> C[Azure Databricks (PySpark)]
    C --> D[Azure Synapse Analytics (SQL)]
    D --> E[Power BI Dashboard] 
```

# Tokyo Olympics – End-to-End Azure Data Engineering

An end-to-end pipeline on the Tokyo Olympics dataset using **Azure Data Lake (Gen2), Azure Data Factory, Azure Databricks (PySpark), Synapse Analytics (SQL)**, and  **Power BI**.

## 📐 Architecture

```mermaid
flowchart LR
  A[Raw CSVs<br/>ADLS Gen2: raw-data] -->|scheduled copy| B[Azure Data Factory]
  B --> C[Azure Databricks (PySpark)]
  C --> D[ADLS Gen2: transformed-data]
  D --> E[Synapse Analytics - SQL]
  E --> F[BI / Analytics (SQL, Power BI)]

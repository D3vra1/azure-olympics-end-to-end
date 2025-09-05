# Azure Data Engineering Project: Olympics Dataset

## 📖 Project Overview
This project demonstrates a modern **end-to-end data engineering pipeline** built on Microsoft Azure.  
The goal is to process and analyze the Olympics dataset using **ADF, Databricks, PySpark, SQL, and Synapse Analytics**, showcasing both data engineering and analytics skills.

---

## 🏗️ Architecture

The pipeline follows these stages:

1. **Raw Data Storage** → Data is ingested into **Azure Data Lake Storage (ADLS Gen2)**.
2. **Data Ingestion (ADF)** → Azure Data Factory pipelines orchestrate the movement of raw data into the bronze zone.
3. **Data Transformation (Databricks + PySpark)** → Data is cleaned, transformed, and written to curated layers.
4. **SQL Analytics (Synapse)** → Processed data is stored and queried in Synapse Analytics.
5. **Visualization (BI Tool)** → Data is available for dashboarding (Power BI / Synapse Serverless).

📌 Here’s the architecture flow:
<img width="1366" height="665" alt="image" src="https://github.com/user-attachments/assets/e42f2bf1-270f-414a-ada0-9a1a59889dd8" />

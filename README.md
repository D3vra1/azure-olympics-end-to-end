# Azure Olympics Data Engineering Pipeline

An end-to-end data engineering pipeline using the Tokyo Olympics dataset on Azure — built with ADF, Databricks (PySpark), SQL, and Synapse Analytics.

---

## Architecture

**Workflow Overview**:
Raw CSVs (ADLS Gen2)
↓ ADF orchestrates
Bronze → Spark in Databricks
Curated data → Synapse Analytics
Visualize via Power BI or Synapse SQL

---

## Tech Stack
- **Azure Data Lake Storage (Gen2)** – Data storage (raw & transformed zones)  
- **Azure Data Factory (ADF)** – Pipeline orchestration  
- **Azure Databricks + PySpark** – Data transformation  
- **Azure Synapse Analytics** – Querying and analysis  
- **Optional**: Power BI or Synapse SQL for visualization  

---

### Architecture Diagram
![Azure Olympics Pipeline]![Tokyo Olympics Data Architecture](https://github.com/user-attachments/assets/f18431c1-7dbd-4be1-8b2f-7487ea30ab5e)

---

## Repo Contents

- `notebooks/` – Databricks notebooks (PySpark logic)  
- `sql/` – Synapse SQL scripts  
- `adf/` – Azure Data Factory JSON/ARM exports  
- `docs/` – Architecture diagram and relevant screenshots  
- `README.md` – Explanation + how-to-run

---

## Highlights & Learnings
- Built read/write pipeline for raw & curated Olympic data  
- Mounted ADLS Gen2 securely using OAuth via Databricks secrets  
- Crafted PySpark jobs for data aggregation  
- Modeled and queried in Synapse for analytics  
- Optional: built dashboards to visualize medal stats and participation patterns  

---

## About the Author

**Dev Raj Singh Sukhai**  
Aspiring Azure Data Engineer.  
Check out my [LinkedIn](https://www.linkedin.com/in/devrajsingh-sukhai-670430249/) for the full story.

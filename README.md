This project focuses on designing and implementing a Customer Relationship Management (CRM) Data Warehouse to support business intelligence and data-driven decision-making.
The data warehouse integrates customer data from multiple sources such as sales, marketing, and support systems. It enables organizations to analyze customer behavior, track performance, and generate actionable insights for improving customer satisfaction and business growth.
📌 Project Overview

A fully functional *Customer Relationship Management (CRM) Data Warehouse* built to consolidate, transform, and analyze customer data for actionable business insights. This system implements a *star schema* data warehouse, an automated *ETL pipeline, and a suite of **analytical reports and dashboards*.

---

## 🎯 Objectives

- Centralize CRM data from multiple sources (sales, support, marketing)
- Design an optimized data warehouse using dimensional modeling (Star Schema)
- Automate data ingestion and transformation via an ETL pipeline
- Generate business intelligence reports (revenue trends, customer segmentation, churn analysis)
- Ensure data quality through validation and testing

---

## 🗂️ Project Structure


crm_dw/
│
├── sql/
│   ├── 01_create_schema.sql          # Database schema & dimension/fact tables
│   ├── 02_indexes.sql                # Performance indexes
│   └── 03_analytical_queries.sql     # BI queries for insights
│
├── etl/
│   ├── extract.py                    # Data extraction from CSV/DB sources
│   ├── transform.py                  # Data cleaning & transformation
│   ├── load.py                       # Load data into warehouse
│   └── pipeline.py                   # Main ETL orchestrator
│
├── reports/
│   ├── business_insights.py          # Revenue, churn, segmentation reports
│   └── dashboard.py                  # Interactive CLI dashboard
│
├── tests/
│   ├── test_etl.py                   # Unit tests for ETL logic
│   └── test_queries.py               # Query validation tests
│
├── diagrams/
│   ├── star_schema.png               # Data warehouse schema diagram
│   └── etl_flow.png                  # ETL pipeline flowchart
│
├── data_samples/
│   └── sample_crm_data.csv           # Sample source data
│
├── docs/
│   └── project_report.md             # Detailed project report
│
├── requirements.txt
└── README.md


---

## 🧱 Architecture — Star Schema


                        ┌────────────────────┐
                        │   dim_date         │
                        │ (date_key, year,   │
                        │  quarter, month)   │
                        └────────┬───────────┘
                                 │
┌──────────────┐    ┌────────────▼────────────┐    ┌──────────────────┐
│ dim_customer │    │     fact_sales           │    │   dim_product    │
│ (cust_key,   │◄───│  (sale_id, date_key,    │───►│ (prod_key, name, │
│  name, seg,  │    │   cust_key, prod_key,   │    │  category, price)│
│  region)     │    │   rep_key, revenue,     │    └──────────────────┘
└──────────────┘    │   quantity, discount)   │
                    └─────────┬───────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   dim_sales_rep    │
                    │ (rep_key, name,    │
                    │  region, team)     │
                    └────────────────────┘


---

## ⚙️ ETL Pipeline


[CSV / DB Sources]
       │
       ▼
  [EXTRACT] ──► Raw data loaded into DataFrames
       │
       ▼
 [TRANSFORM] ──► Cleaning, deduplication, type casting,
                 surrogate key generation, null handling
       │
       ▼
   [LOAD] ──► Insert into PostgreSQL star schema
       │
       ▼
[VALIDATE] ──► Row counts, null checks, referential integrity


---

## 🚀 Setup & Installation

### 1. Clone the repository
bash
git clone https://github.com/yourusername/crm-data-warehouse.git
cd crm-data-warehouse


### 2. Install dependencies
bash
pip install -r requirements.txt


### 3. Configure your database
Edit the DB_CONFIG in etl/pipeline.py:
python
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "crm_dw",
    "user": "your_user",
    "password": "your_password"
}


### 4. Initialize the schema
bash
psql -U your_user -d crm_dw -f sql/01_create_schema.sql
psql -U your_user -d crm_dw -f sql/02_indexes.sql


### 5. Run the ETL pipeline
bash
python etl/pipeline.py


### 6. Generate reports
bash
python reports/business_insights.py


---

## 📊 Key Business Insights Generated

| Report | Description |
|--------|-------------|
| Revenue Trend | Monthly/quarterly revenue over time |
| Customer Segmentation | RFM analysis (Recency, Frequency, Monetary) |
| Churn Analysis | Customers at risk of churn |
| Top Products | Best-performing products by revenue |
| Sales Rep Performance | Rep-level KPIs and rankings |
| Regional Analysis | Revenue breakdown by geography |

---

## 🧪 Running Tests

bash
python -m pytest tests/ -v


---

## 📈 Sample Output


===== CRM DATA WAREHOUSE — BUSINESS INSIGHTS =====

[Revenue Trend]
  2024-Q1: $124,500  ▲ 12.3%
  2024-Q2: $138,200  ▲ 10.9%
  2024-Q3: $151,800  ▲  9.8%
  2024-Q4: $172,400  ▲ 13.6%

[Customer Segments]
  Champions     :  312 customers  |  Avg LTV: $4,820
  Loyal         :  498 customers  |  Avg LTV: $2,340
  At Risk        :  187 customers  |  Avg LTV: $1,105
  Lost           :   94 customers  |  Avg LTV:   $430

[Top 5 Products by Revenue]
  1. Enterprise Suite    — $98,400
  2. Pro License         — $74,200
  3. Support Package     — $52,100
  4. Onboarding Service  — $38,900
  5. Add-on Module       — $27,600


---

## 🛠️ Technologies Used

- *Python 3.10+* — ETL pipeline, data processing
- *PostgreSQL* — Data warehouse backend
- *Pandas* — Data transformation
- *SQLAlchemy* — ORM & DB connectivity
- *Matplotlib / Seaborn* — Visualization
- *Pytest* — Unit testing

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

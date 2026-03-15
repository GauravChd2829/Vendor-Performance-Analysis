# Vendor Performance Analysis

Vendor and supply chain performance analysis using Python, SQL, statistical analysis, and Power BI.

The project studies vendor purchasing behavior, sales performance, profitability patterns, and inventory efficiency. The objective focuses on identifying vendors and brands that influence revenue growth, operational cost efficiency, and inventory turnover.

The workflow includes data ingestion, ETL automation, statistical exploration, and interactive dashboard reporting.

---

# Dataset Overview

The original dataset contains multiple transactional tables representing vendor purchases, product sales, pricing information, and logistics costs.

Data volume exceeds **10 million transactional records across multiple raw tables** including

Vendor purchase transactions
Product level sales data
Vendor invoice freight costs
Pricing tables containing brand level price structures

These raw datasets simulate real enterprise supply chain data typically found in retail distribution systems.

Due to size constraints, the repository includes the **processed analytical dataset used for modelling and dashboard reporting**.

---

# Business Problem

Retail distribution companies depend heavily on vendor networks to maintain supply chains and ensure product availability.

Poor vendor performance monitoring can result in

inefficient procurement
inventory stagnation
high logistics costs
low profitability

The analysis focuses on answering critical supply chain questions

Which vendors generate the highest revenue contribution
Which vendors create inventory stagnation
Which brands maintain strong margins yet low sales volume
How pricing strategies affect profitability
How vendor dependency affects procurement risk

The analysis also evaluates whether vendor relationships align with profitability and operational efficiency.

Key objectives include

Identify underperforming brands requiring pricing or promotional adjustments
Identify vendors contributing maximum revenue and purchase value
Analyze inventory turnover efficiency
Measure profitability differences between high performing and low performing vendors

These objectives directly relate to vendor strategy optimization in supply chain management. 

---

# Data Engineering Pipeline

The project implements a structured data pipeline designed for reproducible analytics.

Raw dataset ingestion
Database storage
Automated ETL processing
Statistical exploration
Interactive dashboard visualization

Python scripts automate the transformation pipeline so that the entire workflow can be executed with minimal manual intervention.

---

# Data Ingestion

Raw datasets are loaded into a relational database using Python.

The ingestion script reads CSV files from the data directory and writes them into SQLite tables.

This step simulates real enterprise ETL pipelines where raw vendor transaction data arrives from multiple operational systems.

Key ingestion tasks

Load CSV datasets
Create database tables
Store structured records in SQLite
Log ingestion operations for traceability

The ingestion script enables repeatable database creation.

File used

ingestion_db.py

---

# Automated ETL Processing

After ingestion the ETL process prepares the dataset for analytical modeling.

The ETL script performs

data cleaning
missing value handling
data type correction
feature engineering
KPI calculation

Key derived metrics include

Gross Profit
Profit Margin
Stock Turnover
Sales to Purchase Ratio

These metrics form the foundation for vendor performance evaluation.

File used

get_vendor_summary.py

The automation ensures that vendor metrics can be regenerated whenever new transactional data arrives.

---

# Exploratory Data Analysis

Exploratory analysis was performed to understand statistical patterns within vendor transactions.

Key observations

Certain products show negative gross profit which indicates selling below purchase cost
Some items show zero sales which indicates stagnant inventory
Large variance in freight cost reveals inconsistent logistics spending
High standard deviation in pricing indicates premium product segments

Statistical exploration identified potential inefficiencies in pricing strategy, vendor dependency, and inventory management. 

Correlation analysis revealed

strong relationship between purchase quantity and sales quantity
weak relationship between purchase price and profitability

These insights highlight that pricing alone does not drive revenue growth.

---

# Statistical Analysis

Statistical testing was conducted to evaluate profitability differences between vendor groups.

Hypothesis testing compared profit margin distributions between high performing vendors and low performing vendors.

Null hypothesis
no significant difference exists between profit margins of vendor groups

Alternative hypothesis
profit margins differ significantly across vendor groups

Results rejected the null hypothesis indicating distinct vendor profitability patterns. 

This finding suggests that vendor performance depends on pricing strategy, sales volume, and operational efficiency rather than uniform profit behavior.

---

# Power BI Dashboard

An interactive dashboard was developed to support decision making for procurement teams.

The dashboard provides real time monitoring of vendor performance indicators.

Main dashboard metrics include

Total Sales
Total Purchase Value
Gross Profit
Profit Margin
Unsold Inventory Capital

The dashboard also highlights

Top vendors by sales
Top performing brands
Low performing vendors
Inventory turnover efficiency
Purchase contribution distribution

These insights support procurement planning, vendor negotiation strategies, and inventory optimization.

Dashboard preview

![Vendor Performance Dashboard](Screenshot%202026-03-15%20210413.png)

---

# Key Insights

Top vendors contribute approximately **65 percent of total purchases**, showing strong vendor concentration.

Vendor dependency introduces supply chain risk and suggests diversification opportunities.

Bulk purchasing significantly reduces unit cost which improves overall profitability.

Slow moving inventory represents more than **2.7 million dollars of locked capital**, indicating procurement inefficiencies.

Certain brands maintain high profit margins with low sales volume. These brands represent candidates for marketing optimization or price adjustments.

These insights can directly influence procurement strategy, pricing decisions, and inventory planning.

---

# Technology Stack

Python
Pandas
SQLite
Statistical Analysis
Power BI
Excel
Data Visualization

---

# Project Structure

```
vendor-performance-analysis

data
vendor_sales_summary.csv

ingestion_db.py
get_vendor_summary.py

Exploratory Data Analysis.ipynb
Vendor Performance Analysis.ipynb

Vendor Performance Report.pdf
vendor_performance.pbix

requirements.txt
README.md
```

---

# How to Run the Project

Clone repository

```
git clone https://github.com/GauravChd2829/Vendor-Performance-Analysis
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run ingestion script

```
python ingestion_db.py
```

Run ETL processing script

```
python get_vendor_summary.py
```

---

# Report

Detailed analytical report available here

📄Vendor Performance Report.pdf

The report contains full statistical analysis, correlation insights, vendor performance evaluation, and business recommendations.

---

# Author

Gaurav Chandak
Computer Science Undergraduate
Interest areas include Data Analytics, Supply Chain Analytics, Machine Learning, Business Intelligence

---

# Project Outcome

The project demonstrates how data engineering pipelines, statistical analysis, and business intelligence dashboards can support vendor management decisions.

Organizations can use this approach to

optimize procurement strategy
reduce inventory holding cost
improve vendor negotiations
increase profitability through data driven decisions

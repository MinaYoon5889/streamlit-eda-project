# Amazon Diwali Sales 2025 – EDA & Interactive Dashboard  
INSY 6500 – Final Project  
Author: Ruiying Zhu, Mina Yoon
Date: December 2025  

---

## Project Overview  
This project analyzes the **Amazon Diwali Sales 2025** dataset by following the structured EDA pipeline taught in INSY 6500 (Phase 1 to Phase 6).  
The goal is to clean the data, assess data quality, explore statistical patterns, engineer transformations, and finally build an **interactive Streamlit dashboard** for insight generation.

The work is organized into Jupyter notebooks (one per phase) and a Streamlit application for interactive exploration.

---

## Folder Structure
my_project/
│
├── data/
│ └── raw/
│ └── amazon_sales_2025_INR.csv
│
├── notebooks/
│ ├── Cleaning.ipynb
│ ├── Data_quality_assessment.ipynb
│ ├── initial_exploration.ipynb
│ ├── Statistical_eda.ipynb
│ └── Transformation.ipynb
│
├── Streamlit_app.py
├── README.md
├── requirements.txt
└── ruff.toml



---

## Phase Summary (Phases 1–5)

### **Phase 1: Initial Exploration**
- Loaded the dataset and inspected basic structure  
- Displayed data types, missing values, and high-level distributions  
- Identified key variables for deeper analysis  

### **Phase 2: Cleaning**
- Standardized date formats  
- Converted numeric columns  
- Cleaned categorical inconsistencies  
- Verified completeness and removed invalid rows if necessary  

### **Phase 3: Data Quality Assessment**
- Checked missingness  
- Validated category domains  
- Verified numerical ranges  
- Ensured dataset is usable for analysis and modeling  

### **Phase 4: Statistical EDA**
- Univariate: histograms, descriptive stats  
- Bivariate: scatter plots, correlations, boxplots  
- Multivariate: heatmaps, subgroup comparisons  
- Interpretation, hypothesis generation, and iteration signals written clearly  

### **🔹 Phase 5: Transformation & Feature Engineering**
Created meaningful features to support dashboard interaction:
- Extracted date components (Month, Quarter)  
- Created binary flags (Delivered, Satisfied)  
- Log-transformed Total Sales  
- Converted month names into ordered categorical data  

---

## Streamlit Dashboard

An interactive dashboard was built to demonstrate insights from the dataset.  
Features include:

### **Filters**
- Product Category  
- State  
- Payment Method  

### **Key Metrics**
- Total Revenue  
- Average Rating  
- Delivery Success Rate  

### **Visualizations**
- Sales by Product Category  
- Rating Behavior by Delivery Status  
- Revenue by Payment Method  
- Monthly Revenue Trend  

---

## How to Run the Streamlit App

### **1. Create the Streamlit environment (only once)**  
```bash
conda create -n streamlit311 python=3.11
conda activate streamlit311
pip install streamlit plotly pandas numpy seaborn matplotlib

# Marketing Analytics Dashboard

## Project Overview

This project analyzes marketing performance for a fictional e-commerce company, **Shop Easy**, using SQL, Python, and Power BI. The objective was to identify factors affecting customer engagement, conversion rates, and customer satisfaction while providing actionable business insights.

---

## Business Problem

Shop Easy experienced:

* Declining customer engagement
* Lower conversion rates
* Increasing marketing expenses
* Customer feedback scores below target

The goal was to transform raw marketing data into meaningful insights to support data-driven decision-making.

---

## Tools & Technologies

* SQL Server
* SQL (CTEs, Window Functions, Joins, CASE Statements)
* Python
* Pandas
* NLTK (VADER Sentiment Analysis)
* PyODBC
* Power BI
* DAX
* Power Query

---

## Project Workflow

### 1. Data Cleaning & Transformation (SQL)

* Categorized products into price segments
* Merged customer and geography data
* Cleaned customer review text
* Standardized engagement data
* Removed duplicate customer journey records
* Handled missing duration values using window functions

### 2. Sentiment Analysis (Python)

* Connected Python directly to SQL Server
* Extracted customer reviews
* Generated:

  * Sentiment Score
  * Sentiment Category
  * Sentiment Bucket
* Exported enriched review dataset for reporting

### 3. Dashboard Development (Power BI)

Built an interactive dashboard with:

* Executive Overview
* Conversion Funnel Analysis
* Customer Engagement Analysis
* Customer Review & Sentiment Analysis

---

## Key Insights

* Identified customer drop-off points in the conversion funnel
* Measured engagement across different content types
* Analyzed customer sentiment beyond star ratings
* Highlighted opportunities to improve marketing effectiveness and customer satisfaction

---

## Project Structure

```text
Marketing Analytics Dashboard
│
├── SQL_scripts/
├── Sentiment_Analysis.py
├── customer_reviews_with_sentiment.csv
├── marketing_dashboard.pbix
├── Buisiness Presentation.pptx
└── Marketing Analytics Business Case (Clean).pptx
```

---

## Files Included

| File                                           | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| SQL_scripts                                    | SQL queries for data cleaning and transformation |
| Sentiment_Analysis.py                          | Python script for sentiment analysis             |
| customer_reviews_with_sentiment.csv            | Enriched customer review dataset                 |
| marketing_dashboard.pbix                       | Interactive Power BI dashboard                   |
| Buisiness Presentation.pptx                    | Final business presentation                      |
| Marketing Analytics Business Case (Clean).pptx | Original business case document                  |

---

## Author

**Supratim Mukherjee**

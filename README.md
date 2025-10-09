# 🏥 Hospital CFO Analysis with Snowflake

Welcome to the **Hospital CFO Analysis** project! This repository contains realistic hospital datasets and strategic business questions designed for financial analysis using **Snowflake**. 📊

---

## 📘 Project Overview

This project simulates a hospital's operational and financial data to help CFOs make data-driven decisions. It includes:
- Patient admissions
- Department expenses
- Staff salaries
- Medical equipment inventory
- Insurance claims

The goal is to analyze these datasets using SQL in Snowflake and answer key financial and operational questions.

---

## 📂 Datasets

1. **Patient Admissions**  
   `Admission_ID`, `Patient_ID`, `Department`, `Admission_Date`, `Discharge_Date`, `Diagnosis`, `Treatment_Cost`

2. **Department Expenses**  
   `Department`, `Month`, `Operational_Cost`, `Staff_Cost`, `Equipment_Cost`, `Total_Expense`

3. **Staff Salaries**  
   `Staff_ID`, `Name`, `Role`, `Department`, `Monthly_Salary`, `Bonus`, `Total_Compensation`

4. **Medical Equipment Inventory**  
   `Equipment_ID`, `Name`, `Department`, `Purchase_Date`, `Cost`, `Maintenance_Cost`, `Status`

5. **Insurance Claims**  
   `Claim_ID`, `Patient_ID`, `Insurance_Provider`, `Claim_Amount`, `Approved_Amount`, `Claim_Status`, `Submission_Date`

---

## ❓ Business Questions

### 💰 Financial Performance
1. What is the total monthly expense per department?
2. Which departments have the highest operational costs?
3. What is the average cost per patient admission?
4. How much revenue is lost due to rejected insurance claims?
5. What is the approval rate of insurance claims by provider?

### 👩‍⚕️ Human Resources
6. What is the total monthly salary expenditure?
7. Which roles have the highest compensation?
8. Are there departments with high staff costs vs. patient volume?
9. What is the staff-to-patient ratio?
10. How does salary correlate with department performance?

### 🏥 Operational Efficiency
11. What is the average length of stay per department?
12. Which departments have the highest patient turnover?
13. Are there seasonal trends in admissions?
14. How many equipment items are out of service?
15. What is the average maintenance cost per equipment type?

### 📈 Strategic Planning
16. Which departments are overspending?
17. What is the ROI on equipment purchases?
18. How do claim amounts compare to treatment costs?
19. Are there diagnosis patterns suggesting resource reallocation?
20. What percentage of expenses are salaries vs. equipment vs. operations?

---

## 🛠️ Tools Used

- **Snowflake** ❄️ for data warehousing and SQL analysis  
- **SQL** for querying and insights  
- **Python** 🐍 for data generation and preprocessing  
- **GitHub** for version control and collaboration  

---

## 🚀 How to Run the Analysis

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/hospital-cfo-analysis-snowflake.git

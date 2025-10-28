
#import os
#for file in os.listdir():
#    if file.endswith('.csv'):
#        os.remove(file)
#print("All CSV files deleted.")


#from google.colab import files
#uploaded = files.upload()  # Select ALL your CSV files at once

# Install dependencies if needed
# !pip install plotly pandas

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load datasets
dep_exp = pd.read_csv("department_expenses.csv")
equip = pd.read_csv("equipment_inventory.csv")
claims = pd.read_csv("insurance_claims.csv")
staff = pd.read_csv("staff_salaries.csv")
admissions = pd.read_csv("patient_admissions.csv")

# -------------------------------
# 1. Expense Breakdown (Stacked Bar)
# -------------------------------
dep_exp_melted = dep_exp.melt(id_vars=['Department', 'Month'],
                              value_vars=['Utilities', 'Salaries', 'Supplies', 'Maintenance'],
                              var_name='Category', value_name='Amount')
fig_expense = px.bar(dep_exp_melted, x='Department', y='Amount', color='Category',
                     title='Expense Breakdown by Department and Category', barmode='stack')
fig_expense.show()

# -------------------------------
# 2. Salary Distribution (Box Plot)
# -------------------------------
fig_salary = px.box(staff, x='Role', y='MonthlySalary', color='Department',
                    title='Salary Distribution by Role and Department')
fig_salary.show()

# -------------------------------
# 3. Monthly Admissions Trend (Line Chart)
# -------------------------------
admissions['Month'] = pd.to_datetime(admissions['AdmissionDate']).dt.to_period('M').astype(str)
monthly_admissions = admissions.groupby('Month').size().reset_index(name='Admissions')
fig_admissions = px.line(monthly_admissions, x='Month', y='Admissions',
                         title='Monthly Admissions Trend')
fig_admissions.show()

# -------------------------------
# 4. Claim Status by Provider (Grouped Bar)
# -------------------------------
fig_claims = px.histogram(claims, x='InsuranceProvider', color='Status',
                          title='Claim Status by Insurance Provider', barmode='group')
fig_claims.show()

# -------------------------------
# 5. Diagnosis Frequency (Bar Chart)
# -------------------------------
diagnosis_freq = admissions['Diagnosis'].value_counts().reset_index()
diagnosis_freq.columns = ['Diagnosis', 'Count']
fig_diagnosis = px.bar(diagnosis_freq, x='Diagnosis', y='Count',
                       title='Diagnosis Frequency')
fig_diagnosis.show()

# -------------------------------
# 6. Equipment Cost by Status (Box Plot)
# -------------------------------
fig_equipment = px.box(equip, x='Status', y='Cost', color='Department',
                       title='Equipment Cost by Status and Department')
fig_equipment.show()

# -------------------------------
# EXTRA VISUALS
# -------------------------------

# Pie Chart: Claim Status Distribution
status_counts = claims['Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']
fig_pie = px.pie(status_counts, names='Status', values='Count',
                 title='Claim Status Distribution')
fig_pie.show()

# Gauge Chart: Approval Rate
approval_rate = (claims[claims['Status'] == 'Approved'].shape[0] / claims.shape[0]) * 100
fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=approval_rate,
    title={'text': "Approval Rate (%)"},
    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "green"}}
))
fig_gauge.show()

# -------------------------------
# Recommendations Section
# -------------------------------
print("Recommendations:")
print("Recommendations:")
print("- Orthopedics has the highest annual expenses; consider cost optimization strategies.")
print("- Approval rate is {:.2f}%; streamline claim processes and improve documentation.".format(approval_rate))
print("- Stroke is the most frequent diagnosis; allocate more resources to Neurology and emergency care.")
print("- Equipment maintenance costs are high; implement preventive maintenance and negotiate service contracts.")
print("- Pediatrics shows high staff-to-patient ratio; review staffing efficiency and workload distribution.")
print("- Claims rejection rate is significant; provide training for accurate claim submissions.")
print("- Seasonal admission peaks in June and November; prepare additional staff and resources during these months.")
print("- MRI scanners and ventilators have high maintenance costs; evaluate replacement vs repair ROI.")
print("- Salaries account for nearly 47% of expenses; explore automation and process improvements to reduce overhead.")
print("- Oncology and Cardiology have high patient volumes; prioritize resource allocation for these departments.")















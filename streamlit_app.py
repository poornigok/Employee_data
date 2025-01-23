import streamlit as st
import pandas as pd
import plotly.express as px

# Load fake employee data
employees = pd.read_csv('employee.csv')

# App title
st.set_page_config(page_title="Employee Dashboard")
st.title("Employee Dashboard")

# Sidebar filters
st.sidebar.title("Filters")
department_filter = st.sidebar.multiselect("Select Department", employees["department"].unique())
gender_filter = st.sidebar.multiselect("Select Gender", employees["gender"].unique())

# Filter data based on selections
filtered_employees = employees[
    (employees["department"].isin(department_filter)) &
    (employees["gender"].isin(gender_filter))
]

# Display filtered data
st.subheader("Employee Data")
st.write(filtered_employees)

# Visualizations
st.subheader("Visualizations")

# Age distribution
fig_age = px.histogram(filtered_employees, x="age", nbins=20, title="Age Distribution")
st.plotly_chart(fig_age, use_container_width=True)

# Salary by department
fig_salary = px.bar(filtered_employees, x="department", y="salary", color="gender", title="Salary by Department")
st.plotly_chart(fig_salary, use_container_width=True)

# Years of experience by gender
fig_experience = px.box(filtered_employees, x="gender", y="years_of_experience", title="Years of Experience by Gender")
st.plotly_chart(fig_experience, use_container_width=True)

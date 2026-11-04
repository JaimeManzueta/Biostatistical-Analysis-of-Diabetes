Diabetes Analysis & Dashboard



📊 Core Project Work: Power BI Desktop

All primary analytics, data modeling, and dashboard construction were handled directly inside Power BI:

1. Data Engineering & Cleansing (Power Query)

Zero-Value Treatment: Identified non-physiological zero values (0) in clinical measurement fields (Glucose, BMI, Insulin) and transformed them to null values within Power Query to prevent placeholder data from distorting statistical averages.

2. Analytical Measures (DAX)

Total Patients (768): Authored a DAX measure (COUNTROWS) to establish the baseline sample cohort size.

Diabetes Rate (34.9%): Constructed explicit DAX logic (DIVIDE with CALCULATE filtered for Outcome = 1) to calculate and format the overall diabetes positivity rate for executive reporting.

3. Visual Engineering & Custom Layout

Average Glucose by Outcome (Clustered Column Chart): Mapped Age (X-axis) against Average Glucose (Y-axis) broken down by Outcome. Adjusted field aggregation from Sum to Average to accurately surface baseline glucose elevation in diabetic patients across all age brackets.

Insulin vs. Glucose Distribution (Scatter Plot): Built an interactive scatter plot using Insulin (X-axis), Glucose (Y-axis), BMI (Marker Size), and Outcome (Legend). Disabled field summarization (Don't Summarize) to plot individual patient records, highlighting clusters of insulin resistance across BMI levels.

Interactive Controls & Layout Polish: Integrated dynamic slicers for Outcome and Age, standardized chart titles, aligned axes, and applied consistent visual styling across the report canvas.


Dashboard: 
[Diabetes Risk Analysis & Patient Overview.pdf](https://github.com/user-attachments/files/34354804/Diabetes.Risk.Analysis.Patient.Overview.pdf)



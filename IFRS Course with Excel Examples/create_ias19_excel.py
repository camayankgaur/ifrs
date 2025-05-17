import pandas as pd

# Create a DataFrame for IAS 19 - Employee Benefits
data_ias19 = {
    'Benefit Type': [
        'Short-term Employee Benefits - Salaries and Wages',
        'Short-term Employee Benefits - Paid Annual Leave',
        'Post-employment Benefits - Defined Contribution Plan',
        'Post-employment Benefits - Defined Benefit Plan (Actuarial Valuation Components)',
        'Post-employment Benefits - Defined Benefit Plan (Remeasurements in OCI)',
        'Other Long-term Employee Benefits - Long-service Leave',
        'Termination Benefits'
    ],
    'Description': [
        'Salaries and wages accrued for services rendered by employees during the reporting period.',
        'Cost of paid annual leave expected to be taken by employees.',
        'Company F contributes a fixed percentage (e.g., 5%) of employee salaries to a separate fund. The company has no further obligation once contributions are paid.',
        'Company F has a defined benefit pension plan. Key components include: Service Cost (current and past), Net Interest on Net Defined Benefit Liability/Asset.',
        'Actuarial gains/losses arising from changes in actuarial assumptions (e.g., discount rate, salary escalation, mortality rates) and experience adjustments related to the defined benefit plan.',
        'Benefits payable to employees after a specified period of service (e.g., 10 years). The obligation is measured using projected unit credit method, similar to defined benefit plans, but remeasurements are recognized in P&L.',
        'Benefits provided in exchange for termination of an employee\'s employment, either by entity decision or employee decision to accept an offer of benefits in exchange for termination.'
    ],
    'Accounting Treatment under IAS 19': [
        'Recognize as an expense (and a liability if unpaid) in the period the service is rendered.',
        'Recognize as an expense (and a liability) as employees render service that increases their entitlement.',
        'Recognize contributions as an expense in the period they are due. No complex actuarial valuation required.',
        'Service cost is recognized in profit or loss. Net interest on the net defined benefit liability (asset) is recognized in profit or loss (calculated using the discount rate).',
        'Remeasurements (actuarial gains/losses, return on plan assets excluding net interest, effect of asset ceiling excluding net interest) are recognized in Other Comprehensive Income (OCI) and are not reclassified to profit or loss in subsequent periods.',
        'The cost is recognized over the service period. The obligation is discounted to present value. Unlike defined benefit post-employment plans, all remeasurements (actuarial gains/losses) are recognized in profit or loss.',
        'Recognize as a liability and an expense when the entity is demonstrably committed to either terminate employment before normal retirement or provide termination benefits as a result of an offer made to encourage voluntary redundancy. Measured at present value if material and payable beyond 12 months.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Salaries Expense: $500,000',
        'Accrued Annual Leave Expense: $20,000',
        'Pension Expense (DC Plan): $25,000 (e.g., 5% of $500,000 salaries)',
        'Service Cost: $60,000; Net Interest Expense: $10,000 (recognized in P&L)',
        'Actuarial Loss of $15,000 recognized in OCI.',
        'Long-service leave expense recognized: $8,000. Actuarial loss on LSL obligation of $2,000 recognized in P&L.',
        'Termination benefits expense: $75,000 for a restructuring plan announced and communicated.'
    ]
}
df_ias19 = pd.DataFrame(data_ias19)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS19_Employee_Benefits_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias19.to_excel(writer, sheet_name='IAS19_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS19_Example']
    for i, col in enumerate(df_ias19.columns):
        column_len = max(df_ias19[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

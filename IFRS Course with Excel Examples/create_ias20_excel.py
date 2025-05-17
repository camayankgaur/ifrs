import pandas as pd

# Create a DataFrame for IAS 20 - Accounting for Government Grants and Disclosure of Government Assistance
data_ias20 = {
    'Scenario Type': [
        'Grant Related to Assets - Deferred Income Method',
        'Grant Related to Assets - Deduction from Asset Cost Method',
        'Grant Related to Income - Recognizing as Income',
        'Repayment of Government Grant (Related to Asset - Deferred Income Method)',
        'Repayment of Government Grant (Related to Income)'
    ],
    'Description': [
        'Company G receives a government grant of $100,000 to purchase a specific machine costing $500,000. The machine has a useful life of 5 years. The company chooses to treat the grant as deferred income.',
        'Alternatively, Company G receives the same $100,000 grant for the $500,000 machine (5-year life) and chooses to deduct the grant from the carrying amount of the asset.',
        'Company G receives a grant of $20,000 to compensate for specific operating expenses incurred in the current period (e.g., training costs for employees in a disadvantaged area).',
        'In year 3, due to non-compliance with a condition, Company G is required to repay $30,000 of the grant received for the machine (originally $100,000, deferred income method). At the time of repayment, the unamortized deferred grant income is $60,000 (original $100,000 - $20,000/year * 2 years).',
        'Company G received a $20,000 grant related to income which was fully recognized in profit or loss in the prior year. In the current year, $5,000 of this grant becomes repayable due to non-fulfillment of a condition.'
    ],
    'Accounting Treatment under IAS 20': [
        'The grant of $100,000 is recognized as deferred income. It is then recognized in profit or loss on a systematic basis over the useful life of the asset (5 years), i.e., $20,000 per year, usually as a reduction of depreciation expense or as other income.',
        'The cost of the machine is reduced to $400,000 ($500,000 - $100,000). Depreciation is then calculated on this reduced amount over its useful life (e.g., $400,000 / 5 years = $80,000 per year).',
        'The grant of $20,000 is recognized in profit or loss in the period the related expenses are incurred. It can be presented as other income or as a deduction from the related expense (e.g., training costs).',
        'The repayment of $30,000 is first applied against any unamortized deferred credit ($60,000). The deferred income balance is reduced to $30,000. If the repayment exceeded the unamortized credit, the excess would be recognized immediately as an expense.',
        'The repayment of $5,000 is recognized as an expense in the current period when the repayment becomes probable and measurable. This is a change in estimate.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Deferred Income: $100,000; Annual P&L recognition: $20,000',
        'Asset Cost: $400,000; Annual Depreciation: $80,000',
        'Income/Reduction in Expense: $20,000',
        'Reduction in Deferred Income: $30,000. Remaining Deferred Income: $30,000.',
        'Expense recognized: $5,000'
    ]
}
df_ias20 = pd.DataFrame(data_ias20)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS20_Government_Grants_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias20.to_excel(writer, sheet_name='IAS20_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS20_Example']
    for i, col in enumerate(df_ias20.columns):
        column_len = max(df_ias20[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

import pandas as pd

# Create a DataFrame for IAS 8 - Accounting Policies, Changes in Accounting Estimates and Errors
data_ias8 = {
    'Scenario Type': [
        'Change in Accounting Policy (Voluntary - Retrospective Application)',
        'Change in Accounting Policy (Required by IFRS - Transitional Provisions)',
        'Change in Accounting Estimate (Prospective Application)',
        'Correction of Prior Period Error (Retrospective Restatement)'
    ],
    'Description': [
        'Company C decides to change its inventory valuation method from weighted average cost to FIFO for better comparability, effective from the current year. This is a voluntary change.',
        'A new IFRS standard is issued requiring a change in how Company C recognizes revenue. The standard provides specific transitional provisions for its first-time application.',
        'Company C changes the estimated useful life of a machine from 10 years to 8 years due to new information about its usage pattern.',
        'Company C discovers that it incorrectly expensed $50,000 of costs in the prior year that should have been capitalized as part of an asset. The prior year financial statements have already been issued.'
    ],
    'Accounting Treatment under IAS 8': [
        'The change is applied retrospectively. Prior period financial statements presented for comparison are restated as if the new policy (FIFO) had always been applied. Opening equity of the earliest period presented is adjusted.',
        'The change is applied in accordance with the specific transitional provisions of the new IFRS. This might be retrospective, modified retrospective, or prospective.',
        'The change in estimate is applied prospectively from the current period. The carrying amount of the asset and future depreciation expense are adjusted in the current and future periods. Prior periods are not restated.',
        'The error is corrected by restating the comparative amounts for the prior period(s) presented in which the error occurred. The opening balances of assets, liabilities, and equity for the earliest prior period presented are restated.'
    ],
    'Illustrative Impact': [
        'If FIFO resulted in a $20,000 higher inventory value for the prior year end, prior year Cost of Sales would decrease by $20,000, Profit would increase by $20,000, and Retained Earnings at the start of the current year would increase by $20,000 (net of tax).',
        'Depends on the specific IFRS standard. For example, if it requires prospective application from a certain date, prior periods are not restated.',
        'If the machine had a carrying amount of $100,000 and 5 years remaining under the old estimate (depreciation $20,000/year), under the new estimate of 3 years remaining (from current year), depreciation would be $100,000 / 3 years = $33,333/year for the current and next 2 years.',
        'Prior year assets would increase by $50,000, prior year expenses would decrease by $50,000, prior year profit would increase by $50,000, and opening retained earnings for the current year would increase by $50,000 (net of tax).'
    ]
}
df_ias8 = pd.DataFrame(data_ias8)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS8_Accounting_Policies_Changes_Estimates_Errors_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias8.to_excel(writer, sheet_name='IAS8_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS8_Example']
    for i, col in enumerate(df_ias8.columns):
        column_len = max(df_ias8[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

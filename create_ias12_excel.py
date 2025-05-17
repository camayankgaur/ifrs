import pandas as pd

# Create a DataFrame for IAS 12 - Income Taxes
data_ias12 = {
    'Scenario': [
        'Current Tax Calculation',
        'Deferred Tax Liability - Taxable Temporary Difference (Asset Revaluation)',
        'Deferred Tax Asset - Deductible Temporary Difference (Provision)',
        'Deferred Tax Asset - Unused Tax Losses',
        'Recognition of Deferred Tax Asset - Probability Assessment'
    ],
    'Description': [
        'Company D has an accounting profit before tax of $500,000. Taxable profit after adjustments (e.g., non-deductible expenses, non-taxable income) is $550,000. The current tax rate is 20%.',
        'Company D revalues an item of Property, Plant, and Equipment (PPE) upwards by $100,000. The tax base of the PPE remains at its original cost. This creates a taxable temporary difference.',
        'Company D recognizes a provision for warranty claims of $50,000. This expense is deductible for tax purposes only when the actual claims are paid in the future. This creates a deductible temporary difference.',
        'Company D has unused tax losses of $200,000 that can be carried forward to offset future taxable profits.',
        'Company D assesses the probability that sufficient future taxable profit will be available against which the unused tax losses ($200,000) and deductible temporary differences (e.g., from warranty provision $50,000) can be utilized.'
    ],
    'Accounting Treatment under IAS 12': [
        'Current tax expense = Taxable profit * Current tax rate = $550,000 * 20% = $110,000. This is recognized as an expense and a liability.',
        'A deferred tax liability is recognized for the taxable temporary difference: $100,000 * 20% (tax rate) = $20,000. This is typically recognized in Other Comprehensive Income if the revaluation was recognized in OCI.',
        'A deferred tax asset is recognized for the deductible temporary difference: $50,000 * 20% (tax rate) = $10,000, provided it is probable that future taxable profit will be available against which it can be utilized.',
        'A deferred tax asset is recognized for unused tax losses: $200,000 * 20% (tax rate) = $40,000, provided it is probable that future taxable profit will be available against which the losses can be utilized.',
        'If it is probable that, say, only $150,000 of future taxable profit will be available to utilize against the total $250,000 of deductible differences and losses, the deferred tax asset recognized would be limited. For example, DTA might be recognized for $150,000 * 20% = $30,000 instead of the full $50,000 ($10,000 + $40,000).'
    ],
    'Illustrative Amount (USD)': [
        110000,
        20000, # DTL
        10000, # DTA
        40000, # DTA from losses
        'Assessment based (e.g., DTA recognized $30,000)'
    ]
}
df_ias12 = pd.DataFrame(data_ias12)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS12_Income_Taxes_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias12.to_excel(writer, sheet_name='IAS12_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS12_Example']
    for i, col in enumerate(df_ias12.columns):
        column_len = max(df_ias12[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

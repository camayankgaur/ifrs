import pandas as pd

# Create a DataFrame for IAS 2 - Inventories
data_ias2 = {
    'Scenario': [
        'Cost of Inventories - Purchase Cost',
        'Cost of Inventories - Conversion Costs (Fixed Production Overheads)',
        'Cost of Inventories - Conversion Costs (Variable Production Overheads)',
        'Net Realizable Value (NRV) - Write-down',
        'Recognition as an Expense - Cost of Goods Sold'
    ],
    'Description': [
        'Company B purchases raw materials for $100,000, including $5,000 import duties and $2,000 transport costs. Trade discounts of $3,000 were received.',
        'Company B incurs fixed production overheads of $50,000 during a period of normal production capacity, producing 10,000 units.',
        'Company B incurs variable production overheads of $3 per unit.',
        'At year-end, finished goods with a cost of $50,000 have an estimated selling price of $60,000, but require $15,000 of modification costs to be saleable.',
        'Company B sells inventory that cost $200,000 for $300,000 during the period.'
    ],
    'Accounting Treatment under IAS 2': [
        'Cost of purchase = $100,000 + $5,000 + $2,000 - $3,000 = $104,000.',
        'Fixed overhead allocated per unit = $50,000 / 10,000 units = $5 per unit.',
        'Variable overhead allocated per unit = $3 per unit. Total conversion cost per unit (example) = $5 (fixed) + $3 (variable) = $8.',
        'NRV = $60,000 (selling price) - $15,000 (costs to complete and sell) = $45,000. Since NRV ($45,000) < Cost ($50,000), inventory is written down by $5,000.',
        'Cost of goods sold of $200,000 is recognized as an expense in the period the related revenue is recognized.'
    ],
    'Amount (USD)': [
        104000,
        5, # Per unit
        3, # Per unit
        -5000, # Write-down
        200000 # Expense
    ]
}
df_ias2 = pd.DataFrame(data_ias2)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS2_Inventories_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias2.to_excel(writer, sheet_name='IAS2_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS2_Example']
    for i, col in enumerate(df_ias2.columns):
        column_len = max(df_ias2[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

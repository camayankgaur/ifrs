import pandas as pd

# Create a DataFrame for IAS 16 - Property, Plant and Equipment
data_ias16 = {
    'Scenario': [
        'Initial Recognition - Cost Model',
        'Depreciation - Straight-Line Method',
        'Revaluation Model - Upwards Revaluation',
        'Revaluation Model - Downwards Revaluation (after previous upward revaluation)',
        'Derecognition - Sale of Asset'
    ],
    'Description': [
        'Company E purchases a machine for $120,000. Installation costs are $5,000, and delivery costs are $2,000. Site preparation costs specifically for the machine are $3,000.',
        'The machine (cost $130,000) has an estimated useful life of 10 years and a residual value of $10,000. Company E uses the straight-line method of depreciation.',
        'Company E applies the revaluation model to its land. Land originally costing $500,000 is revalued to its fair value of $700,000. This is the first revaluation.',
        'In a subsequent year, the land revalued to $700,000 (original cost $500,000, previous revaluation surplus $200,000) is now fair valued at $600,000 due to market changes.',
        'The machine (original cost $130,000, accumulated depreciation $60,000, carrying amount $70,000) is sold for $75,000 cash.'
    ],
    'Accounting Treatment under IAS 16': [
        'Cost of the machine = $120,000 (purchase) + $5,000 (installation) + $2,000 (delivery) + $3,000 (site preparation) = $130,000. This is capitalized as PPE.',
        'Annual depreciation expense = (Cost - Residual Value) / Useful Life = ($130,000 - $10,000) / 10 years = $12,000 per year.',
        'The increase of $200,000 ($700,000 - $500,000) is recognized in Other Comprehensive Income (OCI) and accumulated in equity under the heading Revaluation Surplus.',
        'The decrease of $100,000 ($700,000 - $600,000) is first recognized against the revaluation surplus in OCI to the extent of the credit balance ($200,000). So, revaluation surplus is reduced by $100,000. If the decrease exceeded the surplus, the excess would be recognized in profit or loss.',
        'Gain on sale = Proceeds - Carrying Amount = $75,000 - $70,000 = $5,000. This gain is recognized in profit or loss. The asset and its accumulated depreciation are removed from the statement of financial position.'
    ],
    'Illustrative Amount (USD)': [
        130000,
        12000, # Annual Depreciation
        200000, # Revaluation Surplus in OCI
        -100000, # Reduction in Revaluation Surplus
        5000 # Gain on Sale
    ]
}
df_ias16 = pd.DataFrame(data_ias16)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS16_Property_Plant_Equipment_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias16.to_excel(writer, sheet_name='IAS16_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS16_Example']
    for i, col in enumerate(df_ias16.columns):
        column_len = max(df_ias16[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

import pandas as pd

# Create a DataFrame for IFRS 6 - Exploration for and Evaluation of Mineral Resources
data_ifrs6 = {
    'Scenario': ['Capitalizing Exploration Costs', 'Impairment Testing of Exploration Assets'],
    'Description': [
        'Company A incurs $1,000,000 in exploration and evaluation expenditures in a specific area of interest. These costs meet the criteria for capitalization under IFRS 6.',
        'At the end of the reporting period, Company A assesses its capitalized exploration and evaluation assets for impairment. Facts and circumstances suggest that the carrying amount of an exploration asset of $500,000 may exceed its recoverable amount.'
    ],
    'Accounting Treatment under IFRS 6': [
        'The $1,000,000 is capitalized as an exploration and evaluation asset.',
        'An impairment test is performed. If the recoverable amount is determined to be $300,000, an impairment loss of $200,000 ($500,000 - $300,000) is recognized.'
    ],
    'Amount': [1000000, -200000]
}
df_ifrs6 = pd.DataFrame(data_ifrs6)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IFRS6_Exploration_Evaluation_Mineral_Resources_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ifrs6.to_excel(writer, sheet_name='IFRS6_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IFRS6_Example']
    for i, col in enumerate(df_ifrs6.columns):
        column_len = max(df_ifrs6[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

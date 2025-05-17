import pandas as pd

# Create a DataFrame for IAS 23 - Borrowing Costs
data_ias23 = {
    'Scenario Type': [
        'Qualifying Asset - Capitalization of Borrowing Costs (Specific Borrowing)',
        'Qualifying Asset - Capitalization of Borrowing Costs (General Borrowings)',
        'Commencement of Capitalization',
        'Suspension of Capitalization',
        'Cessation of Capitalization'
    ],
    'Description': [
        'Company I constructs a new factory (a qualifying asset). It takes out a specific loan of $1,000,000 at 8% per annum solely for this construction. Construction period is 1 year. Actual borrowing costs incurred on this loan during the year are $80,000.',
        'Company I also uses its general borrowings (e.g., a general pool of funds with a weighted average cost of capital of 6%) to finance part of the factory construction. Expenditures on the qualifying asset during the year from general funds were $500,000 on average.',
        'Capitalization of borrowing costs commences when: 1) expenditures for the asset are being incurred, 2) borrowing costs are being incurred, and 3) activities necessary to prepare the asset for its intended use or sale are in progress.',
        'During a prolonged period in which active development is interrupted (e.g., due to a major strike stopping construction for 3 months), capitalization of borrowing costs is suspended.',
        'Capitalization of borrowing costs ceases when substantially all the activities necessary to prepare the qualifying asset for its intended use or sale are complete.'
    ],
    'Accounting Treatment under IAS 23': [
        'The actual borrowing costs incurred on the specific loan ($80,000) are capitalized as part of the cost of the factory, less any investment income earned on the temporary investment of those borrowings (if any).',
        'The amount of borrowing costs capitalized from general borrowings is calculated by applying the capitalization rate (6%) to the expenditures on that asset ($500,000 * 6% = $30,000). The total borrowing costs capitalized should not exceed the total borrowing costs incurred during the period.',
        'All three conditions must be met. For example, if funds are borrowed but construction has not started, capitalization does not begin.',
        'Borrowing costs incurred during these 3 months are expensed. Capitalization resumes when active development resumes.',
        'Once the factory is ready for use, further borrowing costs are expensed as incurred, even if the asset is not yet brought into use.'
    ],
    'Illustrative Amount Capitalized/Expensed (USD)': [
        'Capitalized: $80,000 (assuming no temporary investment income)',
        'Capitalized: $30,000',
        'N/A (Condition for commencement)',
        'Borrowing costs for 3 months expensed (e.g., if specific loan interest was $80,000/year, then $80,000 * 3/12 = $20,000 expensed)',
        'N/A (Condition for cessation)'
    ]
}
df_ias23 = pd.DataFrame(data_ias23)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS23_Borrowing_Costs_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias23.to_excel(writer, sheet_name='IAS23_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS23_Example']
    for i, col in enumerate(df_ias23.columns):
        column_len = max(df_ias23[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

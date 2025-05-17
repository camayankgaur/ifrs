import pandas as pd

# Create a DataFrame for IAS 7 - Statement of Cash Flows
data_ias7 = {
    'Cash Flow Activity': [
        'Operating Activities - Direct Method: Cash Inflows',
        'Operating Activities - Direct Method: Cash Outflows',
        'Operating Activities - Indirect Method: Profit before tax',
        'Operating Activities - Indirect Method: Adjustments for non-cash items',
        'Operating Activities - Indirect Method: Changes in working capital',
        'Investing Activities: Purchase of PPE',
        'Investing Activities: Proceeds from sale of equipment',
        'Investing Activities: Purchase of investments',
        'Financing Activities: Proceeds from issuance of shares',
        'Financing Activities: Proceeds from long-term borrowings',
        'Financing Activities: Repayment of long-term borrowings',
        'Financing Activities: Dividends paid'
    ],
    'Example Transaction/Adjustment': [
        'Cash received from customers; Cash received from royalties, fees, commissions',
        'Cash paid to suppliers; Cash paid to employees; Income taxes paid',
        'Profit before income tax as per Statement of Comprehensive Income',
        'Depreciation and amortization; Impairment losses; (Gain)/Loss on sale of PPE; Interest expense (if classified as operating); Interest income (if classified as operating)',
        '(Increase)/Decrease in trade receivables; (Increase)/Decrease in inventories; Increase/(Decrease) in trade payables',
        'Payment for new machinery',
        'Cash received from selling old van',
        'Payment for acquiring shares in another company',
        'Cash received from new share issue',
        'Cash received from bank loan',
        'Principal repayment of bank loan',
        'Cash dividends paid to shareholders'
    ],
    'Illustrative Amount (USD)': [
        '1,500,000; 50,000',
        '-800,000; -300,000; -100,000',
        '430,000 (from IAS 1 example)',
        '50,000 (Depreciation); 10,000 (Amortization); 5,000 (Impairment); -2,000 (Gain on sale); 30,000 (Interest Exp); -10,000 (Interest Inc)',
        '-20,000 (Increase in Receivables); -30,000 (Increase in Inventories); 40,000 (Increase in Payables)',
        '-200,000',
        '15,000',
        '-50,000',
        '100,000',
        '150,000',
        '-70,000',
        '-100,000'
    ]
}
df_ias7 = pd.DataFrame(data_ias7)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS7_Statement_of_Cash_Flows_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias7.to_excel(writer, sheet_name='IAS7_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS7_Example']
    for i, col in enumerate(df_ias7.columns):
        column_len = max(df_ias7[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

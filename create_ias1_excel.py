import pandas as pd

# Create a DataFrame for IAS 1 - Presentation of Financial Statements
data_ias1 = {
    'Financial Statement Element': [
        'Statement of Financial Position (Balance Sheet) - Assets',
        'Statement of Financial Position (Balance Sheet) - Equity',
        'Statement of Financial Position (Balance Sheet) - Liabilities',
        'Statement of Profit or Loss and Other Comprehensive Income - Revenue',
        'Statement of Profit or Loss and Other Comprehensive Income - Cost of Sales',
        'Statement of Profit or Loss and Other Comprehensive Income - Gross Profit',
        'Statement of Profit or Loss and Other Comprehensive Income - Other Income',
        'Statement of Profit or Loss and Other Comprehensive Income - Distribution Costs',
        'Statement of Profit or Loss and Other Comprehensive Income - Administrative Expenses',
        'Statement of Profit or Loss and Other Comprehensive Income - Finance Costs',
        'Statement of Profit or Loss and Other Comprehensive Income - Profit Before Tax',
        'Statement of Profit or Loss and Other Comprehensive Income - Income Tax Expense',
        'Statement of Profit or Loss and Other Comprehensive Income - Profit for the Year',
        'Statement of Changes in Equity - Opening Balance',
        'Statement of Changes in Equity - Total Comprehensive Income for the Year',
        'Statement of Changes in Equity - Dividends Paid',
        'Statement of Changes in Equity - Closing Balance',
        'Statement of Cash Flows - Cash flows from operating activities',
        'Statement of Cash Flows - Cash flows from investing activities',
        'Statement of Cash Flows - Cash flows from financing activities',
        'Statement of Cash Flows - Net increase/decrease in cash and cash equivalents'
    ],
    'Example Item/Component': [
        'Property, Plant and Equipment; Intangible Assets; Inventories; Trade Receivables; Cash and Cash Equivalents',
        'Share Capital; Retained Earnings; Other Reserves',
        'Trade Payables; Loans and Borrowings; Deferred Tax Liabilities',
        'Sale of Goods; Rendering of Services',
        'Direct costs attributable to revenue',
        'Revenue - Cost of Sales',
        'Interest Income; Dividend Income',
        'Salaries of sales staff; Advertising costs',
        'Salaries of admin staff; Rent of office building',
        'Interest expense on loans',
        'Profit after all expenses except tax',
        'Current tax; Deferred tax',
        'Profit Before Tax - Income Tax Expense',
        'Equity at the beginning of the period',
        'Profit for the year + Other Comprehensive Income (e.g., revaluation surplus)',
        'Dividends declared and paid during the year',
        'Equity at the end of the period',
        'Cash received from customers; Cash paid to suppliers and employees',
        'Purchase of property, plant and equipment; Sale of investments',
        'Proceeds from issuance of shares; Repayment of borrowings',
        'Sum of cash flows from operating, investing, and financing activities'
    ],
    'Illustrative Amount (USD)': [
        '1,500,000; 500,000; 300,000; 250,000; 100,000',
        '1,000,000; 800,000; 50,000',
        '200,000; 600,000; 100,000',
        '2,000,000',
        '1,200,000',
        '800,000 (2,000,000 - 1,200,000)',
        '10,000',
        '150,000',
        '200,000',
        '30,000',
        '430,000 (800,000 + 10,000 - 150,000 - 200,000 - 30,000)',
        '86,000 (e.g., 20% of 430,000)',
        '344,000 (430,000 - 86,000)',
        '1,500,000',
        '344,000 (assuming no OCI for simplicity)',
        '100,000',
        '1,744,000 (1,500,000 + 344,000 - 100,000)',
        '500,000',
        '-400,000',
        '50,000',
        '150,000'
    ]
}
df_ias1 = pd.DataFrame(data_ias1)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS1_Presentation_Financial_Statements_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias1.to_excel(writer, sheet_name='IAS1_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS1_Example']
    for i, col in enumerate(df_ias1.columns):
        column_len = max(df_ias1[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

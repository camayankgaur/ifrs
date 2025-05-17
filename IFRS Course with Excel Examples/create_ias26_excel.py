import pandas as pd

# Create a DataFrame for IAS 26 - Accounting and Reporting by Retirement Benefit Plans
data_ias26 = {
    'Disclosure Area': [
        'Statement of Net Assets Available for Benefits - Assets',
        'Statement of Net Assets Available for Benefits - Liabilities',
        'Statement of Net Assets Available for Benefits - Net Assets',
        'Statement of Changes in Net Assets Available for Benefits - Contributions',
        'Statement of Changes in Net Assets Available for Benefits - Investment Income',
        'Statement of Changes in Net Assets Available for Benefits - Benefits Paid',
        'Statement of Changes in Net Assets Available for Benefits - Other Changes',
        'Actuarial Present Value of Promised Retirement Benefits (Defined Benefit Plans - may be in notes or separate report)',
        'Significant Actuarial Assumptions (Defined Benefit Plans)',
        'Investment Policies'
    ],
    'Example Item/Description': [
        'Investments at fair value (e.g., equities, bonds, property); Contributions receivable; Cash and cash equivalents.',
        'Benefits payable; Administrative expenses payable.',
        'Total Assets - Total Liabilities.',
        'Employer contributions; Employee contributions.',
        'Interest income; Dividend income; Realized gains/losses on investments; Unrealized gains/losses on investments (if measured at fair value through P&L equivalent for the plan).',
        'Retirement benefits paid; Lump sum payments; Death benefits paid.',
        'Administrative expenses; Taxes on income of the plan (if applicable); Transfers to/from other plans.',
        'Present value of vested benefits; Present value of non-vested benefits. This is often based on an actuarial valuation.',
        'Discount rate; Expected rates of salary increase; Mortality rates; Retirement ages.',
        'Description of the investment policies of the plan, including policies for diversification, risk management, and valuation of investments.'
    ],
    'Illustrative Value/Note Reference': [
        'Equities: $5,000,000; Bonds: $3,000,000; Cash: $500,000',
        'Benefits Payable: $200,000; Admin Expenses Payable: $50,000',
        'Net Assets: $8,250,000',
        'Employer: $600,000; Employee: $200,000',
        'Interest: $150,000; Dividends: $100,000; Net Realized Gain: $250,000; Net Unrealized Gain: $400,000',
        'Pensions Paid: $300,000; Lump Sums: $100,000',
        'Admin Expenses: $80,000',
        'Actuarial Present Value of Promised Benefits: $7,500,000 (as per actuarial report dated XX/XX/XXXX - Note Y.1)',
        'Discount Rate: 5%; Salary Increase: 3%; Mortality Table: XYZ (Note Y.2)',
        'The plan invests in a diversified portfolio of equities and fixed income securities with a long-term investment horizon... (Note Z)'
    ]
}
df_ias26 = pd.DataFrame(data_ias26)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS26_Accounting_Reporting_Retirement_Benefit_Plans_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias26.to_excel(writer, sheet_name='IAS26_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS26_Example']
    for i, col in enumerate(df_ias26.columns):
        column_len = max(df_ias26[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

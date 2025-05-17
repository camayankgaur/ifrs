import pandas as pd

# Create a DataFrame for IFRS 7 - Financial Instruments: Disclosures
data_ifrs7 = {
    'Disclosure Category': [
        'Significance of Financial Instruments',
        'Nature and Extent of Risks Arising from Financial Instruments - Qualitative',
        'Nature and Extent of Risks Arising from Financial Instruments - Quantitative (Credit Risk)',
        'Nature and Extent of Risks Arising from Financial Instruments - Quantitative (Liquidity Risk)',
        'Nature and Extent of Risks Arising from Financial Instruments - Quantitative (Market Risk - Sensitivity Analysis)'
    ],
    'Example Disclosure Item': [
        'Carrying amounts of each class of financial asset and financial liability.',
        'Exposure to credit risk, liquidity risk, and market risk, and how these risks are managed.',
        'Maximum exposure to credit risk, collateral held, information about credit quality of financial assets.',
        'Maturity analysis for financial liabilities.',
        'Sensitivity analysis for each type of market risk (e.g., interest rate risk, currency risk, other price risk).'
    ],
    'Illustrative Value/Note Reference': [
        'Note X.1: Financial Assets - Loans and Receivables: $5,000,000; Financial Liabilities - Trade Payables: $2,000,000',
        'Note X.2: The company has a comprehensive risk management framework...',
        'Note X.3: Max Credit Exposure: $5,000,000. Collateral: $1,000,000. Past Due but not impaired: $200,000.',
        'Note X.4: Liabilities due within 1 year: $1,500,000; 1-5 years: $500,000.',
        'Note X.5: A 1% increase in interest rates would decrease equity by $50,000. A 10% depreciation in USD would decrease profit by $100,000.'
    ]
}
df_ifrs7 = pd.DataFrame(data_ifrs7)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IFRS7_Financial_Instruments_Disclosures_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ifrs7.to_excel(writer, sheet_name='IFRS7_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IFRS7_Example']
    for i, col in enumerate(df_ifrs7.columns):
        column_len = max(df_ifrs7[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

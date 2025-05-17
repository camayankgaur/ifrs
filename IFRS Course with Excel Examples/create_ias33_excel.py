import pandas as pd

# Create a DataFrame for IAS 33 - Earnings Per Share
data_ias33 = {
    'Scenario Type': [
        'Basic EPS Calculation - Simple Capital Structure',
        'Basic EPS Calculation - Weighted Average Number of Shares (WANOS) - New Issue',
        'Basic EPS Calculation - Weighted Average Number of Shares (WANOS) - Share Buyback',
        'Diluted EPS Calculation - Convertible Debt',
        'Diluted EPS Calculation - Share Options/Warrants',
        'Diluted EPS Calculation - Contingently Issuable Shares'
    ],
    'Description': [
        'Company L has profit attributable to ordinary shareholders of $1,000,000. Number of ordinary shares outstanding throughout the year is 500,000.',
        'Company L has profit attributable to ordinary shareholders of $1,000,000. 500,000 shares were outstanding from Jan 1 to Jun 30. On July 1, an additional 200,000 shares were issued for cash.',
        'Company L has profit attributable to ordinary shareholders of $1,000,000. 700,000 shares were outstanding from Jan 1 to Sep 30. On Oct 1, Company L bought back 100,000 of its own shares.',
        'Company L has profit of $1,000,000 and WANOS of 500,000. It has convertible bonds outstanding that, if converted, would result in the issuance of 100,000 new shares. The after-tax interest expense saved on conversion would be $50,000.',
        'Company L has profit of $1,000,000 and WANOS of 500,000. It has 50,000 share options outstanding with an exercise price of $10. The average market price of ordinary shares during the year was $15.',
        'Company L will issue 100,000 shares if its reported profit next year exceeds $2,000,000. Current year profit is $1,000,000 and WANOS is 500,000. Assume the condition (profit > $2M) is met based on current year-end conditions for diluted EPS calculation purposes if it were a forward-looking condition being assessed.'
    ],
    'Accounting Treatment/Calculation under IAS 33': [
        'Basic EPS = Profit / WANOS = $1,000,000 / 500,000 = $2.00 per share.',
        'WANOS = (500,000 * 6/12) + (700,000 * 6/12) = 250,000 + 350,000 = 600,000 shares. Basic EPS = $1,000,000 / 600,000 = $1.67 per share.',
        'WANOS = (700,000 * 9/12) + (600,000 * 3/12) = 525,000 + 150,000 = 675,000 shares. Basic EPS = $1,000,000 / 675,000 = $1.48 per share.',
        'Adjusted Profit = $1,000,000 + $50,000 = $1,050,000. Adjusted WANOS = 500,000 + 100,000 = 600,000. Incremental EPS for bonds = $50,000 / 100,000 = $0.50. If this is less than Basic EPS ($2.00), they are dilutive. Diluted EPS = $1,050,000 / 600,000 = $1.75.',
        'Proceeds from assumed exercise = 50,000 options * $10 = $500,000. Shares assumed repurchased with proceeds = $500,000 / $15 (avg market price) = 33,333 shares. Incremental shares (dilutive) = 50,000 - 33,333 = 16,667 shares. Diluted WANOS = 500,000 + 16,667 = 516,667. Diluted EPS = $1,000,000 / 516,667 = $1.93. (No adjustment to profit for options).',
        'If the condition for issue is met at the end of the reporting period (or assumed to be met for calculation), the 100,000 shares are included in diluted WANOS. Diluted WANOS = 500,000 + 100,000 = 600,000. Diluted EPS = $1,000,000 / 600,000 = $1.67. (No adjustment to profit).'
    ],
    'Resulting EPS (USD)': [
        'Basic EPS: $2.00',
        'Basic EPS: $1.67',
        'Basic EPS: $1.48',
        'Diluted EPS: $1.75 (assuming dilutive)',
        'Diluted EPS: $1.93 (assuming dilutive)',
        'Diluted EPS: $1.67 (assuming condition met and dilutive)'
    ]
}
df_ias33 = pd.DataFrame(data_ias33)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS33_Earnings_Per_Share_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias33.to_excel(writer, sheet_name='IAS33_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS33_Example']
    for i, col in enumerate(df_ias33.columns):
        column_len = max(df_ias33[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

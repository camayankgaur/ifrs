import pandas as pd

# Create a DataFrame for IAS 34 - Interim Financial Reporting
data_ias34 = {
    'Reporting Area': [
        'Minimum Components of Interim Financial Report',
        'Form and Content of Interim Financial Statements',
        'Significant Events and Transactions',
        'Recognition and Measurement - General Principle',
        'Seasonal, Cyclical, or Occasional Revenue',
        'Costs Incurred Unevenly During the Financial Year',
        'Use of Estimates'
    ],
    'Description': [
        'The minimum components that should be included in an interim financial report according to IAS 34.',
        'The form and content requirements for interim financial statements when a complete set is presented.',
        'Explanation and examples of events and transactions that would require disclosure if significant.',
        'The general principle for recognition and measurement in interim financial reports.',
        'How to account for revenue that is seasonal, cyclical, or occasional in nature.',
        'How to account for costs that are incurred unevenly during the financial year.',
        'The use of estimates in interim financial reporting.'
    ],
    'Requirements/Examples': [
        'Condensed statement of financial position; Condensed statement of profit or loss and OCI; Condensed statement of changes in equity; Condensed statement of cash flows; Selected explanatory notes.',
        'Each of the headings and subtotals included in the most recent annual financial statements and selected explanatory notes. Additional line items or notes if their omission would make the interim financial statements misleading.',
        'Write-down of inventories to net realizable value; Recognition of impairment losses; Restructuring costs; Significant changes in business or economic circumstances affecting fair values; Significant changes in contingent liabilities or assets; Corrections of prior period errors.',
        'Same accounting policies and calculation methods as in annual financial statements. Revenues and costs should be recognized when they occur, not anticipated or deferred. Tax expense recognized based on weighted average annual effective tax rate.',
        'Revenue received seasonally, cyclically, or occasionally should not be anticipated or deferred at interim date. For example, a retailer should not recognize Christmas season revenue in September interim report.',
        'Costs incurred unevenly should not be anticipated or deferred unless it would be appropriate to anticipate or defer at year end. For example, annual bonus should be recognized only when obligation exists at interim date.',
        'Measurement procedures for interim reports may rely more on estimates than annual financial statements. For example, simplified inventory count procedures or simplified calculation methods for pension provisions may be used.'
    ],
    'Illustrative Example': [
        'A company presents a condensed statement of financial position as at June 30, 20X1, comparative statements as at December 31, 20X0, and condensed statements of profit or loss for the six-month periods ended June 30, 20X1 and 20X0.',
        'A company includes all headings and subtotals from its annual statements in its interim statements, plus additional notes on changes in debt and equity, seasonality of operations, unusual items, and changes in estimates.',
        'A company discloses a significant impairment of $500,000 on its manufacturing equipment in Q2 due to technological obsolescence, which was not anticipated in Q1.',
        'A company uses the same inventory valuation method (e.g., FIFO) in its interim report as in its annual statements. It calculates tax expense using an estimated annual effective tax rate of 25%.',
        'A ski resort that earns 70% of its revenue during winter months reports actual revenue earned in each interim period without deferral or anticipation.',
        'Annual marketing costs of $120,000 planned evenly throughout the year are recognized as $30,000 per quarter as incurred, not front-loaded or back-loaded.',
        'A company uses a simplified method to estimate warranty provisions in its interim report, based on historical warranty claim rates, rather than a detailed calculation used for annual reporting.'
    ]
}
df_ias34 = pd.DataFrame(data_ias34)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS34_Interim_Financial_Reporting_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias34.to_excel(writer, sheet_name='IAS34_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS34_Example']
    for i, col in enumerate(df_ias34.columns):
        column_len = max(df_ias34[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

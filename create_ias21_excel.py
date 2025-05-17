import pandas as pd

# Create a DataFrame for IAS 21 - The Effects of Changes in Foreign Exchange Rates
data_ias21 = {
    'Scenario Type': [
        'Initial Recognition - Transaction in Foreign Currency',
        'Reporting at Subsequent Balance Sheet Dates - Monetary Items',
        'Reporting at Subsequent Balance Sheet Dates - Non-Monetary Items (Cost Model)',
        'Reporting at Subsequent Balance Sheet Dates - Non-Monetary Items (Fair Value Model)',
        'Recognition of Exchange Differences - Profit or Loss',
        'Recognition of Exchange Differences - Other Comprehensive Income (OCI) for Net Investment in Foreign Operation',
        'Translation of a Foreign Operation - Functional Currency to Presentation Currency'
    ],
    'Description': [
        'Company H (functional currency USD) purchases goods from a UK supplier for GBP 10,000 on December 1, 20X1. The exchange rate is USD 1.25/GBP.',
        'At December 31, 20X1 (reporting date), the GBP 10,000 payable to the UK supplier is still outstanding. The exchange rate is USD 1.30/GBP.',
        'Company H holds a piece of equipment purchased for EUR 50,000 when the rate was USD 1.10/EUR. It is carried at cost less accumulated depreciation.',
        'Company H holds an investment property measured at fair value. It was acquired for ZAR 1,000,000. At reporting date, its fair value is ZAR 1,200,000. Exchange rates: Acquisition USD 0.060/ZAR; Reporting Date USD 0.065/ZAR.',
        'Exchange differences arising on settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition or in previous financial statements.',
        'Exchange differences arising on a monetary item that forms part of an entity\'s net investment in a foreign operation, when the monetary item is denominated in the functional currency of either the reporting entity or the foreign operation.',
        'Company H has a subsidiary in the UK (functional currency GBP). For consolidation, the UK subsidiary\'s financial statements are translated into USD (presentation currency). Assets & Liabilities at closing rate; Income & Expenses at transaction date rates (or average rate if appropriate); Equity at historical rates; Exchange differences to OCI.'
    ],
    'Accounting Treatment under IAS 21': [
        'The transaction is recorded in USD at the spot rate on December 1: GBP 10,000 * USD 1.25/GBP = USD 12,500. (Dr Purchases/Inventory, Cr Trade Payable).',
        'The GBP 10,000 payable (a monetary item) is retranslated using the closing rate: GBP 10,000 * USD 1.30/GBP = USD 13,000. An exchange loss of USD 500 (USD 13,000 - USD 12,500) is recognized in profit or loss.',
        'Non-monetary items measured at historical cost in a foreign currency are translated using the exchange rate at the date of the transaction (historical rate). No subsequent retranslation for exchange rate changes. Depreciation is based on this USD cost.',
        'Non-monetary items measured at fair value in a foreign currency are translated using the exchange rates at the date when the fair value was determined. Fair Value in USD = ZAR 1,200,000 * USD 0.065/ZAR = USD 78,000. The exchange component of the fair value gain is part of the total fair value gain recognized in P&L (for investment property).',
        'Generally recognized in profit or loss in the period in which they arise (e.g., the USD 500 loss on the trade payable).',
        'Recognized in Other Comprehensive Income (OCI) and accumulated in a separate component of equity. Not reclassified to profit or loss on disposal of the net investment until the disposal of the foreign operation itself.',
        'Assets and liabilities are translated at the closing rate at the date of the statement of financial position. Income and expenses are translated at exchange rates at the dates of the transactions (or average rate). All resulting exchange differences are recognized in OCI.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Trade Payable: USD 12,500',
        'Exchange Loss: USD 500; Trade Payable restated to USD 13,000',
        'Equipment Cost in USD remains at EUR 50,000 * USD 1.10/EUR = USD 55,000',
        'Fair Value Gain in P&L: USD 78,000 (FV at reporting) - (ZAR 1,000,000 * USD 0.060/ZAR = USD 60,000 (Historical Cost in USD)) = USD 18,000. This includes both value change and FX change.',
        'Exchange Loss of USD 500 in P&L.',
        'Exchange gain/loss on intercompany loan forming part of net investment recognized in OCI.',
        'Cumulative Translation Adjustment (CTA) in OCI reflecting the net effect of translating the foreign operation.'
    ]
}
df_ias21 = pd.DataFrame(data_ias21)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS21_Effects_Changes_Foreign_Exchange_Rates_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias21.to_excel(writer, sheet_name='IAS21_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS21_Example']
    for i, col in enumerate(df_ias21.columns):
        column_len = max(df_ias21[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

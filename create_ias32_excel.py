import pandas as pd

# Create a DataFrame for IAS 32 - Financial Instruments: Presentation
data_ias32 = {
    'Scenario Type': [
        'Classification - Financial Liability vs. Equity (Mandatorily Redeemable Preference Shares)',
        'Classification - Financial Liability vs. Equity (Puttable Instrument)',
        'Compound Financial Instrument - Convertible Bond (Split Accounting)',
        'Offsetting Financial Assets and Financial Liabilities - Criteria',
        'Treasury Shares'
    ],
    'Description': [
        'Company K issues preference shares that are mandatorily redeemable by the issuer for a fixed or determinable amount at a fixed or determinable future date.',
        'Company K issues financial instruments that give the holder the right to put the instrument back to the issuer for cash or another financial asset (a puttable instrument).',
        'Company K issues a convertible bond with a principal of $1,000,000, which can be converted into a fixed number of ordinary shares at the option of the holder. The bond pays annual interest. Similar bonds without a conversion option have a market interest rate higher than the coupon rate of the convertible bond.',
        'Company K has a financial asset (e.g., a receivable from Customer A) and a financial liability (e.g., a payable to Customer A). Company K intends to settle on a net basis or simultaneously.',
        'Company K reacquires its own equity shares (treasury shares) from the market.'
    ],
    'Accounting Treatment under IAS 32': [
        'These preference shares are classified as a financial liability because the issuer has a contractual obligation to deliver cash.',
        'Puttable instruments are generally classified as financial liabilities. However, they may be classified as equity if they meet specific criteria (e.g., represent a residual interest, total cash flows based substantially on P&L/NAV, no other instrument has priority, etc.).',
        'The convertible bond is a compound financial instrument with both a liability component (contractual obligation to pay cash) and an equity component (option to convert into shares). The proceeds are allocated first to the liability component (fair value of a similar bond without conversion option), and the residual amount to the equity component.',
        'A financial asset and a financial liability shall be offset and the net amount presented in the statement of financial position when, and only when, an entity: (a) currently has a legally enforceable right to set off the recognized amounts; and (b) intends either to settle on a net basis, or to realize the asset and settle the liability simultaneously.',
        'If an entity reacquires its own equity instruments, those instruments (treasury shares) shall be deducted from equity. No gain or loss shall be recognized in profit or loss on the purchase, sale, issue or cancellation of an entity’s own equity instruments.'
    ],
    'Illustrative Impact/Classification': [
        'Classification: Financial Liability. Interest/dividends recognized as finance cost in P&L.',
        'Typically Financial Liability. If equity criteria met: Equity. Dividends from equity classified instruments are distributions of profit.',
        'Liability Component: e.g., $900,000 (PV of future cash flows discounted at market rate for similar non-convertible debt). Equity Component (Conversion Option): $100,000 (Proceeds $1,000,000 - Liability $900,000).',
        'If criteria met: Net receivable/payable presented. If not met: Gross presentation of asset and liability.',
        'Treasury shares are presented as a deduction from total equity. For example, if $50,000 of shares are reacquired, equity is reduced by $50,000.'
    ]
}
df_ias32 = pd.DataFrame(data_ias32)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS32_Financial_Instruments_Presentation_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias32.to_excel(writer, sheet_name='IAS32_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS32_Example']
    for i, col in enumerate(df_ias32.columns):
        column_len = max(df_ias32[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

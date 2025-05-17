import pandas as pd

# Create a DataFrame for IAS 27 - Separate Financial Statements
data_ias27 = {
    'Scenario Type': [
        'Investment in Subsidiary - Cost Method in Separate Financial Statements',
        'Investment in Subsidiary - IFRS 9 Method in Separate Financial Statements',
        'Investment in Associate - Equity Method (Not permitted in Separate FS under IAS 27, but for context if elected under IAS 28)',
        'Investment in Joint Venture - Cost Method in Separate Financial Statements',
        'Dividends Received from Subsidiary in Separate Financial Statements'
    ],
    'Description': [
        'Parent P holds an investment in Subsidiary S. In its separate financial statements, Parent P accounts for this investment at cost. Cost is $1,000,000.',
        'Alternatively, Parent P accounts for its investment in Subsidiary S in accordance with IFRS 9 (e.g., at fair value through profit or loss - FVTPL, or fair value through other comprehensive income - FVOCI). Initial cost was $1,000,000, fair value at reporting date is $1,200,000.',
        'Parent P holds an investment in Associate A. While IAS 27 requires cost or IFRS 9 for associates in separate FS, if an entity elects to use the equity method for associates in its separate FS (as permitted by an amendment to IAS 28), it would apply IAS 28. (This is more of an IAS 28 point but relevant context).',
        'Parent P holds an investment in Joint Venture J. In its separate financial statements, Parent P accounts for this investment at cost. Cost is $300,000.',
        'Parent P receives a dividend of $50,000 from Subsidiary S during the year. Subsidiary S declared this dividend from post-acquisition profits.'
    ],
    'Accounting Treatment under IAS 27 (Separate Financial Statements)': [
        'Investment in Subsidiary S is carried at $1,000,000. Dividends from S are recognized in profit or loss in P’s separate financial statements when P’s right to receive the dividend is established.',
        'If FVTPL: Investment in Subsidiary S is carried at $1,200,000. The fair value gain of $200,000 ($1,200,000 - $1,000,000) is recognized in profit or loss. Dividends are recognized as income. If FVOCI: Investment at $1,200,000, FV gain of $200,000 in OCI. Dividends typically recognized in P&L.',
        'Under IAS 27, the choice is cost or IFRS 9. If the equity method is elected under IAS 28 for separate FS, then IAS 28 applies (investment adjusted for share of post-acquisition profit/loss, dividends reduce carrying amount).',
        'Investment in Joint Venture J is carried at $300,000. Dividends from J are recognized in profit or loss in P’s separate financial statements when P’s right to receive the dividend is established.',
        'Parent P recognizes dividend income of $50,000 in its profit or loss for the year in its separate financial statements.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Investment in S: $1,000,000 (at cost)',
        'Investment in S: $1,200,000 (at FV). P&L Gain: $200,000 (if FVTPL). OCI Gain: $200,000 (if FVOCI).',
        'N/A under pure IAS 27 choice; if IAS 28 equity method elected: Investment in A adjusted by share of profit/loss.',
        'Investment in J: $300,000 (at cost)',
        'Dividend Income: $50,000 in P&L'
    ]
}
df_ias27 = pd.DataFrame(data_ias27)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS27_Separate_Financial_Statements_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias27.to_excel(writer, sheet_name='IAS27_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS27_Example']
    for i, col in enumerate(df_ias27.columns):
        column_len = max(df_ias27[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

import pandas as pd

# Create a DataFrame for IAS 28 - Investments in Associates and Joint Ventures
data_ias28 = {
    'Scenario Type': [
        'Initial Recognition of Investment in Associate (Cost)',
        'Applying the Equity Method - Share of Profit',
        'Applying the Equity Method - Share of Loss',
        'Applying the Equity Method - Dividends Received',
        'Impairment of Investment in Associate',
        'Discontinuing the Equity Method (Loss of Significant Influence)'
    ],
    'Description': [
        'Investor J acquires a 25% interest in Associate K for $200,000 cash, gaining significant influence. Transaction costs are $5,000.',
        'In Year 1, Associate K reports a profit of $80,000. Investor J uses the equity method.',
        'In Year 2, Associate K reports a loss of $40,000. Investor J uses the equity method.',
        'In Year 2, Associate K declares and pays a dividend. Investor J receives $5,000.',
        'At the end of Year 2, there are indications that the investment in Associate K may be impaired. The recoverable amount of the investment is estimated to be $180,000. Carrying amount before impairment is $200,000 (initial) + $5,000 (txn cost) + $20,000 (share of Y1 profit) - $10,000 (share of Y2 loss) - $5,000 (dividend) = $210,000.',
        'In Year 3, Investor J sells 15% of its interest in Associate K, reducing its holding to 10% and losing significant influence. The remaining investment is accounted for under IFRS 9.'
    ],
    'Accounting Treatment under IAS 28': [
        'The investment is initially recognized at cost, which includes transaction costs. Cost = $200,000 + $5,000 = $205,000.',
        'Investor J recognizes its share of Associate K’s profit: 25% * $80,000 = $20,000. This increases the carrying amount of the investment and is recognized in Investor J’s profit or loss.',
        'Investor J recognizes its share of Associate K’s loss: 25% * $40,000 = $10,000. This decreases the carrying amount of the investment and is recognized in Investor J’s profit or loss.',
        'Dividends received from an associate reduce the carrying amount of the investment. Carrying amount is reduced by $5,000.',
        'Carrying amount ($210,000) > Recoverable amount ($180,000). An impairment loss of $30,000 is recognized in profit or loss, reducing the carrying amount of the investment to $180,000.',
        'The equity method is discontinued from the date significant influence is lost. The carrying amount of the investment at that date is regarded as its deemed cost on initial recognition as a financial asset under IFRS 9. Any difference between the carrying amount of the part sold plus the fair value of the retained interest, and the proceeds from sale, is recognized in P&L.'
    ],
    'Illustrative Carrying Amount/P&L Impact (USD)': [
        'Investment in Associate K: $205,000',
        'P&L: +$20,000 (Share of profit); Investment: $205,000 + $20,000 = $225,000',
        'P&L: -$10,000 (Share of loss); Investment: $225,000 - $10,000 = $215,000',
        'Investment: $215,000 - $5,000 = $210,000',
        'P&L: -$30,000 (Impairment loss); Investment: $180,000',
        'The remaining 10% interest is measured at fair value under IFRS 9. Gain/loss on disposal of 15% and remeasurement of retained interest recognized in P&L.'
    ]
}
df_ias28 = pd.DataFrame(data_ias28)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS28_Investments_Associates_Joint_Ventures_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias28.to_excel(writer, sheet_name='IAS28_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS28_Example']
    for i, col in enumerate(df_ias28.columns):
        column_len = max(df_ias28[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

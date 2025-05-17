import pandas as pd

# Create a DataFrame for IAS 10 - Events After the Reporting Period
data_ias10 = {
    'Event Type': [
        'Adjusting Event - Settlement of a court case\n',
        'Adjusting Event - Bankruptcy of a major customer\n',
        'Adjusting Event - Discovery of fraud or errors\n',
        'Non-Adjusting Event - Decline in market value of investments\n',
        'Non-Adjusting Event - Major business combination or disposal\n',
        'Non-Adjusting Event - Destruction of a major asset by fire\n',
        'Non-Adjusting Event - Dividends declared (if declaration is after reporting date)\n'
    ],
    'Description': [
        'A court case was ongoing at the reporting date. After the reporting date but before financial statements are authorized for issue, the case is settled, confirming the entity had a present obligation at the reporting date. The settlement amount differs from the previously recognized provision.\n',
        'A major customer, whose balance was outstanding at the reporting date, declares bankruptcy after the reporting date. This provides additional evidence of the irrecoverability of the trade receivable at the reporting date.\n',
        'Fraud or errors are discovered after the reporting date that show the financial statements are incorrect.\n',
        'The market value of investments held by the entity declines significantly after the reporting date but before financial statements are authorized for issue. This reflects conditions that arose after the reporting date.\n',
        'The entity announces a plan to acquire a major subsidiary or dispose of a major segment after the reporting date.\n',
        'A major production facility is destroyed by fire after the reporting date.\n',
        'Dividends are declared by the entity after the reporting date but before the financial statements are authorized for issue.\n'
    ],
    'Accounting Treatment under IAS 10': [
        'Adjust the amounts recognized in the financial statements (e.g., the provision for the court case) to reflect the new information.\n',
        'Adjust the carrying amount of the trade receivable to reflect the estimated irrecoverable amount (e.g., recognize or increase bad debt provision).\n',
        'Correct the financial statements for the fraud or errors (retrospective restatement if material prior period error).\n',
        'Do not adjust the amounts recognized in the financial statements. However, if material, disclose the nature of the event and an estimate of its financial effect (or a statement that such an estimate cannot be made).\n',
        'Do not adjust the amounts recognized in the financial statements. Disclose if material.\n',
        'Do not adjust the amounts recognized in the financial statements. Disclose if material (e.g., impairment considerations for future periods).\n',
        'Do not recognize these dividends as a liability at the reporting date. Disclose the dividends in the notes to the financial statements.\n'
    ],
    'Illustrative Financial Impact (if adjusting)': [
        'Provision for legal settlement increased by $50,000 based on final court ruling.\n',
        'Allowance for doubtful accounts increased by $100,000 for bankrupt customer.\n',
        'Prior year revenue overstated by $200,000 due to error, requiring restatement.\n',
        'N/A (Non-adjusting)\n',
        'N/A (Non-adjusting)\n',
        'N/A (Non-adjusting)\n',
        'N/A (Non-adjusting) - Liability not recognized at reporting date.\n'
    ]
}
df_ias10 = pd.DataFrame(data_ias10)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS10_Events_After_Reporting_Period_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias10.to_excel(writer, sheet_name='IAS10_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS10_Example']
    for i, col in enumerate(df_ias10.columns):
        column_len = max(df_ias10[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

import pandas as pd

# Create a DataFrame for IAS 24 - Related Party Disclosures
data_ias24 = {
    'Disclosure Category': [
        'Parent-Subsidiary Relationship Disclosure',
        'Key Management Personnel (KMP) Compensation - Total',
        'Key Management Personnel (KMP) Compensation - Categories',
        'Transactions with Related Parties - Nature and Amount',
        'Transactions with Related Parties - Outstanding Balances',
        'Terms and Conditions of Transactions with Related Parties',
        'Government-Related Entities - Exemption (if applicable and used)'
    ],
    'Example Disclosure Item/Description': [
        'Name of the parent entity and, if different, the ultimate controlling party. If neither the parent nor the ultimate controlling party produces consolidated financial statements available for public use, the name of the next most senior parent that does so shall also be disclosed.',
        'Total compensation paid or payable to KMP for employee services (salaries, short-term benefits, post-employment benefits, other long-term benefits, termination benefits, share-based payments).',
        'Breakdown of KMP compensation into categories: short-term employee benefits, post-employment benefits, other long-term benefits, termination benefits, and share-based payment.',
        'Nature of the related party relationship (e.g., subsidiary, associate, joint venture, KMP). Description of transactions (e.g., sales of goods, purchases of services, loans provided, leases). Amount of the transactions.',
        'Amounts of outstanding balances with related parties at the reporting date, including commitments. Details of any guarantees given or received.',
        'Terms and conditions of transactions, including whether they are secured, and the nature of the consideration to be provided in settlement. Details of any provisions for doubtful debts related to outstanding balances.',
        'If an entity is a government-related entity, it is exempt from some disclosure requirements for transactions with other government-related entities if certain conditions are met. If the exemption is applied, specific disclosures about the nature and extent of these transactions are still required.'
    ],
    'Illustrative Example/Value': [
        'Parent: Alpha Corp. Ultimate Controlling Party: Alpha Holdings Inc. Alpha Holdings Inc. produces publicly available consolidated financial statements.',
        'Total KMP Compensation for the year: $1,200,000.',
        'Short-term benefits: $800,000; Post-employment benefits: $200,000; Share-based payments: $150,000; Other long-term benefits: $50,000.',
        'Sale of goods to Subsidiary X: $500,000. Loan to Associate Y: $100,000 at 5% interest. Management services provided by Parent Alpha Corp: $50,000.',
        'Receivable from Subsidiary X: $150,000 (unsecured, interest-free, repayable on demand). Loan receivable from Associate Y: $100,000 (secured by assets of Associate Y).',
        'Sales to Subsidiary X are made at normal market prices. The loan to Associate Y is repayable in 3 years. No provision for doubtful debts has been made for these balances.',
        'The entity is a government-related entity and has applied the exemption in IAS 24 for transactions with other government-related entities. Significant transactions include deposits with a state-owned bank and utility services from a state-owned provider.'
    ]
}
df_ias24 = pd.DataFrame(data_ias24)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS24_Related_Party_Disclosures_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias24.to_excel(writer, sheet_name='IAS24_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS24_Example']
    for i, col in enumerate(df_ias24.columns):
        column_len = max(df_ias24[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

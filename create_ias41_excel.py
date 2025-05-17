import pandas as pd

# Create a DataFrame for IAS 41 - Agriculture
data_ias41 = {
    'Scenario Type': [
        'Recognition - Biological Asset',
        'Initial Measurement - Biological Asset',
        'Subsequent Measurement - Biological Asset (Fair Value Model)',
        'Gains/Losses on Initial Recognition and Changes in Fair Value',
        'Agricultural Produce at Point of Harvest',
        'Government Grants Related to Biological Assets',
        'Disclosure Requirements'
    ],
    'Description': [
        'Company R has a dairy farm with 100 cows. The company controls the cows, can measure their fair value reliably, and expects future economic benefits from milk production and eventual sale of the cows.',
        'Company R purchases 20 additional dairy cows for $2,000 each. Transaction costs are $5,000 in total.',
        'At the end of the reporting period, the fair value less costs to sell of the 120 dairy cows is estimated to be $260,000. The previous carrying amount was $245,000.',
        'Company R recognizes the initial fair value of its biological assets and subsequent changes in fair value.',
        'Company R harvests 10,000 liters of milk from its dairy cows. The fair value less costs to sell of the milk at the point of harvest is $0.50 per liter.',
        'Company R receives a government grant of $20,000 that is conditional on the company maintaining its dairy farming activities for the next 5 years. The grant is related to biological assets measured at fair value less costs to sell.',
        'Company R needs to disclose information about its biological assets and agricultural activities.'
    ],
    'Accounting Treatment under IAS 41': [
        'A biological asset is recognized when: (a) the entity controls the asset as a result of past events; (b) it is probable that future economic benefits will flow to the entity; and (c) the fair value or cost of the asset can be measured reliably.',
        'A biological asset is measured on initial recognition and at the end of each reporting period at its fair value less costs to sell. Initial measurement = (20 cows * $2,000) + $5,000 = $45,000.',
        'Biological assets are measured at fair value less costs to sell, with changes recognized in profit or loss. Fair value gain = $260,000 - $245,000 = $15,000.',
        'A gain or loss arising on initial recognition of a biological asset at fair value less costs to sell and from a change in fair value less costs to sell of a biological asset is included in profit or loss for the period in which it arises.',
        'Agricultural produce harvested from biological assets is measured at its fair value less costs to sell at the point of harvest. This measurement is the cost at that date when applying IAS 2 Inventories or another applicable standard. Milk inventory = 10,000 liters * $0.50 = $5,000.',
        'An unconditional government grant related to a biological asset measured at fair value less costs to sell is recognized in profit or loss when the grant becomes receivable. If conditional, it is recognized when the conditions are met. The $20,000 grant is recognized as income over the 5-year period as conditions are met.',
        'Disclosures include: aggregate gain/loss from initial recognition and changes in fair value; description of biological assets by group; methods and assumptions used in determining fair value; fair value less costs to sell of agricultural produce harvested during the period; existence and carrying amounts of restricted biological assets; commitments for development or acquisition; financial risk management strategies.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Biological Assets (Dairy Cows) recognized on balance sheet',
        'Biological Assets (New Cows): $45,000',
        'Fair Value Gain in P&L: $15,000; Carrying Amount: $260,000',
        'Initial Recognition Gain and Fair Value Changes in P&L',
        'Agricultural Produce (Milk) Inventory: $5,000',
        'Government Grant Income: $4,000 per year for 5 years',
        'Comprehensive disclosures in notes to financial statements'
    ]
}
df_ias41 = pd.DataFrame(data_ias41)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS41_Agriculture_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias41.to_excel(writer, sheet_name='IAS41_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS41_Example']
    for i, col in enumerate(df_ias41.columns):
        column_len = max(df_ias41[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

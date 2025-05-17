import pandas as pd

# Create a DataFrame for IAS 40 - Investment Property
data_ias40 = {
    'Scenario Type': [
        'Recognition - Initial Acquisition',
        'Initial Measurement',
        'Subsequent Measurement - Fair Value Model',
        'Subsequent Measurement - Cost Model',
        'Transfer to/from Investment Property - Owner-Occupied Property to Investment Property',
        'Transfer to/from Investment Property - Investment Property to Inventory',
        'Disposal of Investment Property'
    ],
    'Description': [
        'Company Q purchases a building for $2,000,000 to earn rental income. The building is not occupied by Company Q.',
        'Company Q incurs legal fees of $30,000 and property transfer taxes of $50,000 on the acquisition of the investment property.',
        'Company Q chooses the fair value model for subsequent measurement of its investment property. At the end of Year 1, the fair value of the property is determined to be $2,150,000.',
        'Company Q chooses the cost model for subsequent measurement of its investment property. The building has an estimated useful life of 40 years and no residual value.',
        'Company Q has a property that was previously used as its headquarters (owner-occupied property) with a carrying amount of $1,500,000. The company relocates its headquarters and decides to rent out the property to third parties.',
        'Company Q has an investment property carried at fair value of $3,000,000. The company decides to develop the property for sale in the ordinary course of business.',
        'Company Q sells an investment property that was carried at fair value of $2,500,000 for $2,700,000 cash.'
    ],
    'Accounting Treatment under IAS 40': [
        'Investment property is recognized as an asset when it is probable that future economic benefits will flow to the entity and the cost can be measured reliably.',
        'Investment property is initially measured at cost, including transaction costs. Cost = $2,000,000 + $30,000 + $50,000 = $2,080,000.',
        'Under the fair value model, investment property is measured at fair value at each reporting date, with changes in fair value recognized in profit or loss. Fair value gain = $2,150,000 - $2,080,000 = $70,000.',
        'Under the cost model, investment property is measured at cost less accumulated depreciation and impairment losses (similar to IAS 16). Annual depreciation = $2,080,000 / 40 years = $52,000.',
        'The property is transferred from property, plant and equipment (IAS 16) to investment property (IAS 40). If using fair value model, any difference between the carrying amount and fair value at the date of transfer is treated as a revaluation under IAS 16.',
        'The property is transferred from investment property to inventory (IAS 2) at fair value. This fair value becomes the deemed cost for subsequent accounting under IAS 2.',
        'The difference between the net disposal proceeds and the carrying amount is recognized in profit or loss. Gain on disposal = $2,700,000 - $2,500,000 = $200,000.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Investment Property recognized: $2,000,000',
        'Investment Property at Cost: $2,080,000',
        'Fair Value Gain in P&L: $70,000; Carrying Amount: $2,150,000',
        'Annual Depreciation: $52,000; Carrying Amount after 1 year: $2,028,000',
        'If Fair Value at Transfer Date is $1,600,000: Revaluation Gain in OCI: $100,000; Investment Property recognized at $1,600,000',
        'Investment Property derecognized: $3,000,000; Inventory recognized: $3,000,000',
        'Gain on Disposal in P&L: $200,000'
    ]
}
df_ias40 = pd.DataFrame(data_ias40)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS40_Investment_Property_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias40.to_excel(writer, sheet_name='IAS40_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS40_Example']
    for i, col in enumerate(df_ias40.columns):
        column_len = max(df_ias40[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

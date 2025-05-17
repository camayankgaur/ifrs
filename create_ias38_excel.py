import pandas as pd

# Create a DataFrame for IAS 38 - Intangible Assets
data_ias38 = {
    'Scenario Type': [
        'Recognition - Separate Acquisition',
        'Recognition - Internally Generated (Research Phase)',
        'Recognition - Internally Generated (Development Phase)',
        'Initial Measurement',
        'Subsequent Measurement - Cost Model',
        'Subsequent Measurement - Revaluation Model',
        'Amortization - Finite Useful Life',
        'Impairment Testing - Indefinite Useful Life'
    ],
    'Description': [
        'Company P purchases a patent for $500,000 plus legal fees of $20,000 and registration fees of $5,000.',
        'Company P incurs costs of $200,000 on research activities aimed at gaining new scientific knowledge.',
        'Company P incurs costs of $300,000 on the development of a new product. The project meets all the criteria for recognition as an intangible asset under IAS 38 (technical feasibility, intention to complete, ability to use/sell, future economic benefits, adequate resources, reliable measurement of expenditure).',
        'Company P acquires a software license for $100,000. Installation costs are $10,000, and employee training costs are $15,000.',
        'Company P has a patent with a cost of $500,000 and a useful life of 10 years. It uses the cost model for subsequent measurement.',
        'Company P has a trademark with a cost of $300,000. It uses the revaluation model for subsequent measurement. At the end of Year 1, the fair value of the trademark is determined to be $350,000.',
        'Company P has a software license with a cost of $120,000 and a useful life of 5 years. The residual value is estimated to be $20,000.',
        'Company P has a brand name with an indefinite useful life, carried at $400,000. There are indications that it may be impaired.'
    ],
    'Accounting Treatment under IAS 38': [
        'An intangible asset is recognized if it is probable that future economic benefits will flow to the entity and the cost can be measured reliably. The patent is recognized at cost: $500,000 + $20,000 + $5,000 = $525,000.',
        'Research expenditure is recognized as an expense when it is incurred. No intangible asset is recognized from research (or from the research phase of an internal project).',
        'Development expenditure is recognized as an intangible asset if, and only if, all the specified criteria are met. The development costs of $300,000 are capitalized as an intangible asset.',
        'An intangible asset is initially measured at cost. The software license is recognized at $110,000 ($100,000 + $10,000). Training costs of $15,000 are expensed as incurred, as they are not directly attributable to bringing the asset to its working condition.',
        'Under the cost model, an intangible asset is carried at cost less accumulated amortization and impairment losses. Annual amortization = ($500,000 / 10 years) = $50,000.',
        'Under the revaluation model, an intangible asset is carried at a revalued amount, which is its fair value at the date of revaluation less subsequent amortization and impairment losses. The increase in value of $50,000 ($350,000 - $300,000) is recognized in other comprehensive income and accumulated in equity under the heading of revaluation surplus.',
        'The depreciable amount ($120,000 - $20,000 = $100,000) is allocated on a systematic basis over the useful life. Annual amortization = $100,000 / 5 years = $20,000.',
        'An intangible asset with an indefinite useful life is not amortized but is tested for impairment annually and whenever there is an indication that it may be impaired. If the recoverable amount is less than the carrying amount, an impairment loss is recognized.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'Intangible Asset (Patent): $525,000',
        'Research Expense: $200,000; No Intangible Asset recognized',
        'Intangible Asset (Development): $300,000',
        'Intangible Asset (Software): $110,000; Expense: $15,000',
        'Annual Amortization: $50,000; Carrying Amount after 1 year: $450,000',
        'Revaluation Surplus in OCI: $50,000; Carrying Amount: $350,000',
        'Annual Amortization: $20,000; Carrying Amount after 1 year: $100,000',
        'If Recoverable Amount is $350,000: Impairment Loss: $50,000; New Carrying Amount: $350,000'
    ]
}
df_ias38 = pd.DataFrame(data_ias38)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS38_Intangible_Assets_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias38.to_excel(writer, sheet_name='IAS38_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS38_Example']
    for i, col in enumerate(df_ias38.columns):
        column_len = max(df_ias38[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

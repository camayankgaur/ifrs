import pandas as pd

# Create a DataFrame for IAS 36 - Impairment of Assets
data_ias36 = {
    'Scenario Type': [
        'Identifying an Asset That May Be Impaired - Indicators',
        'Determining Recoverable Amount - Value in Use Calculation',
        'Determining Recoverable Amount - Fair Value Less Costs of Disposal',
        'Recognition of Impairment Loss - Individual Asset',
        'Recognition of Impairment Loss - Cash Generating Unit (CGU)',
        'Allocation of Goodwill to CGUs',
        'Reversal of Impairment Loss'
    ],
    'Description': [
        'Company M has a manufacturing plant with carrying amount of $10,000,000. There are indications that the plant may be impaired due to technological obsolescence and declining market demand for its products.',
        'Company M estimates future cash flows from the plant for the next 5 years, plus a terminal value. The pre-tax discount rate is 12%.',
        'Company M determines the fair value of the plant based on a recent offer from a potential buyer, less estimated costs to sell.',
        'The plant\'s recoverable amount is determined to be $8,000,000, which is less than its carrying amount of $10,000,000.',
        'Company M has a CGU with assets totaling $5,000,000 (including identifiable assets of $4,500,000 and goodwill of $500,000). The recoverable amount of the CGU is determined to be $4,000,000.',
        'Company M acquires a business and recognizes goodwill of $2,000,000. It allocates this goodwill to three CGUs based on the expected benefits from the synergies of the business combination.',
        'In a subsequent period, the market for Company M\'s products improves, and the recoverable amount of the previously impaired plant increases to $9,000,000. The current carrying amount after previous impairment is $8,000,000.'
    ],
    'Accounting Treatment under IAS 36': [
        'External indicators: significant decline in market value, adverse changes in technology/market/economy/legal environment, increase in market interest rates, market capitalization below net asset value. Internal indicators: obsolescence/physical damage, asset restructuring/discontinuation, worse economic performance than expected.',
        'Value in Use = Present Value of Future Cash Flows. Cash flow projections based on reasonable assumptions, latest budgets/forecasts (max 5 years), extrapolation using steady/declining growth rate. Discount rate reflects current market assessments of time value of money and asset-specific risks.',
        'Fair Value Less Costs of Disposal = Price in an orderly transaction between market participants - costs of disposal. Best evidence is price in binding sale agreement or active market. If not available, based on best information available.',
        'An impairment loss of $2,000,000 ($10,000,000 - $8,000,000) is recognized in profit or loss. The carrying amount of the plant is reduced to $8,000,000.',
        'The impairment loss of $1,000,000 ($5,000,000 - $4,000,000) is allocated first to goodwill ($500,000), reducing it to zero, and then pro-rata to the identifiable assets based on their carrying amounts, reducing them by $500,000 in total.',
        'Goodwill is allocated to CGUs that are expected to benefit from the synergies of the business combination. Each unit represents the lowest level within the entity at which goodwill is monitored for internal management purposes and is not larger than an operating segment.',
        'A reversal of impairment loss of $1,000,000 ($9,000,000 - $8,000,000) is recognized in profit or loss. The carrying amount of the plant is increased to $9,000,000, which does not exceed what the carrying amount would have been had no impairment loss been recognized previously (original $10,000,000 less depreciation).'
    ],
    'Illustrative Amount/Impact (USD)': [
        'N/A (Identification step)',
        'Value in Use: e.g., $8,500,000 (PV of projected cash flows)',
        'Fair Value Less Costs of Disposal: e.g., $8,000,000 (offer price less selling costs)',
        'Impairment Loss: $2,000,000; New Carrying Amount: $8,000,000',
        'Impairment Loss (Goodwill): $500,000; Impairment Loss (Other Assets): $500,000; New CGU Carrying Amount: $4,000,000',
        'Allocation: CGU1: $1,000,000; CGU2: $600,000; CGU3: $400,000',
        'Reversal of Impairment Loss: $1,000,000; New Carrying Amount: $9,000,000'
    ]
}
df_ias36 = pd.DataFrame(data_ias36)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS36_Impairment_of_Assets_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias36.to_excel(writer, sheet_name='IAS36_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS36_Example']
    for i, col in enumerate(df_ias36.columns):
        column_len = max(df_ias36[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

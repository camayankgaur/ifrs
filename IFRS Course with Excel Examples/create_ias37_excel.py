import pandas as pd

# Create a DataFrame for IAS 37 - Provisions, Contingent Liabilities and Contingent Assets
data_ias37 = {
    'Scenario Type': [
        'Provision - Warranty',
        'Provision - Environmental Restoration',
        'Provision - Restructuring',
        'Contingent Liability - Legal Claim',
        'Contingent Liability - Guarantee',
        'Contingent Asset - Insurance Claim',
        'Onerous Contract'
    ],
    'Description': [
        'Company N sells products with a 12-month warranty. Based on past experience, it is probable that there will be some claims under the warranties. The estimated cost of repairs is 2% of revenue.',
        'Company N operates a mine and has a legal obligation to restore the site at the end of its useful life in 10 years. The estimated cost of restoration is $1,000,000.',
        'Company N announces a detailed formal plan to restructure a division, creating a valid expectation in those affected. The estimated costs include employee termination payments of $500,000 and lease termination penalties of $200,000.',
        'Company N is being sued by a customer for $300,000 for alleged product defects. Legal counsel advises that it is possible but not probable that the company will lose the case.',
        'Company N has guaranteed a bank loan of $1,000,000 for a related party. It is not considered probable that the related party will default.',
        'Company N\'s factory was damaged by a flood. It has filed an insurance claim for $500,000. The insurance company has acknowledged the claim but has not yet confirmed the amount that will be paid.',
        'Company N has a non-cancellable operating lease for office space that is no longer used due to relocation. The lease has 3 years remaining with annual payments of $100,000. The space can be sublet for only $60,000 per year.'
    ],
    'Accounting Treatment under IAS 37': [
        'A provision is recognized when: (a) there is a present obligation (legal or constructive) as a result of a past event; (b) it is probable that an outflow of resources will be required to settle the obligation; and (c) a reliable estimate can be made. Warranty provision = 2% of revenue.',
        'The present value of the estimated restoration cost is recognized as a provision and as part of the cost of the mine. The provision is increased each period due to the unwinding of the discount (finance cost).',
        'A provision for restructuring is recognized when the entity has a detailed formal plan and has raised a valid expectation in those affected. Only direct costs of restructuring are included, not costs associated with ongoing activities.',
        'A contingent liability is not recognized in the statement of financial position but is disclosed in the notes, unless the possibility of an outflow is remote.',
        'A contingent liability is not recognized in the statement of financial position but is disclosed in the notes, unless the possibility of an outflow is remote.',
        'A contingent asset is not recognized in the statement of financial position but is disclosed in the notes when an inflow of economic benefits is probable. When the realization of income is virtually certain, the related asset is not a contingent asset and its recognition is appropriate.',
        'An onerous contract is one where the unavoidable costs of meeting the obligations exceed the economic benefits expected. A provision is recognized for the present obligation under the contract, measured at the lower of the cost of fulfilling it and any compensation or penalties from failing to fulfill it.'
    ],
    'Illustrative Amount/Impact (USD)': [
        'If annual revenue is $5,000,000, warranty provision = $100,000 (2% of $5,000,000).',
        'Initial provision (PV of $1,000,000) = $385,543 (assuming 10% discount rate). Year 1 unwinding of discount = $38,554 (finance cost).',
        'Restructuring provision = $700,000 ($500,000 + $200,000).',
        'No provision recognized. Contingent liability of $300,000 disclosed in notes.',
        'No provision recognized. Contingent liability of $1,000,000 disclosed in notes.',
        'No asset recognized. Contingent asset of $500,000 disclosed in notes if recovery is probable.',
        'Provision for onerous contract = $120,000 (($100,000 - $60,000) * 3 years).'
    ]
}
df_ias37 = pd.DataFrame(data_ias37)

# Create an Excel writer
excel_file_path = '/home/ubuntu/IAS37_Provisions_Contingent_Liabilities_Assets_Example.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_ias37.to_excel(writer, sheet_name='IAS37_Example', index=False)
    # Adjust column widths
    worksheet = writer.sheets['IAS37_Example']
    for i, col in enumerate(df_ias37.columns):
        column_len = max(df_ias37[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(i, i, column_len + 2)

print(f"Excel file created: {excel_file_path}")

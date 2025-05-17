import pandas as pd

# Data for the Excel sheets
scenario_data = {
    "Sheet": ["Scenario"],
    "Description": [
        "AcquirerCo acquires 100% of TargetCo on January 1, 20X1. "
        "This Excel file demonstrates the calculation of goodwill and the initial accounting for a business combination under IFRS 3."
    ]
}

consideration_transferred_data = {
    "Component": ["Cash paid", "Fair value of shares issued (10,000 shares @ $5 FV)", "Contingent consideration (fair value)"],
    "Amount ($)": [300000, 50000, 20000],
    "Total Consideration Transferred": ["", "", 370000]
}

identifiable_net_assets_data = {
    "Asset/Liability": [
        "Property, Plant & Equipment (Fair Value)",
        "Intangible Asset - Customer List (Fair Value, not on TargetCo BS)",
        "Inventory (Fair Value)",
        "Trade Receivables (Fair Value)",
        "Cash and Cash Equivalents",
        "Trade Payables (Fair Value)",
        "Contingent Liability (Fair Value, from TargetCo)"
    ],
    "Fair Value at Acquisition Date ($)": [
        200000,
        30000,
        80000,
        40000,
        10000,
        -50000, # Liability
        -15000  # Liability
    ],
    "Net Identifiable Assets Acquired": ["", "", "", "", "", "", 295000] # Sum of above
}

goodwill_calculation_data = {
    "Item": [
        "Consideration Transferred",
        "Less: Fair Value of Net Identifiable Assets Acquired"
    ],
    "Amount ($)": [
        370000,
        -295000
    ],
    "Goodwill Acquired": ["", 75000]
}

acquisition_related_costs_data = {
    "Cost Type": ["Legal and advisory fees", "Due diligence costs", "Total"],
    "Amount ($)": [10000, 5000, 15000],
    "Treatment": ["Expensed in P&L", "Expensed in P&L", ""],
    "Total Acquisition-Related Costs (Expensed)": ["", "", 15000]
}

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = "/home/ubuntu/ifrs_course_excel_examples/IFRS3_Business_Combinations_Example.xlsx"
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Write data to sheets
df_scenario = pd.DataFrame(scenario_data)
df_scenario.to_excel(writer, sheet_name='Scenario', index=False)

df_consideration = pd.DataFrame(consideration_transferred_data)
df_consideration.to_excel(writer, sheet_name='Consideration_Transferred', index=False)

df_net_assets = pd.DataFrame(identifiable_net_assets_data)
df_net_assets.to_excel(writer, sheet_name='Net_Identifiable_Assets', index=False)

df_goodwill = pd.DataFrame(goodwill_calculation_data)
df_goodwill.to_excel(writer, sheet_name='Goodwill_Calculation', index=False)

df_acq_costs = pd.DataFrame(acquisition_related_costs_data)
df_acq_costs.to_excel(writer, sheet_name='Acquisition_Related_Costs', index=False)

# Adjust column widths for better readability
workbook  = writer.book
worksheet_scenario = writer.sheets['Scenario']
worksheet_scenario.set_column('A:A', 15)
worksheet_scenario.set_column('B:B', 100)

worksheet_consideration = writer.sheets['Consideration_Transferred']
worksheet_consideration.set_column('A:A', 40) # Component
worksheet_consideration.set_column('B:B', 15) # Amount
worksheet_consideration.set_column('C:C', 30) # Total Consideration

worksheet_net_assets = writer.sheets['Net_Identifiable_Assets']
worksheet_net_assets.set_column('A:A', 50) # Asset/Liability
worksheet_net_assets.set_column('B:B', 30) # Fair Value
worksheet_net_assets.set_column('C:C', 30) # Net Identifiable Assets

worksheet_goodwill = writer.sheets['Goodwill_Calculation']
worksheet_goodwill.set_column('A:A', 45) # Item
worksheet_goodwill.set_column('B:B', 15) # Amount
worksheet_goodwill.set_column('C:C', 20) # Goodwill

worksheet_acq_costs = writer.sheets['Acquisition_Related_Costs']
worksheet_acq_costs.set_column('A:A', 30) # Cost Type
worksheet_acq_costs.set_column('B:B', 15) # Amount
worksheet_acq_costs.set_column('C:C', 20) # Treatment
worksheet_acq_costs.set_column('D:D', 40) # Total Costs

# Close the Pandas Excel writer and output the Excel file.
writer.close()

print(f"Excel file created at {excel_file_path}")


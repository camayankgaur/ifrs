import pandas as pd

# Data for the Excel sheets
scenario_data = {
    "Sheet": ["Scenario"],
    "Description": [
        "RetailCo decides to sell one of its underperforming divisions, Division X, on October 1, 20X1. "
        "The carrying amounts of Division X's assets and liabilities in RetailCo's books immediately before classification as held for sale are provided. "
        "The fair value less costs to sell (FVLCTS) of Division X as a whole is estimated to be $350,000. "
        "This Excel file demonstrates the application of IFRS 5, including the measurement of assets held for sale and the calculation of any impairment loss."
    ]
}

assets_liabilities_data = {
    "Item": [
        "Goodwill (allocated to Division X)",
        "Property, Plant & Equipment (Net)",
        "Intangible Assets (Brand Name)",
        "Inventory",
        "Trade Receivables",
        "Total Assets of Disposal Group",
        "Trade Payables",
        "Provisions",
        "Total Liabilities of Disposal Group",
        "Net Assets of Disposal Group (Carrying Amount before IFRS 5)"
    ],
    "Carrying Amount before HFS ($)": [
        50000,
        250000,
        80000,
        60000,
        40000,
        480000, # Sum of assets
        -70000, # Liability
        -30000, # Liability
        -100000, # Sum of liabilities
        380000  # Net Assets (480000 - 100000)
    ]
}

measurement_hfs_data = {
    "Step": [
        "1. Carrying Amount of Net Assets of Disposal Group (before classification as HFS)",
        "2. Fair Value Less Costs to Sell (FVLCTS) of Disposal Group",
        "3. Compare Carrying Amount with FVLCTS",
        "4. Impairment Loss to be Recognized (if Carrying Amount > FVLCTS)"
    ],
    "Amount ($)": [
        380000, # From assets_liabilities_data
        350000, # Given in scenario
        "Carrying Amount ($380,000) > FVLCTS ($350,000)",
        30000   # 380000 - 350000
    ],
    "Note": [
        "Calculated from individual assets and liabilities.",
        "Estimated market value less selling expenses.",
        "An impairment loss is indicated.",
        "Impairment loss = $380,000 - $350,000"
    ]
}

impairment_allocation_data = {
    "Asset Category": [
        "Goodwill",
        "Property, Plant & Equipment",
        "Intangible Assets (Brand Name)",
        "Inventory",
        "Trade Receivables"
    ],
    "Carrying Amount before Impairment ($)": [
        50000,
        250000,
        80000,
        60000, # Not subject to IFRS 5 impairment allocation in this step (measured at lower of cost and NRV per IAS 2)
        40000  # Not subject to IFRS 5 impairment allocation (financial asset under IFRS 9)
    ],
    "IFRS 5 Impairment Allocation ($)": [
        -30000, # Goodwill is reduced first
        0,      # Remaining impairment (30000 - 30000 = 0) is allocated pro-rata to other non-current assets within scope of IFRS 5 measurement rules
        0,      # For simplicity, assume PPE and Intangibles are not impaired further after goodwill.
                # A more complex example would pro-rate the remaining impairment.
        "N/A (IAS 2)",
        "N/A (IFRS 9)"
    ],
    "Carrying Amount after Impairment ($)": [
        20000,  # 50000 - 30000
        250000,
        80000,
        60000,
        40000
    ],
    "Note": [
        "Impairment loss allocated first to goodwill.",
        "Remaining impairment (if any) allocated pro-rata to other non-current assets in scope.",
        "(Assuming no further impairment needed for these assets beyond goodwill reduction for this example)",
        "Inventory measured at lower of cost and NRV (IAS 2). Assumed no impairment under IAS 2.",
        "Trade receivables measured per IFRS 9. Assumed no impairment under IFRS 9."
    ]
}

# Recalculate total assets after impairment
total_assets_after_impairment = 20000 + 250000 + 80000 + 60000 + 40000 # 450000

presentation_sofp_data = {
    "Line Item": [
        "Assets classified as held for sale",
        "Liabilities directly associated with assets classified as held for sale"
    ],
    "Amount ($)": [
        total_assets_after_impairment, # Sum of assets after impairment
        100000 # From assets_liabilities_data (absolute value of total liabilities)
    ],
    "Note": [
        "Presented separately on the Statement of Financial Position.",
        "Presented separately on the Statement of Financial Position."
    ]
}

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = "/home/ubuntu/ifrs_course_excel_examples/IFRS5_Non_Current_Assets_HFS_Example.xlsx"
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Write data to sheets
df_scenario = pd.DataFrame(scenario_data)
df_scenario.to_excel(writer, sheet_name='Scenario', index=False)

df_assets_liabilities = pd.DataFrame(assets_liabilities_data)
df_assets_liabilities.to_excel(writer, sheet_name='Assets_Liabilities_HFS', index=False)

df_measurement_hfs = pd.DataFrame(measurement_hfs_data)
df_measurement_hfs.to_excel(writer, sheet_name='Measurement_HFS', index=False)

df_impairment_allocation = pd.DataFrame(impairment_allocation_data)
df_impairment_allocation.to_excel(writer, sheet_name='Impairment_Allocation', index=False)

df_presentation_sofp = pd.DataFrame(presentation_sofp_data)
df_presentation_sofp.to_excel(writer, sheet_name='Presentation_SOFP', index=False)

# Adjust column widths for better readability
workbook  = writer.book
worksheet_scenario = writer.sheets['Scenario']
worksheet_scenario.set_column('A:A', 15)
worksheet_scenario.set_column('B:B', 100)

worksheet_assets_liabilities = writer.sheets['Assets_Liabilities_HFS']
worksheet_assets_liabilities.set_column('A:A', 60) # Item
worksheet_assets_liabilities.set_column('B:B', 30) # Carrying Amount

worksheet_measurement_hfs = writer.sheets['Measurement_HFS']
worksheet_measurement_hfs.set_column('A:A', 60) # Step
worksheet_measurement_hfs.set_column('B:B', 40) # Amount
worksheet_measurement_hfs.set_column('C:C', 50) # Note

worksheet_impairment_allocation = writer.sheets['Impairment_Allocation']
worksheet_impairment_allocation.set_column('A:A', 35) # Asset Category
worksheet_impairment_allocation.set_column('B:B', 35) # Carrying Amount before Impairment
worksheet_impairment_allocation.set_column('C:C', 35) # IFRS 5 Impairment Allocation
worksheet_impairment_allocation.set_column('D:D', 35) # Carrying Amount after Impairment
worksheet_impairment_allocation.set_column('E:E', 70) # Note

worksheet_presentation_sofp = writer.sheets['Presentation_SOFP']
worksheet_presentation_sofp.set_column('A:A', 60) # Line Item
worksheet_presentation_sofp.set_column('B:B', 15) # Amount
worksheet_presentation_sofp.set_column('C:C', 60) # Note

# Close the Pandas Excel writer and output the Excel file.
writer.close()

print(f"Excel file created at {excel_file_path}")


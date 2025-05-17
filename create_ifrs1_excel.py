import pandas as pd

# Data for the Excel sheets
scenario_data = {
    "Sheet": ["Scenario"],
    "Description": [
        "TransitionCo is adopting IFRS for the first time for the year ending December 31, 20X1. "
        "Its date of transition to IFRS is January 1, 20X0. "
        "This Excel file demonstrates the key adjustments required to prepare the opening IFRS Statement of Financial Position as at January 1, 20X0."
    ]
}

local_gaap_bs_data = {
    "Assets": [
        "Property, Plant & Equipment (Net)",
        "Intangible Assets (Development Costs Capitalised)",
        "Inventory",
        "Trade Receivables",
        "Cash and Cash Equivalents",
        "Total Assets"
    ],
    "Amount (Local GAAP)": [500000, 100000, 200000, 150000, 50000, 1000000]
}

equity_liabilities_gaap_bs_data = {
    "Equity and Liabilities": [
        "Share Capital",
        "Retained Earnings (Local GAAP)",
        "Revaluation Reserve (PPE)",
        "Total Equity",
        "Long-term Provisions (Restructuring)",
        "Trade Payables",
        "Total Liabilities",
        "Total Equity and Liabilities"
    ],
    "Amount (Local GAAP)": [300000, 250000, 50000, 600000, 100000, 300000, 400000, 1000000]
}

ifrs_adjustments_data = {
    "Item": [
        "Property, Plant & Equipment (PPE)",
        "Intangible Assets (Development Costs)",
        "Revaluation Reserve (PPE)",
        "Long-term Provisions (Restructuring)",
        "Deferred Tax Liability (New)"
    ],
    "Local GAAP Amount": [500000, 100000, 50000, 100000, "N/A"],
    "Adjustment Dr/(Cr)": [-20000, -100000, -50000, 60000, -30000],
    "IFRS Amount": [480000, 0, 0, 40000, 30000],
    "Explanation": [
        "PPE was revalued under local GAAP. IFRS 1 allows use of fair value or revaluation as deemed cost. Assume TransitionCo elects to use previous GAAP revaluation as deemed cost, but an impairment of 20,000 is identified under IAS 36 on transition.",
        "Development costs of 100,000 were capitalised under local GAAP but do not meet IAS 38 criteria for capitalisation at the date of transition. Must be expensed against opening retained earnings.",
        "The revaluation reserve related to PPE under local GAAP is eliminated against retained earnings as per IFRS 1 election or as part of deemed cost application.",
        "Restructuring provision of 100,000 under local GAAP. On review, only 40,000 meets IAS 37 recognition criteria at the date of transition. The difference of 60,000 increases retained earnings.",
        "New deferred tax liability arises from temporary differences created by IFRS adjustments (e.g., on PPE impairment, derecognition of development costs). Assumed net DTL of 30,000."
    ]
}

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = "/home/ubuntu/ifrs_course_excel_examples/IFRS1_First_Time_Adoption_Example.xlsx"
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Write data to sheets
df_scenario = pd.DataFrame(scenario_data)
df_scenario.to_excel(writer, sheet_name='Scenario', index=False)

df_local_gaap_assets = pd.DataFrame(local_gaap_bs_data)
df_local_gaap_equity_liabilities = pd.DataFrame(equity_liabilities_gaap_bs_data)

# Combine Local GAAP BS parts for a single sheet presentation
worksheet_local_gaap = writer.book.add_worksheet('Local_GAAP_BS')

# Write headers for Assets
for col_num, value in enumerate(df_local_gaap_assets.columns.values):
    worksheet_local_gaap.write(0, col_num, value)
# Write data for Assets
for row_num, row_data in enumerate(df_local_gaap_assets.values):
    for col_num, cell_data in enumerate(row_data):
        worksheet_local_gaap.write(row_num + 1, col_num, cell_data)

# Write headers for Equity and Liabilities (with a blank row separator)
start_row_equity = len(df_local_gaap_assets) + 2
for col_num, value in enumerate(df_local_gaap_equity_liabilities.columns.values):
    worksheet_local_gaap.write(start_row_equity, col_num, value)
# Write data for Equity and Liabilities
for row_num, row_data in enumerate(df_local_gaap_equity_liabilities.values):
    for col_num, cell_data in enumerate(row_data):
        worksheet_local_gaap.write(start_row_equity + row_num + 1, col_num, cell_data)

df_ifrs_adjustments = pd.DataFrame(ifrs_adjustments_data)
df_ifrs_adjustments.to_excel(writer, sheet_name='IFRS_Adjustments', index=False)

# Calculate Opening IFRS BS based on adjustments
# Assets
ppe_ifrs = 480000
intangible_ifrs = 0 # Derecognised
inventory_gaap = 200000 # No adjustment assumed for simplicity
trade_receivables_gaap = 150000 # No adjustment assumed
cash_gaap = 50000 # No adjustment assumed
total_assets_ifrs = ppe_ifrs + intangible_ifrs + inventory_gaap + trade_receivables_gaap + cash_gaap

# Equity and Liabilities
share_capital_gaap = 300000 # No change assumed
retained_earnings_gaap = 250000
adj_ppe_impairment = -20000
adj_dev_costs = -100000
adj_reval_reserve_elim = -50000 # This reserve is eliminated, effect on RE
adj_restructuring_prov = 60000
adj_deferred_tax = -30000 # Impact on RE from DTL recognition
retained_earnings_ifrs = retained_earnings_gaap + adj_ppe_impairment + adj_dev_costs + adj_reval_reserve_elim + adj_restructuring_prov + adj_deferred_tax

total_equity_ifrs = share_capital_gaap + retained_earnings_ifrs

restructuring_prov_ifrs = 40000
deferred_tax_liability_ifrs = 30000
trade_payables_gaap = 300000 # No adjustment assumed
total_liabilities_ifrs = restructuring_prov_ifrs + deferred_tax_liability_ifrs + trade_payables_gaap
total_equity_liabilities_ifrs = total_equity_ifrs + total_liabilities_ifrs

opening_ifrs_bs_assets_data = {
    "Assets": [
        "Property, Plant & Equipment (Net)",
        "Intangible Assets",
        "Inventory",
        "Trade Receivables",
        "Cash and Cash Equivalents",
        "Total Assets"
    ],
    "Amount (IFRS)": [ppe_ifrs, intangible_ifrs, inventory_gaap, trade_receivables_gaap, cash_gaap, total_assets_ifrs]
}

opening_ifrs_bs_equity_liabilities_data = {
    "Equity and Liabilities": [
        "Share Capital",
        "Retained Earnings (IFRS)",
        "Total Equity",
        "Long-term Provisions (Restructuring)",
        "Deferred Tax Liability",
        "Trade Payables",
        "Total Liabilities",
        "Total Equity and Liabilities"
    ],
    "Amount (IFRS)": [
        share_capital_gaap, retained_earnings_ifrs, total_equity_ifrs,
        restructuring_prov_ifrs, deferred_tax_liability_ifrs, trade_payables_gaap, total_liabilities_ifrs,
        total_equity_liabilities_ifrs
    ]
}

df_opening_ifrs_assets = pd.DataFrame(opening_ifrs_bs_assets_data)
df_opening_ifrs_equity_liabilities = pd.DataFrame(opening_ifrs_bs_equity_liabilities_data)

# Write Opening IFRS BS to a new sheet
worksheet_ifrs_bs = writer.book.add_worksheet('Opening_IFRS_BS')
# Write headers for Assets
for col_num, value in enumerate(df_opening_ifrs_assets.columns.values):
    worksheet_ifrs_bs.write(0, col_num, value)
# Write data for Assets
for row_num, row_data in enumerate(df_opening_ifrs_assets.values):
    for col_num, cell_data in enumerate(row_data):
        worksheet_ifrs_bs.write(row_num + 1, col_num, cell_data)

# Write headers for Equity and Liabilities (with a blank row separator)
start_row_equity_ifrs = len(df_opening_ifrs_assets) + 2
for col_num, value in enumerate(df_opening_ifrs_equity_liabilities.columns.values):
    worksheet_ifrs_bs.write(start_row_equity_ifrs, col_num, value)
# Write data for Equity and Liabilities
for row_num, row_data in enumerate(df_opening_ifrs_equity_liabilities.values):
    for col_num, cell_data in enumerate(row_data):
        worksheet_ifrs_bs.write(start_row_equity_ifrs + row_num + 1, col_num, cell_data)

# Adjust column widths for better readability
workbook  = writer.book
worksheet_scenario = writer.sheets['Scenario']
worksheet_scenario.set_column('A:A', 15)
worksheet_scenario.set_column('B:B', 100)

worksheet_local_gaap.set_column('A:A', 40)
worksheet_local_gaap.set_column('B:B', 20)

worksheet_ifrs_adj = writer.sheets['IFRS_Adjustments']
worksheet_ifrs_adj.set_column('A:A', 35) # Item
worksheet_ifrs_adj.set_column('B:B', 20) # Local GAAP Amount
worksheet_ifrs_adj.set_column('C:C', 20) # Adjustment Dr/(Cr)
worksheet_ifrs_adj.set_column('D:D', 15) # IFRS Amount
worksheet_ifrs_adj.set_column('E:E', 100) # Explanation

worksheet_ifrs_bs.set_column('A:A', 40)
worksheet_ifrs_bs.set_column('B:B', 20)

# Close the Pandas Excel writer and output the Excel file.
writer.close()

print(f"Excel file created at {excel_file_path}")


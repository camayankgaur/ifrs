import pandas as pd

# Data for the Excel sheets
scenario_data = {
    "Sheet": ["Scenario"],
    "Description": [
        "TechCorp grants 100 share options to each of its 50 senior executives on January 1, 20X1. "
        "The options vest if the executives remain in service for three years (i.e., until December 31, 20X3). "
        "The fair value of each option at the grant date is $15. "
        "This Excel file demonstrates the calculation of the share-based payment expense over the vesting period under IFRS 2."
    ]
}

inputs_assumptions_data = {
    "Parameter": [
        "Number of executives",
        "Options per executive",
        "Total options granted",
        "Grant date fair value per option ($)",
        "Vesting period (years)",
        "Expected forfeitures (Year 1 - estimate at grant date)",
        "Expected forfeitures (Year 2 - revised estimate)",
        "Expected forfeitures (Year 3 - actual at vesting)"
    ],
    "Value": [
        50,
        100,
        5000, # 50 * 100
        15,
        3,
        "5 executives (10%)",
        "3 executives in total (revised from 5)",
        "2 executives actually forfeited"
    ]
}

# Calculations
# Year 1 (20X1)
num_executives_y1 = 50
options_per_exec_y1 = 100
grant_date_fv_y1 = 15
vesting_period_y1 = 3

# Initial estimate of executives expected to vest
estimated_forfeitures_initial_pct = 0.10
estimated_exec_vesting_y1 = num_executives_y1 * (1 - estimated_forfeitures_initial_pct) # 50 * 0.9 = 45
total_options_expected_to_vest_y1 = estimated_exec_vesting_y1 * options_per_exec_y1 # 45 * 100 = 4500
total_compensation_cost_y1 = total_options_expected_to_vest_y1 * grant_date_fv_y1 # 4500 * 15 = 67500
annual_expense_y1 = total_compensation_cost_y1 / vesting_period_y1 # 67500 / 3 = 22500
cumulative_expense_y1 = annual_expense_y1 # 22500

# Year 2 (20X2)
# Revised estimate: 3 executives expected to forfeit in total (meaning 47 expected to vest)
estimated_exec_vesting_y2 = num_executives_y1 - 3 # 50 - 3 = 47
total_options_expected_to_vest_y2 = estimated_exec_vesting_y2 * options_per_exec_y1 # 47 * 100 = 4700
total_compensation_cost_y2 = total_options_expected_to_vest_y2 * grant_date_fv_y1 # 4700 * 15 = 70500
cumulative_expense_target_y2 = (total_compensation_cost_y2 / vesting_period_y1) * 2 # (70500 / 3) * 2 = 23500 * 2 = 47000
annual_expense_y2 = cumulative_expense_target_y2 - cumulative_expense_y1 # 47000 - 22500 = 24500
cumulative_expense_y2 = cumulative_expense_target_y2 # 47000

# Year 3 (20X3) - Vesting Date
# Actual forfeitures: 2 executives forfeited (meaning 48 actually vested)
actual_exec_vested_y3 = num_executives_y1 - 2 # 50 - 2 = 48
total_options_actually_vested_y3 = actual_exec_vested_y3 * options_per_exec_y1 # 48 * 100 = 4800
total_compensation_cost_actual_y3 = total_options_actually_vested_y3 * grant_date_fv_y1 # 4800 * 15 = 72000
cumulative_expense_target_y3 = total_compensation_cost_actual_y3 # 72000 (fully vested)
annual_expense_y3 = cumulative_expense_target_y3 - cumulative_expense_y2 # 72000 - 47000 = 25000
cumulative_expense_y3 = cumulative_expense_target_y3 # 72000

expense_calculation_data = {
    "Year": ["20X1 (Year 1)", "20X2 (Year 2)", "20X3 (Year 3)"],
    "Executives Expected to Vest (Cumulative)": [estimated_exec_vesting_y1, estimated_exec_vesting_y2, actual_exec_vested_y3],
    "Total Options Expected to Vest": [total_options_expected_to_vest_y1, total_options_expected_to_vest_y2, total_options_actually_vested_y3],
    "Fair Value per Option ($)": [grant_date_fv_y1, grant_date_fv_y1, grant_date_fv_y1],
    "Total Compensation Cost ($)": [total_compensation_cost_y1, total_compensation_cost_y2, total_compensation_cost_actual_y3],
    "Cumulative Expense Recognized ($)": [cumulative_expense_y1, cumulative_expense_y2, cumulative_expense_y3],
    "Annual Expense Recognized ($)": [annual_expense_y1, annual_expense_y2, annual_expense_y3],
    "Notes": [
        "Expense based on initial estimate of 45 executives vesting.",
        "Expense adjusted for revised estimate of 47 executives vesting.",
        "Expense adjusted for actual 48 executives vesting."
    ]
}

journal_entries_data = {
    "Date": [
        "Dec 31, 20X1", "Dec 31, 20X1",
        "Dec 31, 20X2", "Dec 31, 20X2",
        "Dec 31, 20X3", "Dec 31, 20X3",
        "Exercise Date (Example)", "Exercise Date (Example)", "Exercise Date (Example)", "Exercise Date (Example)"
    ],
    "Account": [
        "Share-based Payment Expense (P&L)", "Equity-settled SBP Reserve (Equity)",
        "Share-based Payment Expense (P&L)", "Equity-settled SBP Reserve (Equity)",
        "Share-based Payment Expense (P&L)", "Equity-settled SBP Reserve (Equity)",
        "Cash (assuming exercise price of $10 for 4800 options)", "Equity-settled SBP Reserve (Equity)", "Share Capital", "Share Premium"
    ],
    "Debit ($)": [annual_expense_y1, "", annual_expense_y2, "", annual_expense_y3, "", 4800 * 10, cumulative_expense_y3, "", ""],
    "Credit ($)": ["", annual_expense_y1, "", annual_expense_y2, "", annual_expense_y3, "", "", "(Nominal Value)", "(Balancing figure)"],
    "Description": [
        "To recognize SBP expense for Year 1", "",
        "To recognize SBP expense for Year 2", "",
        "To recognize SBP expense for Year 3", "",
        "To record exercise of options (illustrative)", "(Transfer from reserve)", "(e.g., 4800 options * $1 nominal)", " "
    ]
}

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file_path = "/home/ubuntu/ifrs_course_excel_examples/IFRS2_Share_Based_Payment_Example.xlsx"
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Write data to sheets
df_scenario = pd.DataFrame(scenario_data)
df_scenario.to_excel(writer, sheet_name='Scenario', index=False)

df_inputs = pd.DataFrame(inputs_assumptions_data)
df_inputs.to_excel(writer, sheet_name='Inputs_Assumptions', index=False)

df_expense_calc = pd.DataFrame(expense_calculation_data)
df_expense_calc.to_excel(writer, sheet_name='Expense_Calculation', index=False)

df_journal_entries = pd.DataFrame(journal_entries_data)
df_journal_entries.to_excel(writer, sheet_name='Journal_Entries_Illustrative', index=False)

# Adjust column widths for better readability
workbook  = writer.book
worksheet_scenario = writer.sheets['Scenario']
worksheet_scenario.set_column('A:A', 15)
worksheet_scenario.set_column('B:B', 100)

worksheet_inputs = writer.sheets['Inputs_Assumptions']
worksheet_inputs.set_column('A:A', 50)
worksheet_inputs.set_column('B:B', 30)

worksheet_expense_calc = writer.sheets['Expense_Calculation']
worksheet_expense_calc.set_column('A:A', 15) # Year
worksheet_expense_calc.set_column('B:B', 35) # Executives Expected to Vest
worksheet_expense_calc.set_column('C:C', 30) # Total Options Expected to Vest
worksheet_expense_calc.set_column('D:D', 25) # Fair Value per Option
worksheet_expense_calc.set_column('E:E', 25) # Total Compensation Cost
worksheet_expense_calc.set_column('F:F', 30) # Cumulative Expense Recognized
worksheet_expense_calc.set_column('G:G', 30) # Annual Expense Recognized
worksheet_expense_calc.set_column('H:H', 50) # Notes

worksheet_journal_entries = writer.sheets['Journal_Entries_Illustrative']
worksheet_journal_entries.set_column('A:A', 25) # Date
worksheet_journal_entries.set_column('B:B', 50) # Account
worksheet_journal_entries.set_column('C:C', 15) # Debit
worksheet_journal_entries.set_column('D:D', 15) # Credit
worksheet_journal_entries.set_column('E:E', 50) # Description

# Close the Pandas Excel writer and output the Excel file.
writer.close()

print(f"Excel file created at {excel_file_path}")


# ============================================================
# CELL 33: CREATE FINAL COMPARISON TABLE
# ============================================================

final_comparison_table = comparison_dataset[
    [
        "Qubits",
        "Gate_Count_Original",
        "Gate_Count_Processed",
        "Two_Qubit_Gate_Count_Original",
        "Two_Qubit_Gate_Count_Processed",
        "Two_Qubit_Gate_Ratio_Original_%",
        "Two_Qubit_Gate_Ratio_Processed_%",
        "Two_Qubit_Gate_Reduction_%",
        "Circuit_Depth_Original",
        "Circuit_Depth_Processed",
        "Circuit_Depth_Reduction_%",
        "Median_Execution_Time_Original_s",
        "Median_Execution_Time_Processed_s",
        "Execution_Time_Improvement_%"
    ]
].copy()

# Display the final comparison table
display(final_comparison_table)

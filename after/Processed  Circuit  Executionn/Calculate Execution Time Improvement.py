# ============================================================
# CELL 32: CALCULATE EXECUTION TIME IMPROVEMENT
# ============================================================

comparison_dataset["Execution_Time_Improvement_%"] = (
    (
        comparison_dataset["Median_Execution_Time_Original_s"]
        - comparison_dataset["Median_Execution_Time_Processed_s"]
    )
    / comparison_dataset["Median_Execution_Time_Original_s"]
) * 100

print("Execution Time Improvement")
print("-" * 45)

display(
    comparison_dataset[
        [
            "Qubits",
            "Median_Execution_Time_Original_s",
            "Median_Execution_Time_Processed_s",
            "Execution_Time_Improvement_%"
        ]
    ]
)

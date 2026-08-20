# ============================================================
# CELL 30: CALCULATE TOTAL GATE REDUCTION
# ============================================================

comparison_dataset["Total_Gate_Reduction_%"] = (
    (
        comparison_dataset["Gate_Count_Original"]
        - comparison_dataset["Gate_Count_Processed"]
    )
    / comparison_dataset["Gate_Count_Original"]
) * 100

print("Total Gate Reduction")
print("-" * 40)

display(
    comparison_dataset[
        [
            "Qubits",
            "Gate_Count_Original",
            "Gate_Count_Processed",
            "Total_Gate_Reduction_%"
        ]
    ]
)

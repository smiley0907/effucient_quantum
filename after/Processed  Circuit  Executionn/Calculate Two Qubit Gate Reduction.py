# ============================================================
# CELL 29: CALCULATE TWO-QUBIT GATE REDUCTION
# ============================================================

comparison_dataset["Two_Qubit_Gate_Reduction_%"] = (
    (
        comparison_dataset["Two_Qubit_Gate_Count_Original"]
        - comparison_dataset["Two_Qubit_Gate_Count_Processed"]
    )
    / comparison_dataset["Two_Qubit_Gate_Count_Original"]
) * 100

print("Two-Qubit Gate Reduction")
print("-" * 40)

display(
    comparison_dataset[
        [
            "Qubits",
            "Two_Qubit_Gate_Count_Original",
            "Two_Qubit_Gate_Count_Processed",
            "Two_Qubit_Gate_Reduction_%"
        ]
    ]
)

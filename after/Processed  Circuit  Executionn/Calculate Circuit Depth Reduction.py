# ============================================================
# CELL 31: CALCULATE CIRCUIT DEPTH REDUCTION
# ============================================================

comparison_dataset["Circuit_Depth_Reduction_%"] = (
    (
        comparison_dataset["Circuit_Depth_Original"]
        - comparison_dataset["Circuit_Depth_Processed"]
    )
    / comparison_dataset["Circuit_Depth_Original"]
) * 100

print("Circuit Depth Reduction")
print("-" * 40)

display(
    comparison_dataset[
        [
            "Qubits",
            "Circuit_Depth_Original",
            "Circuit_Depth_Processed",
            "Circuit_Depth_Reduction_%"
        ]
    ]
)

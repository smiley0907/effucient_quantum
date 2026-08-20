# ============================================================
# CELL 15: CREATE ORIGINAL EXECUTION DATASET
# ============================================================

original_execution_dataset = pd.DataFrame({
    "Qubits": QUBIT_SIZES,

    "Gate_Count_Original": [
        original_gate_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Count": [
        original_two_qubit_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Ratio_%": [
        original_two_qubit_ratios[q]
        for q in QUBIT_SIZES
    ],

    "Circuit_Depth_Original": [
        original_circuit_depths[q]
        for q in QUBIT_SIZES
    ],

    "Median_Execution_Time_s": [
        original_execution_statistics[q]["Median_Execution_Time"]
        for q in QUBIT_SIZES
    ],

    "Mean_Execution_Time_s": [
        original_execution_statistics[q]["Mean_Execution_Time"]
        for q in QUBIT_SIZES
    ],

    "Standard_Deviation_s": [
        original_execution_statistics[q]["Standard_Deviation"]
        for q in QUBIT_SIZES
    ]
})

# Display the complete dataset
original_execution_dataset

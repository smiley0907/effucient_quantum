# ============================================================
# CELL 28: COMBINE ORIGINAL AND PROCESSED RESULTS
# ============================================================

comparison_dataset = pd.DataFrame({
    "Qubits": QUBIT_SIZES,

    "Gate_Count_Original": [
        original_gate_counts[q]
        for q in QUBIT_SIZES
    ],

    "Gate_Count_Processed": [
        processed_gate_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Count_Original": [
        original_two_qubit_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Count_Processed": [
        processed_two_qubit_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Ratio_Original_%": [
        original_two_qubit_ratios[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Ratio_Processed_%": [
        processed_two_qubit_ratios[q]
        for q in QUBIT_SIZES
    ],

    "Circuit_Depth_Original": [
        original_circuit_depths[q]
        for q in QUBIT_SIZES
    ],

    "Circuit_Depth_Processed": [
        processed_circuit_depths[q]
        for q in QUBIT_SIZES
    ],

    "Median_Execution_Time_Original_s": [
        original_execution_statistics[q]["Median_Execution_Time"]
        for q in QUBIT_SIZES
    ],

    "Median_Execution_Time_Processed_s": [
        processed_execution_statistics[q]["Median_Execution_Time"]
        for q in QUBIT_SIZES
    ]
})

comparison_dataset

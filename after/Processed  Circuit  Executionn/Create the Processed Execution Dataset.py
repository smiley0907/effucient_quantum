# ============================================================
# CELL 27: CREATE PROCESSED EXECUTION DATASET
# ============================================================

processed_execution_dataset = pd.DataFrame({
    "Qubits": QUBIT_SIZES,

    "Gate_Count_Processed": [
        processed_gate_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Count_Processed": [
        processed_two_qubit_counts[q]
        for q in QUBIT_SIZES
    ],

    "Two_Qubit_Gate_Ratio_Processed_%": [
        processed_two_qubit_ratios[q]
        for q in QUBIT_SIZES
    ],

    "Circuit_Depth_Processed": [
        processed_circuit_depths[q]
        for q in QUBIT_SIZES
    ],

    "Median_Execution_Time_Processed_s": [
        processed_execution_statistics[q]["Median_Execution_Time"]
        for q in QUBIT_SIZES
    ],

    "Mean_Execution_Time_Processed_s": [
        processed_execution_statistics[q]["Mean_Execution_Time"]
        for q in QUBIT_SIZES
    ],

    "Standard_Deviation_Processed_s": [
        processed_execution_statistics[q]["Standard_Deviation"]
        for q in QUBIT_SIZES
    ]
})

processed_execution_dataset

# ============================================================
# CELL 9: DISPLAY ORIGINAL CIRCUIT CHARACTERISTICS
# ============================================================

original_characteristics = pd.DataFrame({
    "Qubits": QUBIT_SIZES,
    "Gate_Count_Original": [
        original_gate_counts[q] for q in QUBIT_SIZES
    ],
    "Two_Qubit_Gate_Count": [
        original_two_qubit_counts[q] for q in QUBIT_SIZES
    ],
    "Two_Qubit_Gate_Ratio_%": [
        original_two_qubit_ratios[q] for q in QUBIT_SIZES
    ],
    "Circuit_Depth_Original": [
        original_circuit_depths[q] for q in QUBIT_SIZES
    ]
})

original_characteristics

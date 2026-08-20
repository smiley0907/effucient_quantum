# ============================================================
# CELL 21: CALCULATE PROCESSED TWO-QUBIT GATE RATIO
# ============================================================

processed_two_qubit_ratios = {}

for qubits in QUBIT_SIZES:

    # Get processed two-qubit gate count
    two_qubit_count = processed_two_qubit_counts[qubits]

    # Get processed total gate count
    total_gate_count = processed_gate_counts[qubits]

    # Calculate two-qubit gate ratio
    if total_gate_count > 0:
        two_qubit_ratio = (
            two_qubit_count / total_gate_count
        ) * 100
    else:
        two_qubit_ratio = 0.0

    processed_two_qubit_ratios[qubits] = two_qubit_ratio


print("Processed Two-Qubit Gate Ratio")
print("-" * 45)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"Two-Qubit Gate Ratio: "
        f"{processed_two_qubit_ratios[qubits]:.2f}%"
    )

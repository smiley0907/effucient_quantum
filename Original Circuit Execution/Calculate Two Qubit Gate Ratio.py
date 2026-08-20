# ============================================================
# CELL 7: CALCULATE TWO-QUBIT GATE RATIO
# ============================================================

original_two_qubit_counts = {}
original_two_qubit_ratios = {}

for qubits, circuit in original_circuits.items():

    # Count gates operating on exactly two qubits
    two_qubit_count = sum(
        1
        for instruction in circuit.data
        if instruction.operation.num_qubits == 2
    )

    # Get total gate count
    total_gate_count = circuit.size()

    # Calculate two-qubit gate ratio
    two_qubit_ratio = (
        two_qubit_count / total_gate_count * 100
        if total_gate_count > 0
        else 0
    )

    original_two_qubit_counts[qubits] = two_qubit_count
    original_two_qubit_ratios[qubits] = two_qubit_ratio

print("Original Two-Qubit Gate Ratio")
print("-" * 40)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"Two-Qubit Gates: {original_two_qubit_counts[qubits]}, "
        f"Ratio: {original_two_qubit_ratios[qubits]:.2f}%"
    )

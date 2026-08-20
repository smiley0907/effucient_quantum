# ============================================================
# CELL 20: CALCULATE PROCESSED TWO-QUBIT GATE COUNT
# ============================================================

processed_two_qubit_counts = {}

for qubits, circuit in processed_circuits.items():

    # Count gates that operate on exactly two qubits
    two_qubit_count = sum(
        1
        for instruction in circuit.data
        if instruction.operation.num_qubits == 2
    )

    processed_two_qubit_counts[qubits] = two_qubit_count

print("Processed Two-Qubit Gate Count")
print("-" * 45)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"Two-Qubit Gates: {processed_two_qubit_counts[qubits]}"
    )

# ============================================================
# CELL 16: GENERATE PROCESSED CIRCUITS
# ============================================================

processed_circuits = {}

for qubits in QUBIT_SIZES:

    # Retrieve the original circuit
    original_circuit = original_circuits[qubits]

    # Apply the two-qubit gate reduction procedure
    processed_circuit = reduce_two_qubit_gates(
        original_circuit
    )

    # Store the processed circuit
    processed_circuits[qubits] = processed_circuit

    print(
        f"{qubits} qubits -> "
        f"Processed circuit generated"
    )

print("\nAll processed circuits generated successfully.")

# ============================================================
# CELL 19: CALCULATE PROCESSED TOTAL GATE COUNT
# ============================================================

processed_gate_counts = {}

for qubits, circuit in processed_circuits.items():

    # Count total operations in the processed circuit
    processed_gate_counts[qubits] = circuit.size()

print("Processed Total Gate Count")
print("-" * 40)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"{processed_gate_counts[qubits]} gates"
    )

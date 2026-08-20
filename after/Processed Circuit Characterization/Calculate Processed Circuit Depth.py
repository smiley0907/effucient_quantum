# ============================================================
# CELL 22: CALCULATE PROCESSED CIRCUIT DEPTH
# ============================================================

processed_circuit_depths = {}

for qubits, circuit in processed_circuits.items():

    # Calculate circuit depth
    processed_circuit_depths[qubits] = circuit.depth()

print("Processed Circuit Depth")
print("-" * 40)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"Depth: {processed_circuit_depths[qubits]}"
    )

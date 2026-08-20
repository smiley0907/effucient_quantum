# ============================================================
# CELL 8: CALCULATE CIRCUIT DEPTH
# ============================================================

original_circuit_depths = {}

for qubits, circuit in original_circuits.items():
    original_circuit_depths[qubits] = circuit.depth()

print("Original Circuit Depth")
print("-" * 35)

for qubits in QUBIT_SIZES:
    print(
        f"{qubits} qubits -> "
        f"Depth: {original_circuit_depths[qubits]}"
    )

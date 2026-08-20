# ============================================================
# CELL 5: CALCULATE TOTAL GATE COUNT
# ============================================================

original_gate_counts = {}

for qubits, circuit in original_circuits.items():
    original_gate_counts[qubits] = circuit.size()

print("Original Total Gate Count")
print("-" * 35)

for qubits in QUBIT_SIZES:
    print(f"{qubits} qubits -> {original_gate_counts[qubits]} gates")

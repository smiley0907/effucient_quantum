# ============================================================
# CELL 6: IDENTIFY TWO QUBIT GATES
# ============================================================

two_qubit_gate_names = set()

for qubits, circuit in original_circuits.items():
    for instruction in circuit.data:
        operation = instruction.operation

        if operation.num_qubits == 2:
            two_qubit_gate_names.add(operation.name)

print("Two-Qubit Gates Identified")
print("-" * 35)

if two_qubit_gate_names:
    for gate_name in sorted(two_qubit_gate_names):
        print(gate_name)
else:
    print("No two-qubit gates identified.")

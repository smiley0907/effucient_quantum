# ============================================================
# CELL 11: PREPARE ORIGINAL CIRCUITS FOR EXECUTION
# ============================================================

execution_circuits = {}

for qubits in QUBIT_SIZES:

    circuit = original_circuits[qubits]

    execution_circuits[qubits] = transpile(
        circuit,
        simulator,
        optimization_level=0
    )

    print(
        f"{qubits} qubits -> "
        f"Execution circuit prepared"
    )

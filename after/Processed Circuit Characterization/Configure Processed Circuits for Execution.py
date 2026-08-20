# ============================================================
# CELL 23: PREPARE PROCESSED CIRCUITS FOR EXECUTION
# ============================================================

processed_execution_circuits = {}

for qubits in QUBIT_SIZES:

    circuit = processed_circuits[qubits]

    processed_execution_circuits[qubits] = transpile(
        circuit,
        simulator,
        optimization_level=0
    )

    print(
        f"{qubits} qubits -> "
        f"Processed execution circuit prepared"
    )

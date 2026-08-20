# ============================================================
# CELL 25: EXECUTE PROCESSED CIRCUITS
# ============================================================

processed_execution_times = {}

for qubits in QUBIT_SIZES:

    circuit = processed_execution_circuits[qubits]

    execution_times = []

    for _ in range(MEASUREMENT_RUNS):

        result = simulator.run(
            circuit,
            shots=SHOTS
        ).result()

        execution_times.append(result.time_taken)

    processed_execution_times[qubits] = execution_times

    print(
        f"{qubits} qubits -> "
        f"{len(execution_times)} measurements collected"
    )

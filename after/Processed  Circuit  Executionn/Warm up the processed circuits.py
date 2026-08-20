# ============================================================
# CELL 24: WARM-UP PROCESSED CIRCUITS
# ============================================================

for qubits in QUBIT_SIZES:

    circuit = processed_execution_circuits[qubits]

    for _ in range(WARMUP_RUNS):

        simulator.run(
            circuit,
            shots=SHOTS
        ).result()

    print(
        f"{qubits} qubits -> "
        f"{WARMUP_RUNS} warm-up executions completed"
    )

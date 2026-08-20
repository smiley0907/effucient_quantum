# ============================================================
# CELL 17: VERIFY CIRCUIT EQUIVALENCE
# ============================================================

from qiskit.quantum_info import Statevector, state_fidelity

equivalence_results = {}

for qubits in QUBIT_SIZES:

    # Retrieve original and processed circuits
    original_circuit = original_circuits[qubits]
    processed_circuit = processed_circuits[qubits]

    # Remove final measurement operations
    original_no_measurement = (
        original_circuit.remove_final_measurements(
            inplace=False
        )
    )

    processed_no_measurement = (
        processed_circuit.remove_final_measurements(
            inplace=False
        )
    )

    # Generate statevectors
    original_state = Statevector.from_instruction(
        original_no_measurement
    )

    processed_state = Statevector.from_instruction(
        processed_no_measurement
    )

    # Calculate state fidelity
    fidelity = state_fidelity(
        original_state,
        processed_state
    )

    equivalence_results[qubits] = fidelity

    print(
        f"{qubits} qubits -> "
        f"State Fidelity: {fidelity:.10f}"
    )

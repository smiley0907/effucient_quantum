# ============================================================
# CELL 4: GENERATE ORIGINAL GROVER CIRCUITS
# ============================================================

def create_grover_circuit(num_qubits):
    """
    Create a Grover search circuit for the specified
    number of qubits.
    """

    qc = QuantumCircuit(num_qubits)

    # Apply Hadamard gates to create superposition
    qc.h(range(num_qubits))

    # Number of Grover iterations
    iterations = max(1, int(np.floor(np.pi / 4 * np.sqrt(2 ** num_qubits))))

    for _ in range(iterations):

        # Oracle: mark the |11...1> state
        qc.x(range(num_qubits))

        # Multi-controlled phase operation
        qc.h(num_qubits - 1)
        qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
        qc.h(num_qubits - 1)

        qc.x(range(num_qubits))

        # Diffusion operator
        qc.h(range(num_qubits))
        qc.x(range(num_qubits))

        qc.h(num_qubits - 1)
        qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
        qc.h(num_qubits - 1)

        qc.x(range(num_qubits))
        qc.h(range(num_qubits))

    # Measurement
    qc.measure_all()

    return qc


# Generate circuits for all workload sizes
original_circuits = {}

for qubits in QUBIT_SIZES:
    original_circuits[qubits] = create_grover_circuit(qubits)

print("Original Grover circuits generated successfully.")

for qubits, circuit in original_circuits.items():
    print(
        f"{qubits} qubits -> "
        f"{circuit.num_qubits} qubits, "
        f"{circuit.size()} operations"
    )

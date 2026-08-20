# ============================================================
# CELL 15: DEFINE TWO-QUBIT GATE REDUCTION PROCEDURE
# ============================================================

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import CommutativeCancellation


def reduce_two_qubit_gates(circuit):
    """
    Apply a targeted optimization procedure for reducing
    redundant two-qubit gate operations.

    The circuit is first transpiled into a consistent basis.
    Commutative cancellation is then applied to identify
    cancellable gate sequences.
    """

    # Convert the circuit to a consistent basis
    basis_circuit = transpile(
        circuit,
        simulator,
        basis_gates=BASIS_GATES,
        optimization_level=0
    )

    # Apply commutation-based cancellation
    pass_manager = PassManager([
        CommutativeCancellation()
    ])

    optimized_circuit = pass_manager.run(basis_circuit)

    return optimized_circuit


print("Two-qubit gate reduction procedure defined successfully.")

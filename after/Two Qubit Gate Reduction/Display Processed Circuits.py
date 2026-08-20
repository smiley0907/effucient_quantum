# ============================================================
# CELL 18: DISPLAY PROCESSED CIRCUITS
# ============================================================

for qubits in QUBIT_SIZES:

    print("=" * 70)
    print(f"Processed Circuit: {qubits} Qubits")
    print("=" * 70)

    display(processed_circuits[qubits].draw("mpl"))

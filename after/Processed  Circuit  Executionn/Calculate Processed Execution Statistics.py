# ============================================================
# CELL 26: CALCULATE PROCESSED EXECUTION STATISTICS
# ============================================================

processed_execution_statistics = {}

for qubits in QUBIT_SIZES:

    execution_times = np.array(
        processed_execution_times[qubits]
    )

    median_time = np.median(execution_times)
    mean_time = np.mean(execution_times)
    std_time = np.std(execution_times, ddof=1)

    processed_execution_statistics[qubits] = {
        "Median_Execution_Time": median_time,
        "Mean_Execution_Time": mean_time,
        "Standard_Deviation": std_time
    }

    print(f"{qubits} qubits")
    print(f"  Median : {median_time:.6f} seconds")
    print(f"  Mean   : {mean_time:.6f} seconds")
    print(f"  Std Dev: {std_time:.6f} seconds")
    print()

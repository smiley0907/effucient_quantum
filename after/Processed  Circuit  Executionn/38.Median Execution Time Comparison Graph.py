# ============================================================
# CELL 38: MEDIAN EXECUTION TIME COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Median_Execution_Time_Original_s"],
    marker="o",
    linewidth=2,
    label="Original Circuit"
)

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Median_Execution_Time_Processed_s"],
    marker="s",
    linewidth=2,
    label="Processed Circuit"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Median Execution Time (seconds)")
plt.title("Median Execution Time Before and After Two-Qubit Optimization")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# ============================================================
# CELL 39: EXECUTION TIME IMPROVEMENT GRAPH
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Execution_Time_Improvement_%"],
    marker="o",
    linewidth=2
)

plt.xlabel("Number of Qubits")
plt.ylabel("Execution Time Improvement (%)")
plt.title("Execution Time Improvement Across Qubit Configurations")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

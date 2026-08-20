# ============================================================
# CELL 35: TWO-QUBIT GATE REDUCTION GRAPH
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Two_Qubit_Gate_Reduction_%"],
    marker="o",
    linewidth=2
)

plt.xlabel("Number of Qubits")
plt.ylabel("Two-Qubit Gate Reduction (%)")
plt.title("Two-Qubit Gate Reduction Across Qubit Configurations")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

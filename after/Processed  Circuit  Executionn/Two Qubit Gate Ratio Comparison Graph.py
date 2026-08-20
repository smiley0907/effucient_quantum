# ============================================================
# CELL 36: TWO-QUBIT GATE RATIO COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Two_Qubit_Gate_Ratio_Original_%"],
    marker="o",
    linewidth=2,
    label="Original Circuit"
)

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Two_Qubit_Gate_Ratio_Processed_%"],
    marker="s",
    linewidth=2,
    label="Processed Circuit"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Two-Qubit Gate Ratio (%)")
plt.title("Two-Qubit Gate Ratio Before and After Optimization")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

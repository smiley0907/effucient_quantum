# ============================================================
# CELL 37: CIRCUIT DEPTH COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Circuit_Depth_Original"],
    marker="o",
    linewidth=2,
    label="Original Circuit"
)

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Circuit_Depth_Processed"],
    marker="s",
    linewidth=2,
    label="Processed Circuit"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Circuit Depth")
plt.title("Circuit Depth Before and After Two-Qubit Optimization")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

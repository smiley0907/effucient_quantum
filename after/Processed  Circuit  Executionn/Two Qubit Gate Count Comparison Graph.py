# ============================================================
# CELL 34: TWO-QUBIT GATE COUNT COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Two_Qubit_Gate_Count_Original"],
    marker="o",
    label="Original Circuit"
)

plt.plot(
    final_comparison_table["Qubits"],
    final_comparison_table["Two_Qubit_Gate_Count_Processed"],
    marker="s",
    label="Processed Circuit"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Two-Qubit Gate Count")
plt.title("Two-Qubit Gate Count Before and After Optimization")

plt.xticks(QUBIT_SIZES)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

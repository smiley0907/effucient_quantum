# ============================================================
# CELL 40: EXPORT COMPLETE RESULTS DATASET
# ============================================================

# Save the final comparison results
output_file = "two_qubit_optimization_results.csv"

final_comparison_table.to_csv(
    output_file,
    index=False
)

print("Results exported successfully.")
print(f"File: {output_file}")
print(f"Rows: {len(final_comparison_table)}")
print(f"Columns: {len(final_comparison_table.columns)}")

# ============================================================
# CELL 10: CONFIGURE AER SIMULATOR
# ============================================================

simulator = AerSimulator(
    method="automatic"
)

print("Aer simulator configured successfully.")
print("Backend:", simulator.name)

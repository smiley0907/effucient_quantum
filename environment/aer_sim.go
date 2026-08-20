# ============================================================
# CELL 3: INITIALIZE QISKIT AER SIMULATOR
# ============================================================

# Create the Aer simulator used for all circuit executions
simulator = AerSimulator()

print("Qiskit Aer simulator initialized successfully.")
print("Backend:", simulator.name)

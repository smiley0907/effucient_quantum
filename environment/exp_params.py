# ============================================================
# CELL 2: DEFINE EXPERIMENT PARAMETERS
# ============================================================

# Qubit configurations used in the experiment
QUBIT_SIZES = [3, 5, 7, 9, 11]

# Number of measurement shots for each circuit execution
SHOTS = 1024

# Number of warm-up executions before collecting measurements
WARMUP_RUNS = 2

# Number of measured execution repetitions
MEASUREMENT_RUNS = 10

print("Qubit configurations :", QUBIT_SIZES)
print("Shots                :", SHOTS)
print("Warm-up runs         :", WARMUP_RUNS)
print("Measurement runs     :", MEASUREMENT_RUNS)

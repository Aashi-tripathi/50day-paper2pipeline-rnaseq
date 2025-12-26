import pandas as pd

# Example RNA-seq count matrix
counts = pd.DataFrame({
    "Gene": ["BRCA1", "TP53", "GAPDH"],
    "S1": [120, 340, 5000],
    "S2": [130, 360, 5200],
    "S3": [90, 400, 5100],
    "S4": [95, 390, 5050]
}).set_index("Gene")

# Metadata
metadata = pd.DataFrame({
    "Sample": ["S1", "S2", "S3", "S4"],
    "Condition": ["Control", "Control", "Treated", "Treated"]
})

print("Counts matrix:")
print(counts)

print("\nMetadata:")
print(metadata)

import pandas as pd

# Example RNA-seq count matrix
counts = pd.DataFrame({
    "Gene": ["BRCA1", "TP53", "GAPDH"],
    "Sample_1": [120, 340, 5000],
    "Sample_2": [98, 410, 5200],
    "Sample_3": [150, 390, 5100]
})

counts = counts.set_index("Gene")
print(counts)

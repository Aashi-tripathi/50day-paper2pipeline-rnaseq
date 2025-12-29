## 50-Day Paper → Pipeline Challenge (RNA-seq)

This repository documents my 50-day learning journey where I study RNA-seq
research papers and gradually convert them into small, reproducible
bioinformatics pipelines using Python.

### Goal
- Build strong RNA-seq fundamentals
- Improve Python and bioinformatics skills
- Learn reproducible research practices (Git, documentation)

### Current Status
- Day 1: Project setup, Python environment, Git & GitHub configuration - DONE
- Day 2: Understanding RNA-seq Data
  Today’s focus was on the core structure of RNA-seq data:
  Count matrices: rows = genes, columns = samples, values = read counts
  Metadata: sample conditions, replicates, and other experimental details
  Connecting paper descriptions to actual data objects
  Small Python experiment to visualize count matrix structure


- Day 3: Conceptual understanding of scRNA-seq data structures
  Focus:
- Conceptual understanding of single-cell RNA-seq
- How raw sequencing data is transformed into:
  - Gene expression count matrix
  - Cell-level and sample-level metadata

Key topics covered:
- Difference between bulk RNA-seq and single-cell RNA-seq
- scRNA-seq experimental workflow
- Role of barcodes and UMIs
- What a count matrix represents biologically
- What metadata contains and why it matters in analysis

Outcome:
- Built a strong foundation to interpret scRNA-seq methods sections
- Prepared to map research papers to computational pipelines

- DAY 4 – Dissecting a real scRNA-seq research paper for primary understanding 

Focus:
- Learning how scRNA-seq studies are structured
- Understanding how experimental methods translate into data objects

Tasks:
- Selected a representative scRNA-seq research paper
- Analyzed the abstract and biological question
- Carefully read the Methods section with focus on:
  - scRNA-seq platform
  - sequencing and alignment strategy
  - generation of count matrix and metadata
- Connected paper figures to underlying data structures

Outcome:
- Gained confidence in reading scRNA-seq papers from a pipeline perspective
- Identified on primary level , how raw data in public repositories relates to published results

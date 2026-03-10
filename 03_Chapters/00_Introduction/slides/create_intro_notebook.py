# Create the requested Colab/Jupyter notebook with the exact slide content
import json, uuid, textwrap, os

def md(text, slide_type="slide"):
    return {
        "cell_type": "markdown",
        "metadata": {"id": uuid.uuid4().hex[:8], "slideshow": {"slide_type": slide_type}},
        "source": textwrap.dedent(text).strip("\n").splitlines(True)
    }

def code(text, slide_type="subslide"):
    return {
        "cell_type": "code",
        "metadata": {"id": uuid.uuid4().hex[:8], "slideshow": {"slide_type": slide_type}},
        "execution_count": None,
        "outputs": [],
        "source": textwrap.dedent(text).strip("\n").splitlines(True)
    }

cells = []

# Slide 1
cells.append(md("""
# Computational Thinking for Life Scientists

### Course Introduction

Modern biology increasingly relies on computation.

This course teaches how to use **Python and computational thinking**
to analyze biological data.
"""))

# Slide 2
cells.append(md("""
## Biology is now a data science

Modern biological research generates large datasets:

• genome sequences  
• protein databases  
• biological images  
• interaction networks  

Computational tools are essential to analyze these data.
"""))

# Slide 3
cells.append(md("""
## Computational Thinking

Computational thinking is a systematic way to solve problems.

Steps:

1. Understand the biological question  
2. Build a computational model  
3. Design an algorithm  
4. Implement the algorithm in code  
5. Analyze results
"""))

# Slide 4 text
cells.append(md("""
## Computational Thinking Diagram
"""))

# Slide 4 code
cells.append(code("""
import matplotlib.pyplot as plt

steps = [
"Biological\\nQuestion",
"Model",
"Algorithm",
"Program",
"Result"
]

x = range(len(steps))

plt.figure(figsize=(10,2))
plt.scatter(x,[1]*len(x))

for i,s in enumerate(steps):
    plt.text(i,1.05,s, ha="center")

plt.plot(x,[1]*len(x))

plt.axis("off")
plt.title("Computational Thinking Pipeline")

plt.show()
"""))

cells.append(md("""
This visual helps students understand the workflow of scientific computing.
""","fragment"))

# Slide 5
cells.append(md("""
## Learning Objectives

Students will learn to:

• understand programming concepts  
• analyze biological data  
• design simple algorithms  
• implement solutions in Python  
• visualize biological information
"""))

# Slide 6
cells.append(md("""
## Skills Gained

After the course students will be able to:

• write Python programs  
• process DNA sequences  
• analyze biological datasets  
• visualize results  
• apply algorithmic thinking
"""))

# Slide 7
cells.append(md("""
## Topics Covered

1. Python programming  
2. Computational complexity  
3. Biological sequences  
4. Graphs and biological networks  
5. Image analysis  
6. Limits of computation
"""))

# Slide 8
cells.append(md("""
## Example Dataset

Suppose we study DNA sequences from several organisms.
"""))

cells.append(code("""
dna_sequences = [
"ATGCGTAC",
"ATTTGGCA",
"GCGCGCAA",
"ATATATAT",
"CGCGATTA"
]

dna_sequences
"""))

# Slide 9
cells.append(md("""
## Basic Data Analysis
"""))

cells.append(code("""
from collections import Counter

Counter(dna_sequences[0])
"""))

cells.append(md("""
Students see how code can quickly compute biological statistics.
""","fragment"))

# Slide 10
cells.append(md("""
## DNA Visualization
"""))

cells.append(code("""
from collections import Counter
import matplotlib.pyplot as plt

sequence = "ATGCGTAC"

counts = Counter(sequence)

bases = ["A","C","G","T"]
values = [counts.get(b,0) for b in bases]

plt.bar(bases, values)
plt.xlabel("Base")
plt.ylabel("Count")
plt.title("DNA nucleotide distribution")

plt.show()
"""))

cells.append(md("""
This creates a visual representation of a DNA sequence.
""","fragment"))

# Slide 11
cells.append(md("""
## Example Algorithm

GC content = percentage of nucleotides that are **G or C**.
"""))

cells.append(code("""
def GC_content(dna_string):

    GC = 0

    for nuc in dna_string:
        if nuc == "C" or nuc == "G":
            GC += 1

    return 100 * GC / len(dna_string)
"""))

# Slide 12
cells.append(md("""
## Running the Algorithm
"""))

cells.append(code("""
GC_content("ATGCGTAC")
"""))

# Slide 13
cells.append(md("""
## Concepts Introduced

This small program demonstrates:

• variables  
• loops  
• conditional statements  
• functions  
• returning results  

These are the fundamental building blocks of programming.
"""))

# Slide 14
cells.append(md("""
## Big Picture

Programming becomes a **scientific tool**.

With these skills you can:

• analyze genomes  
• explore biological networks  
• study images  
• automate scientific analysis
"""))

# Slide 15
cells.append(md("""
## Next Lecture

### Crash Introduction to Python

Topics:

• variables  
• data types  
• operators  
• loops  
• functions
"""))

nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "colab": {"name": "07_Introduction_slides.ipynb", "toc_visible": True},
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"}
    },
    "cells": cells
}

path = "/C:\Users\arief\OneDrive - Bar Ilan University\03 - BIU\01 - מבוא לחישוב ביולוגי\00 - GitHub repo\BIU-bio-python-2026\03_Chapters\00_Introduction\slides/07_Introduction_slides.ipynb"
with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

path
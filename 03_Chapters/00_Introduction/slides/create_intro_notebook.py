import json
import uuid
import textwrap

def md(text, slide="slide"):
    return {
        "cell_type": "markdown",
        "metadata": {
            "id": uuid.uuid4().hex[:8],
            "slideshow": {"slide_type": slide}
        },
        "source": textwrap.dedent(text).splitlines(True)
    }

def code(text, slide="subslide"):
    return {
        "cell_type": "code",
        "metadata": {
            "id": uuid.uuid4().hex[:8],
            "slideshow": {"slide_type": slide}
        },
        "execution_count": None,
        "outputs": [],
        "source": textwrap.dedent(text).splitlines(True)
    }

nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {"name": "python"}
    },
    "cells": []
}

cells = nb["cells"]

cells.append(md("""
# Computational Thinking for Life Scientists
## Visual Introduction Lecture
"""))

cells.append(md("""
## Computational Thinking Pipeline

Biological Question → Model → Algorithm → Program → Result
"""))

cells.append(code("""
import matplotlib.pyplot as plt

steps = ["Question","Model","Algorithm","Program","Result"]

x = range(len(steps))

plt.figure(figsize=(10,2))
plt.scatter(x,[1]*len(x))
plt.plot(x,[1]*len(x))

for i,s in enumerate(steps):
    plt.text(i,1.05,s, ha="center")

plt.axis("off")
plt.title("Computational Thinking Pipeline")
plt.show()
"""))

cells.append(md("""
# Gene Sequence Animation
"""))

cells.append(code("""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

sequence = "ATGCGTACGTTAGCCTAGGA"

fig, ax = plt.subplots(figsize=(12,2))
ax.set_xlim(-0.5,len(sequence)-0.5)
ax.set_ylim(0,1)

ax.set_xticks([])
ax.set_yticks([])

texts = []
for i in range(len(sequence)):
    t = ax.text(i,0.6,"",ha="center",fontsize=20)
    texts.append(t)

def update(frame):
    for i in range(len(sequence)):
        if i<=frame:
            texts[i].set_text(sequence[i])
        else:
            texts[i].set_text("")
    return texts

anim = FuncAnimation(fig,update,frames=len(sequence),interval=400)

HTML(anim.to_jshtml())
"""))

cells.append(md("""
# DNA Composition Visualization
"""))

cells.append(code("""
from collections import Counter

sequence="ATGCGTACGTTAGCCTAGGA"

counts=Counter(sequence)

bases=["A","C","G","T"]
values=[counts.get(b,0) for b in bases]

plt.bar(bases,values)
plt.title("DNA nucleotide distribution")
plt.show()
"""))

cells.append(md("""
# Example Algorithm: GC Content
"""))

cells.append(code("""
def GC_content(dna_string):

    GC=0

    for nuc in dna_string:
        if nuc=="C" or nuc=="G":
            GC+=1

    return 100*GC/len(dna_string)
"""))

cells.append(code("""
GC_content("ATGCGTACGTTAGCCTAGGA")
"""))

cells.append(md("""
# Biological Network Example
"""))

cells.append(code("""
import networkx as nx

G=nx.DiGraph()

G.add_edges_from([
("Signal","GeneA"),
("GeneA","GeneB"),
("GeneA","GeneC"),
("GeneB","ProteinX"),
("GeneC","ProteinY"),
("ProteinX","Response"),
("ProteinY","Response")
])

pos={
"Signal":(0,1),
"GeneA":(1,1),
"GeneB":(2,1.4),
"GeneC":(2,0.6),
"ProteinX":(3,1.4),
"ProteinY":(3,0.6),
"Response":(4,1)
}

nx.draw(G,pos,with_labels=True,node_size=2000)
plt.title("Biological Information Flow Network")
plt.show()
"""))

cells.append(md("""
# Protein Interaction Graph
"""))

cells.append(code("""
P=nx.Graph()

P.add_edges_from([
("P53","MDM2"),
("P53","ATM"),
("P53","BAX"),
("ATM","CHK2"),
("CHK2","P53"),
("BAX","CASP9"),
("MDM2","RB1"),
("RB1","E2F1"),
("E2F1","ATM")
])

pos=nx.spring_layout(P)

nx.draw(P,pos,with_labels=True,node_size=2000)
plt.title("Protein Interaction Network")
plt.show()
"""))

cells.append(md("""
# Small Biological Dataset Example
"""))

cells.append(code("""
dna_sequences=[
"ATGCGTAC",
"ATTTGGCA",
"GCGCGCAA",
"ATATATAT",
"CGCGATTA"
]

dna_sequences
"""))

cells.append(code("""
gc_values=[GC_content(s) for s in dna_sequences]

plt.bar(range(len(gc_values)),gc_values)
plt.ylabel("GC %")
plt.title("GC content of sequences")
plt.show()
"""))

cells.append(md("""
# Summary

Programming is a powerful tool for studying biological data.
"""))

with open("01_Visual_Introduction_Lecture.ipynb","w") as f:
    json.dump(nb,f,indent=2)

print("Notebook created.")
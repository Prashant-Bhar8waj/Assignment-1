
from exercise_2 import analysis
import matplotlib.pyplot as plt

# Experiment 1: Don't lowercase anything
with open("data/macbeth_en.txt", "r") as f:
    p, m = analysis("English", f.read().split())
    plt.savefig('my_plot5.png')

# Experiment 2: Use character level tokenization, rather than word level
with open("data/macbeth_en.txt", "r") as f:
    data = f.read()
    tokens = [c for c in data if c != ' ' and c != '\n']
    p, m = analysis("English", tokens)
    plt.savefig('my_plot6.png')
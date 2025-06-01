import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 6))
ax.axis('off')  # Turn off the axis

# Text for the solution steps
solution_text = (
    r"$\mathbf{Given:}$" "\n"
    r"$P(\mathrm{Cold}=Y) = 0.3$" "\n"
    r"$P(\mathrm{Cold}=N) = 0.7$" "\n"
    r"$P(\mathrm{Fever}=Y \mid \mathrm{Cold}=Y) = 0.8$" "\n"
    r"$P(\mathrm{Fever}=Y \mid \mathrm{Cold}=N) = 0.1$" "\n\n"
    
    r"$\mathbf{Bayes'\ Theorem:}$" "\n"
    r"$P(\mathrm{Cold}=Y \mid \mathrm{Fever}=Y) = \frac{P(\mathrm{Fever}=Y \mid \mathrm{Cold}=Y) \cdot P(\mathrm{Cold}=Y)}{P(\mathrm{Fever}=Y)}$" "\n\n"
    
    r"$P(\mathrm{Fever}=Y) = 0.8 \cdot 0.3 + 0.1 \cdot 0.7 = 0.24 + 0.07 = 0.31$" "\n\n"
    
    r"$P(\mathrm{Cold}=Y \mid \mathrm{Fever}=Y) = \frac{0.24}{0.31} \approx 0.774$" "\n"
    r"$P(\mathrm{Cold}=N \mid \mathrm{Fever}=Y) = \frac{0.07}{0.31} \approx 0.226$"
)

# Add the text to the figure
ax.text(0.01, 0.95, solution_text, fontsize=12, va='top', ha='left', family='monospace')

# Save as PNG
plt.tight_layout()
plt.savefig("bayesian_solution.png", dpi=300)
plt.show()

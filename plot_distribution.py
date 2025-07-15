import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the scores
df = pd.read_csv("score_output.csv")

# Plot setup
plt.figure(figsize=(10, 6))
sns.histplot(df["score"], bins=10, kde=True, color="skyblue", edgecolor="black")

# Labels and styling
plt.title("Credit Score Distribution of Wallets")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.grid(True)

# Save the plot
import os
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/score_distribution.png")

# Show the plot
plt.show()

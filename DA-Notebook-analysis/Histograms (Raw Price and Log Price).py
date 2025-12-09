# --- Histograms: Price (raw) and log(1+price) ---
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df['log_price'] = np.log1p(df['price'])

fig, axes = plt.subplots(1, 2, figsize=(12,5))

sns.histplot(df['price'], bins=50, ax=axes[0])
axes[0].set_title("Raw Price Distribution")

sns.histplot(df['log_price'], bins=50, ax=axes[1])
axes[1].set_title("Log(1+Price) Distribution")

plt.tight_layout()
plt.show()

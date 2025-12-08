# --- PCA on Scaled Numeric Features ---
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Select numeric features (include derived columns if present)
numeric_cols = ['price','availability_365','days_since_last_review','description_length']
X = df[numeric_cols].fillna(0)

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Explained variance table
explained_variance = pd.DataFrame({
    'PC': [f'PC{i+1}' for i in range(len(pca.explained_variance_ratio_))],
    'Explained Variance Ratio': pca.explained_variance_ratio_
})
print("Explained Variance Ratios:\n", explained_variance)

# Scatter plot PC1 vs PC2 colored by neighbourhood_group
plt.figure(figsize=(8,6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['neighbourhood_group'], palette='Set2', alpha=0.7)
plt.title("PCA: PC1 vs PC2 (colored by neighbourhood_group)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(title="Neighbourhood Group")
plt.show()

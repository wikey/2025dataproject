# --- Correlation Matrix and Heatmap ---
corr_matrix = df[['price','availability_365','days_since_last_review','description_length']].corr()

print("Correlation Matrix:\n", corr_matrix)

plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Heatmap (Numeric Features)")
plt.show()

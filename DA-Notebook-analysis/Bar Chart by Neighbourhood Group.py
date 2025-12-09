# --- Bar Chart: Listing Counts by Neighbourhood Group ---
if 'neighbourhood_group' in df.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(x='neighbourhood_group', data=df, order=df['neighbourhood_group'].value_counts().index)
    plt.title("Listing Counts by Neighbourhood Group")
    plt.xlabel("Neighbourhood Group")
    plt.ylabel("Count")
    plt.show()
else:
    print("Column 'neighbourhood_group' not found in DataFrame.")

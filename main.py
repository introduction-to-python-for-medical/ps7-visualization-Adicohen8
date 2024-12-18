reference_feature = selected_features[1]  # The reference feature
comparison_feature = selected_features[2]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6, c='purple', edgecolors='black')
plt.xlabel(reference_feature, fontsize = 18)
plt.ylabel(comparison_feature, fontsize = 18)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()

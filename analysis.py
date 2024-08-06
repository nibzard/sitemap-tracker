import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('dummy_sitemap_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot the data
plt.figure(figsize=(14, 8))

# Plot Total URLs
sns.lineplot(data=df[df['Sitemap'] == 'definitions'], x='Date', y='Total URLs', label='Total URLs - Definitions', marker='o')
sns.lineplot(data=df[df['Sitemap'] == 'dotfiles'], x='Date', y='Total URLs', label='Total URLs - Dotfiles', marker='o')

# Plot New URLs
sns.lineplot(data=df[df['Sitemap'] == 'definitions'], x='Date', y='New URLs', label='New URLs - Definitions', marker='x')
sns.lineplot(data=df[df['Sitemap'] == 'dotfiles'], x='Date', y='New URLs', label='New URLs - Dotfiles', marker='x')

# Customize plot
plt.title('URL Metrics Over Time')
plt.xlabel('Date')
plt.ylabel('Number of URLs')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('url_metrics_over_time.png')
plt.show()
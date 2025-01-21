#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('boston_311_2023_raw.csv')

# Group the data by the 'reason' column and count the occurrences of each reason
reason_counts = data.groupby('reason').size().reset_index(name='Count')

# Save the result to a new CSV file (optional)
reason_counts.to_csv('boston_311_2023_by_reason.csv', index=False)

# Sort the reasons by count and select the top 10
top_10_reasons = reason_counts.sort_values(by='Count', ascending=False).head(10)

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_10_reasons['reason'], top_10_reasons['Count'], color='skyblue')

# Add labels, title, and citation
plt.xlabel('Number of Calls', fontsize=12)
plt.ylabel('Reason', fontsize=12)
plt.title("Top 10 Reasons for 311 Calls in Boston (2023)", fontsize=16)
plt.figtext(0.5, -0.1, "Data Source: Boston 311, Author: Your Name", ha="center", fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the chart as an image
plt.savefig('top_10_reasons_311_calls_horizontal.png')

# Show the chart
plt.show()

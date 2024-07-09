# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Step 2: Load the dataset
# Assuming the dataset is a CSV file. Replace 'your_dataset.csv' with your actual file name.
df = pd.read_csv('your_dataset.csv')

# Step 3: Data Summary
print("First few rows of the dataset:")
print(df.head())

print("\nSummary of the dataset:")
print(df.info())

print("\nSummary statistics of the dataset:")
print(df.describe())

# Step 4: Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Optionally, handle missing values (e.g., by dropping or imputing)
# df = df.dropna() # Drop rows with missing values
# df.fillna(df.mean(), inplace=True) # Impute missing values with mean

# Step 5: Univariate Analysis
# Distribution of numerical variables
num_vars = df.select_dtypes(include=['float64', 'int64']).columns
for var in num_vars:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[var], kde=True)
    plt.title(f'Distribution of {var}')
    plt.show()

# Distribution of categorical variables
cat_vars = df.select_dtypes(include=['object']).columns
for var in cat_vars:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df[var])
    plt.title(f'Distribution of {var}')
    plt.show()

# Step 6: Bivariate Analysis
# Scatter plot for numerical variables
for var1 in num_vars:
    for var2 in num_vars:
        if var1 != var2:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=df[var1], y=df[var2])
            plt.title(f'Scatter plot of {var1} vs {var2}')
            plt.show()

# Correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df[num_vars].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Step 7: Outliers
# Box plots to identify outliers
for var in num_vars:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[var])
    plt.title(f'Box plot of {var}')
    plt.show()

# Optionally, handle outliers (e.g., by removing)
# Z-score method to remove outliers
# df = df[(np.abs(zscore(df[num_vars])) < 3).all(axis=1)]

print("\nEDA completed.")

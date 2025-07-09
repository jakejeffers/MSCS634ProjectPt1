# %% [markdown]
# # OpenPowerlifting Data Cleaning and EDA
# Deliverable 1 – MSCS 634 Project

# %% Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% Load the dataset
df = pd.read_csv('openpowerlifting-2021-06-26-027dc895.csv', low_memory=False)

# %% Initial Inspection
print("\n--- Dataset Overview ---")
print(df.shape)
print(df.info())
print(df.head())

# %% Check and Report Missing Values
print("\n--- Missing Values (Top 20) ---")
missing = df.isnull().sum().sort_values(ascending=False)
print(missing.head(20))

# %% Drop Columns with Excessive Nulls
columns_to_drop = ['Squat4Kg', 'Bench4Kg', 'Deadlift4Kg', 'MeetState', 'Tested', 'MeetCountry']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# %% Clean Rows
df.dropna(subset=['TotalKg'], inplace=True)
df['BodyweightKg'] = df['BodyweightKg'].fillna(df['BodyweightKg'].mean())
df.drop_duplicates(inplace=True)

# %% Post-cleaning Summary
print("\n--- Post-cleaning Missing Values ---")
missing_cleaned = df.isnull().sum().sort_values(ascending=False)
print(missing_cleaned[missing_cleaned > 0])

print("\n--- Cleaned Dataset Summary ---")
print(df.describe())

# %% EDA: Distribution of Total Weight Lifted
plt.figure(figsize=(8, 4))
sns.histplot(df['TotalKg'], bins=50, kde=True)
plt.title('Distribution of Total Weight Lifted')
plt.xlabel('TotalKg')
plt.ylabel('Number of Lifters')
plt.tight_layout()
plt.show()

# %% EDA: Gender Distribution
plt.figure(figsize=(5, 4))
sns.countplot(data=df, x='Sex')
plt.title('Lifter Gender Distribution')
plt.tight_layout()
plt.show()

# %% EDA: Boxplot - Total Weight by Gender
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='Sex', y='TotalKg')
plt.title('Total Weight by Gender')
plt.tight_layout()
plt.show()

# %% EDA: Correlation Heatmap
plt.figure(figsize=(12, 8))
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()


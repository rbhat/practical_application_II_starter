import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/vehicles.csv')

# Data Cleaning and Preprocessing

# Handle missing values (simple imputation for demonstration)
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)


# Convert data types
df['year'] = pd.to_datetime(df['year'], errors='coerce').dt.year
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')

# Remove rows with invalid price or odometer values
df.dropna(subset=['price', 'odometer'], inplace=True)
df = df[df['price'] > 0]
df = df[df['odometer'] >= 0]

# Exploratory Data Analysis (EDA)

# Analyze price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True)
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Analyze relationship between price and year
plt.figure(figsize=(10, 6))
sns.scatterplot(x='year', y='price', data=df)
plt.title('Price vs. Year')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

# Analyze relationship between price and odometer
plt.figure(figsize=(10, 6))
sns.scatterplot(x='odometer', y='price', data=df)
plt.title('Price vs. Odometer')
plt.xlabel('Odometer')
plt.ylabel('Price')
plt.show()

# Analyze relationship between price and other categorical features (example: condition)
plt.figure(figsize=(10, 6))
sns.boxplot(x='condition', y='price', data=df)
plt.title('Price vs. Condition')
plt.xlabel('Condition')
plt.ylabel('Price')
plt.show()

#Further analysis and model building can be added here.

# Recommendations (Preliminary)

# Based on the initial EDA, it appears that:
# * Newer cars generally command higher prices.
# * Lower odometer readings are associated with higher prices.
# * Car condition significantly impacts price.

# Further analysis is needed to quantify these relationships and identify other important factors.  More sophisticated models (e.g., regression) could be used to determine feature importance and build a predictive model for car prices.  This would allow for more precise recommendations.
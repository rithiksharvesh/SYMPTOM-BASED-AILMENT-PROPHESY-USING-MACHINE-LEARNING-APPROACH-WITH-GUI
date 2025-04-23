# data_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load data
train_df = pd.read_csv('Training.csv')
test_df = pd.read_csv('Testing.csv')

# Basic info
print("Train Data Shape:", train_df.shape)
print("Test Data Shape:", test_df.shape)
print(train_df.head())

# Check for missing values
print(train_df.isnull().sum())

# Encode target labels
le = LabelEncoder()
train_df['prognosis'] = le.fit_transform(train_df['prognosis'])
test_df['prognosis'] = le.transform(test_df['prognosis'])

# Save label mappings
disease_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print("Disease Mapping:", disease_mapping)

# Feature correlation (optional for visualization)
plt.figure(figsize=(10, 6))
sns.heatmap(train_df.drop('prognosis', axis=1).corr().iloc[:10, :10], annot=True)
plt.title("Feature Correlation Heatmap (Partial)")
plt.tight_layout()
plt.show()

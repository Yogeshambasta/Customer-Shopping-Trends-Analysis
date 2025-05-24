import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r"D:\games\customer\shopping_trends.csv")  # Replace with your actual dataset path
print(df.head())

# Rename useful columns for consistency
df['CustomerID'] = df['Customer ID']
df['ProductCategory'] = df['Category']
df['AmountSpent'] = df['Purchase Amount (USD)']

# Simulate VisitDate if not already present
if 'VisitDate' not in df.columns:
    np.random.seed(42)
    df['VisitDate'] = pd.to_datetime('2024-01-01') + pd.to_timedelta(
        np.random.randint(0, 120, size=len(df)), unit='D'
    )

# Add a 'Month' column for monthly analysis
df['Month'] = df['VisitDate'].dt.to_period('M')


# 1. Frequency of Visits per Customer Over Time

visit_freq = df.groupby(['CustomerID', 'Month']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
for customer_id in visit_freq.index[:5]:  # Sample 5 customers
    plt.plot(visit_freq.columns.astype(str), visit_freq.loc[customer_id], label=f"Customer {customer_id}")

plt.title("Monthly Visit Frequency (Sample Customers)")
plt.xlabel("Month")
plt.ylabel("Number of Visits")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ---------------------------------------
# 2. Total Spending per Customer
# ---------------------------------------
total_spent = df.groupby('CustomerID')['AmountSpent'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
total_spent.head(10).plot(kind='bar', color='steelblue')
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Amount Spent (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------
# 3. Spending by Product Category
# ---------------------------------------
category_spending = df.groupby('ProductCategory')['AmountSpent'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(category_spending, labels=category_spending.index, autopct='%1.1f%%', startangle=140)
plt.title("Spending Distribution by Product Category")
plt.tight_layout()
plt.show()

# Age distribution
plt.figure(figsize=(8,6))
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Spending by gender
gender_spending = df.groupby('Gender')['AmountSpent'].sum()
plt.figure(figsize=(6,4))
gender_spending.plot(kind='bar', color='lightcoral')
plt.title("Total Spending by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Spending (USD)")
plt.tight_layout()
plt.show()











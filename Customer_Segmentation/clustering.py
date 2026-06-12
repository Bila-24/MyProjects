import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Load data
df = pd.read_csv("customers.csv")

print(df.head())
X = df[["Age", "Income", "SpendingScore"]]
kmeans = KMeans(n_clusters=3, random_state=42)

df["Cluster"] = kmeans.fit_predict(X)

print(df)
plt.scatter(df["Income"], df["SpendingScore"], c=df["Cluster"])

plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments")

plt.show()
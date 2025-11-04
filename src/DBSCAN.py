"""
DBSCAN Customer Clustering and Behavioral Analysis (From Scratch)
Author: Vamsi Gudipudi
Description:
    Pure Python implementation of DBSCAN for customer segmentation
    using Recency, Frequency, and Monetary analysis.
    Generates 3D plots, outlier details, and cluster behavioral insights.
"""

import math
import os
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==================== Utility Functions ====================

def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def compute_rfm_with_ids(data):
    """Compute Recency, Frequency, and Monetary for each Customer_ID."""
    customer_rfm = {}
    today = datetime.datetime(2025, 5, 1)

    for record in data:
        cust_id = record['Customer_ID']
        date = datetime.datetime.strptime(record['Date'], "%Y-%m-%d")
        amount = float(record['Total_Amount'])

        if cust_id not in customer_rfm:
            customer_rfm[cust_id] = {'recency': (today - date).days, 'frequency': 0, 'monetary': 0}
        else:
            customer_rfm[cust_id]['recency'] = min(customer_rfm[cust_id]['recency'], (today - date).days)
        customer_rfm[cust_id]['frequency'] += 1
        customer_rfm[cust_id]['monetary'] += amount

    dataset, ids = [], []
    for cust_id, values in customer_rfm.items():
        dataset.append([values['recency'], values['frequency'], values['monetary']])
        ids.append(cust_id)
    return dataset, ids


def euclidean_distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))


def region_query(dataset, point_idx, eps):
    neighbors = []
    for i, point in enumerate(dataset):
        if euclidean_distance(dataset[point_idx], point) <= eps:
            neighbors.append(i)
    return neighbors


def expand_cluster(dataset, labels, point_idx, cluster_id, eps, min_pts):
    neighbors = region_query(dataset, point_idx, eps)
    if len(neighbors) < min_pts:
        labels[point_idx] = -1
        return False
    else:
        labels[point_idx] = cluster_id
        i = 0
        while i < len(neighbors):
            n_idx = neighbors[i]
            if labels[n_idx] == 0:
                labels[n_idx] = cluster_id
                new_neighbors = region_query(dataset, n_idx, eps)
                if len(new_neighbors) >= min_pts:
                    neighbors.extend(new_neighbors)
            elif labels[n_idx] == -1:
                labels[n_idx] = cluster_id
            i += 1
        return True


def dbscan(dataset, eps, min_pts):
    labels = [0] * len(dataset)
    cluster_id = 0
    for i in range(len(dataset)):
        if labels[i] == 0:
            if expand_cluster(dataset, labels, i, cluster_id + 1, eps, min_pts):
                cluster_id += 1
    return labels


# ==================== Analysis Logic ====================

def interpret_cluster(row):
    """Behavioral interpretation based on RFM averages."""
    if row['Avg_Recency'] < 150 and row['Avg_Frequency'] > 10 and row['Avg_Monetary'] > 10000:
        return "Loyal / High-Value Customers"
    elif row['Avg_Recency'] > 300 and row['Avg_Frequency'] < 5 and row['Avg_Monetary'] < 5000:
        return "Lost / Inactive Customers"
    elif row['Avg_Recency'] < 200 and row['Avg_Frequency'] < 10 and row['Avg_Monetary'] < 8000:
        return "Occasional / Mid-Spenders"
    else:
        return "Potential Loyalists / Average Buyers"


def interpret_outlier(row):
    if row["Monetary"] > 12000:
        return "VIP / High-Spending Customer"
    elif row["Monetary"] < 3000:
        return "Low-Value / Inactive Customer"
    else:
        return "Irregular Mid-Spender"


def run_dbscan_analysis(filename):
    """Run DBSCAN at multiple eps values and analyze results."""

    data = load_dataset(filename)
    dataset, ids = compute_rfm_with_ids(data)
    df_rfm = pd.DataFrame(dataset, columns=["Recency", "Frequency", "Monetary"])
    df_rfm["Customer_ID"] = ids

    eps_values = [500, 1000, 3000]
    min_pts = 4

    all_summaries = []
    all_outliers = []

    for eps in eps_values:
        labels = dbscan(dataset, eps, min_pts)
        df_rfm[f'Cluster_eps_{eps}'] = labels

        # 3D Scatter plot with outliers
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        noise_mask = [l == -1 for l in labels]
        cluster_mask = [l != -1 for l in labels]

        ax.scatter(df_rfm.loc[cluster_mask, 'Recency'],
                   df_rfm.loc[cluster_mask, 'Frequency'],
                   df_rfm.loc[cluster_mask, 'Monetary'],
                   c=df_rfm.loc[cluster_mask, f'Cluster_eps_{eps}'],
                   cmap='viridis', s=50, label='Clusters')

        ax.scatter(df_rfm.loc[noise_mask, 'Recency'],
                   df_rfm.loc[noise_mask, 'Frequency'],
                   df_rfm.loc[noise_mask, 'Monetary'],
                   c='red', s=60, marker='x', label='Outliers / Noise')

        ax.set_title(f"DBSCAN Clusters (eps={eps}, min_pts={min_pts})")
        ax.set_xlabel("Recency")
        ax.set_ylabel("Frequency")
        ax.set_zlabel("Monetary")
        ax.legend()
        plt.show()

        # Cluster Summary
        df_tmp = df_rfm.copy()
        df_tmp["Cluster"] = labels
        cluster_summary = df_tmp[df_tmp["Cluster"] != -1].groupby("Cluster").agg(
            Customers=('Customer_ID', 'count'),
            Avg_Recency=('Recency', 'mean'),
            Avg_Frequency=('Frequency', 'mean'),
            Avg_Monetary=('Monetary', 'mean')
        ).reset_index()

        cluster_summary["Behavior"] = cluster_summary.apply(interpret_cluster, axis=1)
        cluster_summary["eps"] = eps
        all_summaries.append(cluster_summary)

        # Outlier Details
        outliers = df_tmp[df_tmp["Cluster"] == -1][["Customer_ID", "Recency", "Frequency", "Monetary"]]
        outliers["Category"] = outliers.apply(interpret_outlier, axis=1)
        outliers["eps"] = eps
        all_outliers.append(outliers)

        print(f"\n=== Cluster Summary (eps={eps}) ===")
        print(cluster_summary.to_string(index=False))
        print(f"\n=== Outlier Customers (eps={eps}) ===")
        print(outliers.to_string(index=False))

    # Combine and save
    all_summary_df = pd.concat(all_summaries)
    all_outlier_df = pd.concat(all_outliers)
    all_summary_df.to_csv("DBSCAN_All_Cluster_Summary.csv", index=False)
    all_outlier_df.to_csv("DBSCAN_All_Outliers.csv", index=False)

    print("\nAll results saved to:")
    print(" DBSCAN_All_Cluster_Summary.csv")
    print(" DBSCAN_All_Outliers.csv")


# ==================== Run ====================
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))        # points to src/
    data_path = os.path.join(base_dir, "..", "data", "synthetic_visits.csv")  # go up one folder, then into data/
    
    run_dbscan_analysis(data_path)

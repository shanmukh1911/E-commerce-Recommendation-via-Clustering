# 🧩 E-Commerce Customer Segmentation (DBSCAN + K-Means from Scratch)

**Author:** Shanmukha Srinivas Regidi  
**Institute:** IIT Goa  
**Description:**  
End-to-end customer segmentation using **DBSCAN (manual implementation)** and **K-Means** clustering, driven by **RFM (Recency, Frequency, Monetary)** analysis.  
The project extracts patterns from synthetic e-commerce data to identify **loyal customers, inactive users, and high-value VIPs**.

---

##  Project Overview

This project combines **K-Means** and **DBSCAN** clustering methods to understand e-commerce customer behavior.  
Using RFM metrics derived from purchase data, customers are grouped into actionable business segments and visualized in 3D.

| Method | Description |
|---------|-------------|
| **K-Means** | Partition-based algorithm used to form distinct spherical clusters. Used for baseline segmentation. |
| **DBSCAN** | Density-based algorithm capable of detecting arbitrary cluster shapes and identifying outliers. |

---

##  Key Features

 Computes **Recency, Frequency, Monetary (RFM)** directly from transactions  
 Implements **DBSCAN from scratch (no scikit-learn)**  
 Includes **K-Means** notebook for comparative analysis  
 Visualizes clusters and elbow method for K-Means  
 Highlights **VIP / Outlier customers** detected by DBSCAN  
 Saves **cluster summaries** and **outlier lists** into `/results`  

---

##  Project Structure

```
E-Commerce/
│
├── data/
│   └── synthetic_visits.csv
│
├── notebooks/
│   ├── K_Means.ipynb
│   ├── DataSet_Synthesis.ipynb
│   └── DBSCAN.ipynb
│
├── src/
│   └── DBSCAN_Full_Analysis_From_Scratch.py
│
├── results/
│   ├── DBSCAN_All_Cluster_Summary.csv
│   ├── DBSCAN_All_Outliers.csv
│
├── plots/
│   ├── eps500_plot.png
│   ├── eps1000_plot.png
│   ├── eps3000_plot.png
│   └── kmeans_elbow_curve.png
│
├── README.md
└── requirements.txt
```

---

##  Input Data

Located at **`data/synthetic_visits.csv`**

| Column | Description |
|--------|-------------|
| `Customer_ID` | Unique customer identifier |
| `Date` | Transaction date (YYYY-MM-DD) |
| `Total_Amount` | Transaction amount |

---

##  How to Run

###  Run DBSCAN Analysis
```bash
cd E-Commerce
python src/DBSCAN_Full_Analysis_From_Scratch.py
```

Outputs will be stored in the `/results/` folder.

###  Run K-Means Analysis
Open the Jupyter notebook:
```
notebooks/K_Means.ipynb
```
This notebook contains:
- Elbow curve to determine optimal `k`
- Cluster visualizations for RFM data
- Comparison of K-Means and DBSCAN segmentations

---

##  Results and Visualizations

| Method | Visualization | Insight |
|---------|----------------|----------|
| **K-Means (k=3)** | ![Elbow Curve](docs/kmeans_elbow_curve.png) | Shows 3 optimal customer groups |
| **DBSCAN (eps=500)** | ![DBSCAN 500](docs/eps500_plot.png) | Distinct small clusters with VIP outliers |
| **DBSCAN (eps=1000)** | ![DBSCAN 1000](docs/eps1000_plot.png) | Moderate merging of clusters |
| **DBSCAN (eps=3000)** | ![DBSCAN 3000](docs/eps3000_plot.png) | Broad single cluster |

---

##  Behavioral Insights (Sample)

| Segment | Description | Example Behavior |
|----------|--------------|------------------|
| Loyal / High-Value Customers | Frequent buyers, high monetary value | Visit often and spend consistently |
| Occasional / Mid-Spenders | Moderate spending & activity | Purchase seasonally |
| Lost / Inactive Customers | Rare or old buyers | Haven’t purchased recently |
| VIP / Outliers | Unique or extreme spending patterns | High-value or inconsistent buyers |

---

##  Output Files

| File | Description |
|------|--------------|
| `results/DBSCAN_All_Cluster_Summary.csv` | Summary of clusters with RFM averages |
| `results/DBSCAN_All_Outliers.csv` | Outlier customers with behavioral labels |

---

##  Tech Stack
- Python (DBSCAN logic manually implemented)
- Pandas, Matplotlib
- Jupyter Notebooks for visualization

---

##  Author
**Shanmukha Srinivas Regidi**  
B.Tech in Mathematics and Computing, IIT Goa  
Focus: Data Science, Machine Learning, and Systems Analysis

---

##  Future Work
- Add **Hierarchical Clustering** for comparison  
- Build an **interactive dashboard** for segmentation visualization  
- Apply to **real e-commerce transaction datasets**

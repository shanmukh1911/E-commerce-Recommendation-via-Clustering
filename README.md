# 🧩 DBSCAN Customer Segmentation (From Scratch)

**Author:** Shanmukha Srinivas Regidi  
**Description:**  
Pure Python implementation of the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm for customer segmentation using Recency, Frequency, and Monetary (RFM) analysis.

---

## 🧾 Overview

This project segments customers into distinct behavioral groups using DBSCAN.  
It identifies clusters of customers with similar purchase patterns and detects outliers representing unique or irregular spending behavior.

---

## ⚙️ Features

✅ Computes **Recency, Frequency, and Monetary (RFM)** values directly from raw transactions  
✅ Implements **DBSCAN manually** (no scikit-learn)  
✅ Runs clustering for multiple eps values (`500`, `1000`, `3000`)  
✅ Generates **3D scatter plots** with outliers highlighted in red  
✅ Saves **cluster summaries** and **outlier details** as CSV files

---

## 📊 Input Format

The dataset should be named **`synthetic_visits.csv`** and contain the following columns:

| Column | Description |
|--------|-------------|
| Customer_ID | Unique customer identifier |
| Date | Transaction date (YYYY-MM-DD) |
| Total_Amount | Amount spent in that transaction |

---

## 🚀 How to Run

1. Place your dataset (`synthetic_visits.csv`) in the same folder as the script.  
2. Run the script:

```bash
python DBSCAN_Full_Analysis_From_Scratch.py
```

3. Outputs will be saved in the **results/** folder.

---

## 📈 Outputs

| File | Description |
|------|--------------|
| `DBSCAN_All_Cluster_Summary.csv` | Cluster-level stats and behavioral labels |
| `DBSCAN_All_Outliers.csv` | Customer IDs and RFM values of outliers |

3D visualizations will appear for each `eps` value:  
- **eps = 500:** Fine-grained clusters + VIP outliers  
- **eps = 1000:** Moderate merging of groups  
- **eps = 3000:** Broad unified cluster

---

## 🧠 Behavioral Interpretation

| Category | Meaning |
|-----------|----------|
| Loyal / High-Value Customers | Frequent and recent buyers with high spending |
| Occasional / Mid-Spenders | Moderate buyers with stable activity |
| Lost / Inactive Customers | Rare buyers or old customers |
| VIP / Outliers | Exceptional or irregular customers detected as noise |

---

## 👨‍💻 Author
**Shanmukha Srinivas Regidi**  
B.Tech in Mathematics and Computing, IIT Goa  


---

## 🏁 Future Work
- Add **K-Means** comparison visualization  
- Introduce **automatic eps tuning** (k-distance graph)  
- Extend to **real-world e-commerce datasets**

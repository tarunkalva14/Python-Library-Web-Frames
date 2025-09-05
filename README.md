# PySpark With Python

This project explores the **BigMart Sales dataset**,**test1 dataset**,**tips dataset** using **PySpark** in **Google Colab**.  
The main objective is to clean, transform, and analyze the data to extract useful insights about sales patterns and product performance.

---

## 🚀 Project Overview
- **Dataset**: `BigMart Sales.csv`,`test1.csv`,`tips.csv`
- **Environment**: Google Colab (PySpark)  
- **Goal**: Perform exploratory data analysis (EDA), handle missing values, and prepare the dataset for potential predictive modeling.

---

## 📂 Steps Covered
1. **Setup Environment**
   - Install and configure PySpark in Colab.
   - Mount Google Drive to access dataset.

2. **Data Loading**
   - Read `BigMart Sales.csv`,`test1.csv`,`tips.csv` into a PySpark DataFrame.
   - Inspect schema and column types.

3. **Data Cleaning**
   - Handle null or missing values.
   - Standardize categorical columns.
   - Fix inconsistent entries (e.g., item types).

4. **Exploratory Data Analysis (EDA)**
   - Summary statistics for numerical features.
   - GroupBy operations to find sales trends.
   - Visualizations (with Matplotlib/Seaborn after converting to Pandas when needed).

5. **Feature Engineering (Optional)**
   - Encoding categorical variables.
   - Creating new derived columns for analysis.

---

## 🔧 Technologies Used
- **Python**
- **PySpark (DataFrame API)**
- **Google Colab**
- **Pandas / Matplotlib (for some plots)**

---

## 📊 Example Analysis
- Average sales by outlet type.
- Impact of item visibility on sales.
- Distribution of sales across item categories.

---

## ▶️ How to Run
1. Open Google Colab.
2. Upload or connect your Google Drive with `BigMart Sales.csv`.
3. Upload or connect your Google Drive with `test1.csv`.
4. Upload or connect your Google Drive with `tips.csv`.
5. Run the notebook cells step by step.
   ```python
   from google.colab import drive
   drive.mount('/content/drive')

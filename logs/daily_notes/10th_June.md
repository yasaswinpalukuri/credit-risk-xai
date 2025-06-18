# Day 02 - 2025-06-10

## ✅ Tasks Done
- Loaded the processed dataset from Day 01
- Converted 'Risk' to binary format (Good → 0, Bad → 1)
- Handled missing values in categorical features by assigning 'Unknown'
- Learned the concept of Weight of Evidence (WoE) and Information Value (IV)
- Created reusable WoE + IV calculation function in `src/data_prep.py`
- Visualized WoE binning for each categorical feature
- Ranked features by IV and plotted an importance bar chart
- Resolved a `ModuleNotFoundError` by modifying the Jupyter notebook to recognize the `src/` folder

## 🧠 Concepts Learned
- WoE transforms help make categorical features interpretable for linear models
- IV provides a quantitative way to measure feature usefulness for classification
- Importance of managing relative paths in Jupyter for custom Python modules

## ❓Doubts
- Should we convert all categorical variables to WoE now or only top-IV features?
- Should we try automatic binning for numerical features too?

## 🔁 Tomorrow’s Plan
- Finalize list of features to use in the model (based on IV threshold)
- Apply WoE transformation to those features
- Prepare train-test split for modeling
- Begin baseline model: Logistic Regression, Decision Tree
# Day 01 - 2025-06-09

## ✅ Tasks Done
- Set up complete project folder structure in VS Code
- Downloaded and loaded German Credit dataset
- Created synthetic `Risk` target using business rules (credit amount, duration, account info)
- Performed initial EDA: data types, target class balance, missing values
- Saved processed data to `data/processed/credit_data_with_risk.csv`
- Initialized Git repository and connected it to GitHub
- Created `.gitkeep` files to preserve empty folders in version control
- Committed and pushed initial project to GitHub
- Added a polished `README.md` with structure, tech stack, and roadmap

## 🧠 Concepts Learned
- How to simulate binary classification targets when not directly provided
- Importance of class balance in real-world datasets
- What `.gitkeep` is and why it matters for versioning
- First full GitHub push with `.gitignore` best practices

## ❓Doubts
- Should the Risk logic be tweaked further for finer realism?
- Would LabelEncoder or OneHotEncoder make sense for WoE fallback?

## 🔁 Tomorrow’s Plan
- Handle missing values in categorical variables
- Learn and apply WoE (Weight of Evidence) binning
- Calculate IV (Information Value) for feature selection
- Save cleaned + transformed dataset
- Begin work in `src/data_prep.py` and `woe_iv_analysis.ipynb`
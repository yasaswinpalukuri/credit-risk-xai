
# 🧠 Credit Risk Scoring with Explainable AI (XAI)

A machine learning pipeline to assess customer creditworthiness using real-world German credit data. This project simulates a banking-grade credit scoring model with explainable outputs using SHAP and Weight of Evidence (WoE).

---

## 📌 Problem Statement

Financial institutions need to assess whether a customer is likely to default on a loan. This project aims to:
- Build a credit risk prediction model using customer financial and demographic data.
- Use interpretable ML techniques so risk analysts and compliance teams can understand decisions.

---

## 🔍 Dataset

- **Source**: [German Credit Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/german-credit)
- **Records**: 1,000
- **Target**: Synthetic `Risk` label created using rules on credit amount, duration, and account types.
- **Features**: Age, Job type, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose.

---

## ⚙️ Tech Stack

| Component         | Tool/Library                |
|------------------|-----------------------------|
| Language         | Python                      |
| Data Handling    | Pandas, Numpy               |
| Modeling         | XGBoost, Scikit-learn       |
| Feature Encoding | WoE Binning, IV             |
| Explainability   | SHAP                        |
| Dashboard        | Streamlit                   |
| Containerization | Docker                      |
| Version Control  | Git, GitHub                 |

---

## 📁 Project Structure

```
credit-risk-xai/
│
├── data/               # Raw + processed data
├── notebooks/          # EDA and analysis notebooks
├── src/                # Source code: preprocessing, modeling
├── app/                # Streamlit app files
├── docker/             # Dockerfile and container setup
├── logs/               # Daily learning + dev logs
├── README.md
└── requirements.txt
```

---

## 🧪 Completed

- [x] Project folder scaffold
- [x] EDA on credit dataset
- [x] Created `Risk` target column from domain logic
- [x] Set up GitHub tracking with `.gitkeep`
- [x] Daily logging template
- [ ] WoE Binning + IV computation
- [ ] ML model (XGBoost) + SHAP explanation
- [ ] Streamlit deployment
- [ ] Docker containerization

---

## 🚀 Setup Instructions

```bash
# Clone this repo
git clone https://github.com/yasaswinpalukuri/credit-risk-xai.git
cd credit-risk-xai

# Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Or . .venv/bin/activate on Mac/Linux

# Install requirements
pip install -r requirements.txt

# Start working on notebooks
jupyter notebook
```

---

## 📊 Example Screenshots (Coming Soon)

<!--
Add screenshots from:
- EDA visualizations
- SHAP output plots
- Streamlit app (risk score prediction)
-->

---

## 🧠 Learning Goals

- Simulate a real-world ML problem in finance
- Learn Weight of Evidence (WoE) and Information Value (IV)
- Apply SHAP to interpret predictions
- Build and deploy a model-ready app

---

## 👥 Author

**Yasaswin Palukuri**  
📍 Data Science & AI Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/yasaswinpalukuri)

---

## 📌 License

MIT License. Free to use, modify, and deploy.
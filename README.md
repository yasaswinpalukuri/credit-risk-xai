
# 🧠 Credit Risk Scoring with Explainable AI (XAI)

A machine learning pipeline to assess customer creditworthiness using real-world German credit data. This project simulates a banking-grade credit scoring model with explainable outputs using SHAP, Weight of Evidence (WoE), and GridSearchCV optimization.

---

## 📌 Problem Statement

Financial institutions need to assess whether a customer is likely to default on a loan. This project aims to:
- Build a credit risk prediction model using customer financial and demographic data.
- Apply interpretable ML techniques to help risk analysts and compliance teams understand model decisions.

---

## 🔍 Dataset

- **Source**: [German Credit Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/german-credit)
- **Records**: 1,000
- **Target**: Synthetic `Risk` label created using domain rules
- **Features**: Age, Job type, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose

---

## ⚙️ Tech Stack

| Component         | Tool/Library                |
|------------------|-----------------------------|
| Language         | Python                      |
| Data Handling    | Pandas, Numpy               |
| Modeling         | Scikit-learn, GridSearchCV  |
| Feature Encoding | WoE Binning, IV             |
| Explainability   | SHAP (planned)              |
| Visualization    | Matplotlib, Seaborn         |
| Dashboard (Planned) | Streamlit                |
| Deployment (Planned) | Docker                  |
| Version Control  | Git, GitHub                 |

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/credit-risk-xai.git
cd credit-risk-xai

# (Optional) Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Or . .venv/bin/activate on Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run training
python src/train.py

# Run tuning + evaluation
python src/tune_model.py
```

---

## 📁 Project Structure

```
credit-risk-xai/
├── data/                   # Raw + processed data
│   ├── raw/
│   └── processed/
├── notebooks/              # EDA and analysis notebooks
├── src/                    # Source code: preprocessing, training, tuning
│   ├── data_prep.py
│   ├── train.py
│   └── tune_model.py
├── models/                 # Saved models and evaluation visuals (ROC, CM)
├── app/                    # Streamlit app files (planned)
├── docker/                 # Dockerfile and container setup (planned)
├── logs/                  # Daily learning + dev logs
│   └── daily_notes/
│       ├── 9th_June.md
│       ├── 10th_June.md
│       ├── 12th_June.md
│       └── 13th_June.md
├── README.md               # Project overview and documentation
├── requirements.txt        # Python dependencies
└── .gitignore              # Files/folders ignored by Git

```

| Path                           | Description                                               |
|--------------------------------|-----------------------------------------------------------|
| `data/raw/`                    | Original downloaded dataset (`german_credit_data.csv`)   |
| `data/processed/`              | Cleaned + labeled dataset (`credit_data_with_risk.csv`)  |
| `models/`                      | Saved models (`.pkl`) and evaluation plots (`.png`)       |
| `logs/daily_notes/`            | Daily progress logs (`9th_June.md` to `13th_June.md`)     |
| `notebooks/`                   | EDA, feature engineering, model training + tuning         |
| `src/data_prep.py`             | WoE + IV functions for categorical encoding               |
| `src/train.py`                 | Script to train baseline models                           |
| `src/tune_model.py`            | GridSearchCV + evaluation script (AUC, CM, ROC)           |
| `app/` *(planned)*             | Placeholder for Streamlit or FastAPI app                  |
| `docker/` *(planned)*          | Placeholder for Docker deployment setup                   |
| `.gitignore`                   | Git exclusions (data, logs, environment)                  |
| `README.md`                    | 📄 This file                                              |
| `requirements.txt`             | 🧪 All dependencies (`pip install -r`)                   |

---

## 🧪 Model Evaluation

- ✅ Logistic Regression (Baseline + Tuned)
- ✅ Decision Tree (Baseline)
- 🔄 ROC Curve & Confusion Matrix visualized
- 🔄 AUC used as primary metric for model selection

Evaluation plots saved in:
```
models/confusion_matrix_logreg.png
models/roc_curve_logreg.png
```

---

## 🗓️ Project Timeline

| Day         | Highlights |
|-------------|------------|
| Day 01 (9th June)  | Folder setup, dataset loaded, EDA done, risk label created |
| Day 02 (10th June) | WoE + IV implemented and visualized |
| Day 03 (12th June) | Baseline models trained and saved |
| Day 04 (13th June) | Hyperparameter tuning + evaluation plots generated |

---

## 👥 Author

**Yasaswin Palukuri**  
📍 Data Science & AI Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/yasaswin-palukuri)

---

## 📌 License

MIT License. Free to use, modify, and deploy.

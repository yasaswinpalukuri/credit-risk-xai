
# 🧠 Credit Risk Scoring with Explainable AI (XAI)

A machine learning pipeline to assess customer creditworthiness using real-world German credit data. This project simulates a banking-grade credit scoring model with explainable outputs using SHAP, Weight of Evidence (WoE), Streamlit UI, and Dockerized deployment.

---

## 📌 Problem Statement

Financial institutions need to assess whether a customer is likely to default on a loan. This project aims to:
- Build a credit risk prediction model using customer financial and demographic data.
- Apply interpretable ML techniques to help risk analysts and compliance teams understand model decisions.

---

## ⚙️ Tech Stack

| Component         | Tool/Library                |
|------------------|-----------------------------|
| Language         | Python                      |
| Data Handling    | Pandas, Numpy               |
| Modeling         | Scikit-learn, GridSearchCV  |
| Feature Encoding | WoE Binning, IV             |
| Explainability   | SHAP                        |
| Visualization    | Matplotlib, Seaborn         |
| Dashboard        | Streamlit                   |
| Deployment       | Docker                      |
| Version Control  | Git, GitHub                 |

---

## 🚀 How to Run

### 💻 Local (Python)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/credit-risk-xai.git
cd credit-risk-xai

# (Optional) Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Or . .venv/bin/activate on Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run training and tuning
python src/train.py
python src/tune_model.py

# Run Streamlit UI
streamlit run app/credit_scoring_app.py
```

---

### 🐳 Run with Docker

```bash
# From root folder
docker build -t credit-risk-app .
docker run -p 8501:8501 credit-risk-app
```

Visit 👉 http://localhost:8501 to access the app.

---

## 📁 Project Structure

```
credit-risk-xai/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── data_prep.py
│   ├── train.py
│   └── tune_model.py
├── models/
├── app/
│   └── credit_scoring_app.py
├── docker/
│   └── Dockerfile
├── logs/
│   └── daily_notes/
├── requirements.txt
└── README.md
```

---

## 🧪 Model Evaluation

- ✅ Logistic Regression (Baseline + Tuned)
- ✅ Decision Tree (Baseline + Tuned)
- ✅ SHAP Waterfall and Beeswarm explainability
- ✅ ROC Curve & Confusion Matrix
- ✅ Streamlit interactive predictions

Evaluation plots saved in `/models/`:
- `confusion_matrix_logreg.png`
- `roc_curve_logreg.png`
- `shap_beeswarm_logreg.png`
- `shap_waterfall_logreg_sample0.png`
- `shap_beeswarm_tree.png`
- `shap_waterfall_tree_sample0.png`

---

## 🗓️ Project Timeline

| Day         | Highlights |
|-------------|------------|
| Day 01 (9th June)   | Folder setup, dataset loaded, EDA, risk labeling |
| Day 02 (10th June)  | WoE + IV calculated and visualized |
| Day 03 (12th June)  | Baseline models trained + saved |
| Day 04 (13th June)  | Hyperparameter tuning, AUC, ROC, CM evaluation |
| Day 05 (13th June)  | Tuned Decision Tree, model comparison added |
| Day 06 (15th June)  | SHAP Explainability implemented |
| Day 07 (18th June)  | Streamlit UI built + Dockerized for deployment |

---

## 👥 Author

**Yasaswin Palukuri**  
📍 Data Science & AI Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/yasaswin-palukuri)

---

## 📌 License

MIT License. Free to use, modify, and deploy.

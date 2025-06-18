
# 📅 Day 07 – 2025-06-18

## ✅ Tasks Done
- Created and styled Streamlit UI for Credit Risk Scoring App
- Added input widgets: dropdowns for accounts, sliders for age & duration
- Connected model backend with real-time predictions
- Customized UI with headings, emojis, color scheme
- Dockerized app for local deployment

## 🧩 Streamlit App Summary

| Component      | Description                                 |
|----------------|---------------------------------------------|
| Input Panel    | Categorical (selectbox) + Numeric inputs    |
| Model Output   | Binary Risk (Good/Bad) + Probabilities      |
| SHAP Output    | Waterfall plot for single instance          |

---

## 🐳 Docker Setup

- Wrote `docker/Dockerfile` to package the app
- Encountered issues with `COPY` context not finding `data/`, `models/`, etc.
- **Fix**: Ran the build from project root using `-f` flag:

```bash
docker build -f docker/Dockerfile -t credit-risk-app .
docker run -p 8501:8501 credit-risk-app
```

- App confirmed to run at `http://localhost:8501`

---

## ❗Challenges

| Issue                        | Resolution                                                   |
|-----------------------------|--------------------------------------------------------------|
| COPY path errors            | Used project root as build context with `-f` flag            |
| Streamlit not loading       | Tried to access 0.0.0.0 instead of `localhost:8501`          |
| Dockerfile not found error  | Entered correct directory and confirmed file presence        |
| Folder nesting issues       | Adjusted working directory and Docker context appropriately |

---

## 📘 Concepts Learned

- Streamlit layout and input handling
- Docker build context, filesystem binding
- Streamlit host binding (`0.0.0.0` vs `localhost`)
- Debugging container build + run processes

---

## 📁 Files Created

| File                            | Purpose                        |
|----------------------------------|--------------------------------|
| `app/credit_scoring_app.py`     | Streamlit UI logic             |
| `requirements.txt`              | Dependency list for Docker     |
| `docker/Dockerfile`             | Docker container build file    |

---

## 🧾 Git Commit Commands

```bash
git add app/ docker/Dockerfile requirements.txt logs/daily_notes/18th_June.md
git commit -m "Day 07: Streamlit UI + Docker setup complete"
git push
```

---

## 🚀 What’s Next (Day 08)

- Add SHAP global beeswarm plots to UI
- Streamlit layout polishing and responsiveness
- Deploy to cloud (Render / Hugging Face / EC2 optional)

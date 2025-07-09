# 🎬 MovieIQ - Predictive Analytics on Film Success

An interactive Streamlit dashboard that analyzes and predicts the success of movies using key performance indicators such as budget, revenue, popularity, runtime, and average votes. Built with Python, this project leverages data visualization, statistical testing, and machine learning (Random Forest) for movie performance insights.

---

## 🌐 Live Demo

🚀 [Click here to try the live app](https://movieiq-predictive-analytics-on-film-success-hkz386d9xzv5mygjz.streamlit.app/)

---

## 📊 Key Features

- 🎯 Predicts whether a movie is likely to be successful (Revenue > Budget)
- 📈 Visual insights with Seaborn + Matplotlib (Budget vs Revenue, Genre Trends)
- 📊 T-Test and Chi-Square statistical tests
- 🤖 Random Forest Classifier for binary success prediction
- 🧠 Interactive filtering by genre and vote average via Streamlit sidebar
- 📂 Clean modular dashboard ready for deployment and GitHub showcasing

---

## 🧰 Tech Stack

- Python 🐍
- Pandas, NumPy
- Seaborn & Matplotlib
- Scikit-learn (RandomForestClassifier)
- Streamlit (App Framework)
- SciPy (Statistical Analysis)

---

## 📷 Screenshots

> *(You can add images to an `assets/` folder and reference them here.)*

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nv2105/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run MovieIQ.py
📁 Dataset
Make sure the project includes a movies.csv file with the following columns:

Copy
Edit
budget, revenue, popularity, runtime, vote_average, title, genres
👨‍💻 Author
Naman Vora
Final Year CSE Student | Aspiring Data Analyst
📫 LinkedIn • GitHub

📄 License
This project is open source and available under the MIT License.

yaml
Copy
Edit

---

### ✅ Final Step

Run the following in your terminal to push the updated README:

```bash
git add README.md
git commit -m "📄 Update README with live Streamlit app link"
git push origin main

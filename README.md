# 🎬 MovieIQ - Predictive Analytics on Film Success

An interactive Streamlit dashboard that analyzes and predicts the success of movies using key performance indicators such as budget, revenue, popularity, runtime, and average votes. Built with Python, this project leverages data visualization, statistical testing, and machine learning (Random Forest) for movie performance insights.

---

## 🌐 Live Demo

🚀 [Click here to try the live app](https://movieiq-predictive-analytics-on-film-success-hkz386d9xzv5mygjz.streamlit.app/)

---

## 📊 Key Features

- 🎯 Predicts whether a movie is likely to be successful (Revenue > Budget)
- 📈 Visual insights using Seaborn & Matplotlib (Budget vs Revenue, Genre Trends)
- 📊 T-Test and Chi-Square statistical tests
- 🤖 Random Forest Classifier for success prediction
- 🧠 Interactive filtering by genre and vote average via sidebar
- 🧼 Clean, modular dashboard ready for deployment

---

## 🧰 Tech Stack

- **Python** 🐍
- **Pandas**, **NumPy**
- **Seaborn**, **Matplotlib**
- **Scikit-learn**
- **Streamlit**
- **SciPy**

---

## 📷 Screenshots

| Dashboard Overview | Statistical Tests |
|--------------------|-------------------|
| ![Dashboard](assets/dashboard.png) | ![Tests](assets/stats_tests.png) |

> Add more screenshots to the `assets/` folder and reference them similarly.

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/nv2105/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success
 
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
```bash
streamlit run MovieIQ.py
```
## 📁 Dataset
Make sure the project includes a `movies.csv` file with the following columns:<br>
` budget, revenue, popularity, runtime, vote_average, title, genres`
<br>
## 👨‍💻 Author<br>
### Naman Vora<br>
#### Final Year CSE Student | Aspiring Data Analyst<br>
📫 [LinkedIn](www.linkedin.com/in/namanvora21) • [GitHub](https://github.com/nv2105)

## 📄 License
This project is open source and available under the [MIT License.](https://mit-license.org/) 

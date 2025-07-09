import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind, chi2_contingency
import ast

# --- Page Config ---
st.set_page_config(page_title="🎬 MovieIQ Dashboard", layout="wide")

# --- Sidebar About Section ---
with st.sidebar.expander("ℹ️ About this app", expanded=True):
    st.markdown("""
    **MovieIQ** uses machine learning to predict whether a movie will be *successful* based on:
    - Budget
    - Popularity
    - Runtime
    - Average Votes

    📈 Includes EDA, Stats, and Prediction
    """)

# --- App Title ---
st.title("🎬 MovieIQ - Movie Success Prediction Dashboard")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload your movies CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # --- Preprocessing ---
    df = df[["budget", "revenue", "popularity", "runtime", "vote_average", "title", "genres"]]
    df = df[df["budget"] > 0]
    df = df[df["revenue"] > 0]
    df.dropna(inplace=True)
    df["success"] = (df["revenue"] > df["budget"]).astype(int)
    df["main_genre"] = df["genres"].apply(lambda x: ast.literal_eval(x)[0]['name'] if x != '[]' else "Unknown")

    # --- Top-Level KPIs ---
    col1, col2, col3 = st.columns(3)
    col1.metric("🎞️ Total Movies", len(df))
    col2.metric("✅ Success %", f"{df['success'].mean()*100:.1f}%")
    col3.metric("🎬 Unique Genres", df['main_genre'].nunique())

    # --- Sidebar Filters ---
    st.sidebar.header("🔍 Filter Options")
    selected_genres = st.sidebar.multiselect("Select Genre(s)", options=df["main_genre"].unique(), default=df["main_genre"].unique())
    min_votes = st.sidebar.slider("Minimum Vote Average", 0.0, 10.0, 5.0)

    # --- Apply Filters ---
    filtered_df = df[(df["main_genre"].isin(selected_genres)) & (df["vote_average"] >= min_votes)]

    st.subheader("🎯 Dataset Overview")
    st.write(filtered_df.head())

    # --- Descriptive Statistics ---
    st.subheader("📊 Descriptive Statistics")
    st.write(filtered_df.describe())

    # --- Budget vs Revenue Plot ---
    st.subheader("💸 Budget vs Revenue")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(data=filtered_df, x="budget", y="revenue", hue="success", palette="coolwarm", ax=ax1)
    ax1.set_title("Budget vs Revenue (Success Highlighted)")
    st.pyplot(fig1)

    # --- Average Metrics by Success ---
    st.subheader("📈 Average Metrics by Success")
    avg_metrics = filtered_df.groupby("success")[["budget", "revenue", "popularity", "runtime", "vote_average"]].mean().reset_index()
    avg_metrics = pd.melt(avg_metrics, id_vars="success", var_name="Metric", value_name="Average Value")

    fig2, ax2 = plt.subplots()
    sns.barplot(data=avg_metrics, x="Metric", y="Average Value", hue="success", palette="Set2", ax=ax2)
    plt.setp(ax2.get_xticklabels(), rotation=45)
    st.pyplot(fig2)

    # --- Statistical Tests ---
    st.subheader("🧐 Statistical Tests")

    t_stat, p_val = ttest_ind(filtered_df[filtered_df["success"] == 1]["vote_average"],
                              filtered_df[filtered_df["success"] == 0]["vote_average"])
    st.markdown(f"**T-Test (Vote Average by Success):** t-stat = {t_stat:.2f}, p = {p_val:.4f}")

    contingency = pd.crosstab(filtered_df["main_genre"], filtered_df["success"])
    chi2, p, dof, expected = chi2_contingency(contingency)
    st.markdown(f"**Chi-Square (Genre vs Success):** chi2 = {chi2:.2f}, p = {p:.4f}")

    # --- ML Model ---
    st.subheader("🤖 Machine Learning: Success Prediction")

    features = filtered_df[["budget", "popularity", "runtime", "vote_average"]]
    target = filtered_df["success"]

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = model.score(X_test, y_test)
    st.markdown(f"**Model Accuracy:** {accuracy:.2%}")

    st.markdown("**Classification Report**")
    st.text(classification_report(y_test, y_pred))

    conf_matrix = confusion_matrix(y_test, y_pred)
    fig3, ax3 = plt.subplots()
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues", ax=ax3)
    ax3.set_title("Confusion Matrix")
    st.pyplot(fig3)

    # --- Prediction Section ---
    st.subheader("🎬 Predict Movie Success")

    with st.form("prediction_form"):
        st.markdown("📥 **Enter movie features to predict success:**")

        input_budget = st.number_input("Budget (USD)", min_value=1000, max_value=500000000, value=10000000, step=1000000)
        input_popularity = st.slider("Popularity", 0.0, 100.0, 10.0)
        input_runtime = st.slider("Runtime (minutes)", 30, 300, 120)
        input_vote_average = st.slider("Vote Average", 0.0, 10.0, 6.5)

        submit = st.form_submit_button("Predict")

    if submit:
        input_data = pd.DataFrame({
            "budget": [input_budget],
            "popularity": [input_popularity],
            "runtime": [input_runtime],
            "vote_average": [input_vote_average]
        })

        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0][prediction]

        if prediction == 1:
            st.success(f"🌟 **Success!** Predicted as a successful movie with {prediction_proba:.2%} confidence.")
        else:
            st.error(f"🚨 **Unsuccessful.** Predicted as an unsuccessful movie with {prediction_proba:.2%} confidence.")

    # --- Download Filtered Data ---
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Filtered Data", data=csv, file_name="filtered_movies.csv", mime="text/csv")

else:
    st.info("👇 Upload a CSV file to get started.")
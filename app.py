!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np

def load_data(file_path):
    #Load the dataset from a CSV file
    return pd.read_csv(file_path)

def simulate_recommendations(df, user_preferences, num_recommendations=5):
    #Simulate recommendations based on user preferences.
    filtered_df = df[df['taste'].isin(user_preferences.get('taste', df['taste'].unique()))]
    recommendations = filtered_df.sample(n=min(num_recommendations, len(filtered_df)), random_state=42)
    return recommendations

def main():
    st.title("Food Recommendation Simulation")
    file_path = "/content/recommendation_model_updated_v4.csv"
    df = load_data(file_path)

    st.sidebar.header("User Preferences")
    unique_tastes = df['taste'].unique()
    selected_tastes = st.sidebar.multiselect("Select preferred tastes", unique_tastes, default=unique_tastes[:2])

    if st.sidebar.button("Get Recommendations"):
        user_preferences = {"taste": selected_tastes}
        recommendations = simulate_recommendations(df, user_preferences)
        st.write("### Recommended Items:")
        st.dataframe(recommendations)

if __name__ == "__main__":
    main()

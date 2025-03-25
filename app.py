
import streamlit as st
import pandas as pd
import numpy as np

def load_data(file_path):
    #Load the dataset from a CSV file.
    return pd.read_csv(file_path)

def simulate_recommendations(df, user_preferences, num_recommendations=5):
    #Simulate recommendations based on user preferences.
    filtered_df = df.copy()

    if user_preferences.get('taste'):
        filtered_df = filtered_df[filtered_df['taste'].isin(user_preferences['taste'])]

    if user_preferences.get('user_cuisine'):
        filtered_df = filtered_df[filtered_df['user_cuisine'].isin(user_preferences['user_cuisine'])]

    if user_preferences.get('user_age'):
        filtered_df = filtered_df[filtered_df['user_age'].isin(user_preferences['user_age'])]

    if user_preferences.get('sex'):
        filtered_df = filtered_df[filtered_df['sex'].isin(user_preferences['sex'])]

    
    recommendations = filtered_df.sample(n=min(num_recommendations, len(filtered_df)), random_state=42)
    return recommendations

def main():
    st.title("Food Recommendation Simulation")
    file_path = "recommendation_model_updated_v4.csv"  # Replace with your file path
    df = load_data(file_path)

    st.sidebar.header("User Preferences")

    # Taste selection
    unique_tastes = df['taste'].unique()
    selected_tastes = st.sidebar.multiselect("Select preferred tastes", unique_tastes, default=unique_tastes[:2])

    # Cuisine selection
    unique_cuisines = df['user_cuisine'].unique()
    selected_cuisines = st.sidebar.multiselect("Select preferred cuisines", unique_cuisines, default=unique_cuisines[:2])

    # Age selection
    unique_age = df['user_age'].unique()
    selected_age = st.sidebar.multiselect("Select age", unique_age, default= unique_age[0:1])

    # Gender selection
    unique_sex = df['sex'].unique()
    selected_gender = st.sidebar.multiselect("Select gender", unique_sex, default=unique_sex[0:1])

  
    if st.sidebar.button("Get Recommendations"):
        user_preferences = {
            "taste": selected_tastes,
            "user_cuisine": selected_cuisines,
            "user_age": selected_age,
            "sex": selected_gender,
        }
        recommendations = simulate_recommendations(df, user_preferences)
        st.write("### Recommended Items:")
        st.dataframe(recommendations)

if __name__ == "__main__":
    main()

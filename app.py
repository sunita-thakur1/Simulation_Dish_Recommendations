
import streamlit as st
import pandas as pd
import numpy as np

def load_data(file_path):
    #Load the dataset from a CSV file.
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
    
    st.sidebar.header("User Taste")
    unique_tastes = df['taste'].unique()
    selected_tastes = st.sidebar.multiselect("Select preferred tastes", unique_tastes, default=unique_tastes[:2])

    st.sidebar.header("User Preferred cuisine")
    unique_cuisine = df['user_cuisine'].unique()
    selected_cuisine = st.sidebar.multiselect("Select preferred cuisine", unique_cuisine, default=unique_tastes[:2])

    st.sidebar.header("User age")
    unique_age = df['user_age'].unique()
    selected_age = st.sidebar.multiselect("Select age", unique_age, default=unique_tastes[:1])

    st.sidebar.header("User Gender")
    unique_gender = df['sex'].unique()
    selected_gender = st.sidebar.multiselect("Select gender", unique_gender, default=unique_tastes[:1])


    
    if st.sidebar.button("Get Recommendations"):
        user_preferences = {"taste": selected_tastes, "user_cuisine":selected_cuisine, "user_age":selected_age, "sex": selected_gender  }
        recommendations = simulate_recommendations(df, user_preferences)
        st.write("### Recommended Items:")
        st.dataframe(recommendations)
    
if __name__ == "__main__":
    main()

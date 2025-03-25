
import streamlit as st
import pandas as pd
import numpy as np

def load_data(file_path):
    #Load the dataset from a CSV file.
    return pd.read_csv(file_path)

def simulate_recommendations(df, user_preferences, num_recommendations=5):
    #Simulate recommendations based on user preferences.
    filtered_df1 = df[df['taste'].isin(user_preferences.get('taste', df['taste'].unique()))]
    filtered_df2 = df[df['user_cuisine'].isin(user_preferences.get('user_cuisine', df['user_cuisine'].unique()))]
    filtered_df3 = df[df['user_age'].isin(user_preferences.get('user_age', df['user_age'].unique()))]
    filtered_df4 = df[df['sex'].isin(user_preferences.get('sex', df['sex'].unique()))]
    recommendations1 = filtered_df1.sample(n=min(num_recommendations, len(filtered_df1)), random_state=42)
    recommendations2 = filtered_df2.sample(n=min(num_recommendations, len(filtered_df2)), random_state=42)
    recommendations3 = filtered_df3.sample(n=min(num_recommendations, len(filtered_df3)), random_state=42)
    recommendations4 = filtered_df4.sample(n=min(num_recommendations, len(filtered_df4)), random_state=42)
    
    return recommendations1, recommendations2, recommendations3, recommendations4

def main():
    st.title("Food Recommendation Simulation")
    # Change this google colab file path: copy and paste path of uploaded data csv file on Github: recommendation_model_updated_v4.csv[this is github oploaded file path]
    file_path = "recommendation_model_updated_v4.csv"
    df = load_data(file_path)
    
    st.sidebar.header("User Taste")
    unique_tastes = df['taste'].unique()
    selected_tastes = st.sidebar.multiselect("Select preferred tastes", unique_tastes, default=unique_tastes[:2])

    st.sidebar.header("User Preferred cuisine")
    unique_cuisine = df['user_cuisine'].unique()
    selected_cuisine = st.sidebar.multiselect("Select preferred cuisine", unique_cuisine, default=unique_cuisine[:2])

    st.sidebar.header("User age")
    unique_age = df['user_age'].unique()
    selected_age = st.sidebar.multiselect("Select age", unique_age, default=unique_age[:1])

    st.sidebar.header("User Gender")
    unique_gender = df['sex'].unique()
    selected_gender = st.sidebar.multiselect("Select gender", unique_gender, default=unique_gender[:1])


    
    if st.sidebar.button("Get Recommendations"):
        user_preferences = {"taste": selected_tastes, "user_cuisine":selected_cuisine, "user_age":selected_age, "sex": selected_gender  }
        recommendations = simulate_recommendations(df, user_preferences)
        st.write("### Recommended Items:")
        st.dataframe(recommendations)
    
if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd

# Load the CSV data into a Pandas DataFrame
@st.cache
def load_data():
    df = pd.read_csv("roll_numbers_total.csv")  # Replace "your_data.csv" with your CSV file path
    return df

# Function to find rank for a given roll number
def find_rank(roll_number, df):
    try:
        rank = df[df['Roll Number'] == roll_number].index[0] + 1  # Add 1 to get the actual rank
        return rank
    except IndexError:
        return "Roll number not found"

def main():
    st.title("Roll Number Rank Finder")

    # Load data
    @st.cache_data(persist=True)
    def load_data_cache():
        return load_data()

    data_load_state = st.text("Loading data...")
    df = load_data_cache()
    data_load_state.text("Data loaded successfully!")

    # User input
    roll_number = st.text_input("Enter Roll Number:")
    if roll_number:
        if st.button("Find Rank"):
            # Find rank
            rank = find_rank(int(roll_number), df)
            st.write(f"The rank of roll number {roll_number} is: {rank}")

if __name__ == "__main__":
    main()

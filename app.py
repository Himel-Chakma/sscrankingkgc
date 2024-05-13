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
        # Sort the DataFrame by 'Total Number' column in descending order
        sorted_df = df.sort_values(by='Total Number', ascending=False)
        
        # Find the index of the roll number in the sorted DataFrame
        rank = sorted_df[sorted_df['Roll Number'] == roll_number].index[0] + 1  # Add 1 to get the actual rank
        return rank
    except IndexError:
        return "Roll number not found"

def main():
    st.title("SSC-2024 Khagrachari Science Rank Finder")

    # Load data
    def load_data_cache():
        return load_data()
    
    df = load_data_cache()

    # User input
    roll_number = st.text_input("Enter Roll Number:")
    if roll_number:
        if st.button("Find Rank"):
            # Find rank
            rank = find_rank(int(roll_number), df)
            st.write(f"The rank of roll number {roll_number} is: {rank}")

if __name__ == "__main__":
    main()

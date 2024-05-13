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
        # Assign ranks based on the 'Total Number' column
        df['Rank'] = df['Total Number'].rank(ascending=False, method='min')
        
        # Find the rank of the roll number
        rank = int(df[df['Roll Number'] == roll_number]['Rank'])
        return rank
    except KeyError:
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

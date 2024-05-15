import streamlit as st
import pandas as pd

# Load the CSV data into a Pandas DataFrame
@st.cache_data(persist=True)
def load_data(option):
    if option == "Science":
        df = pd.read_csv("roll_numbers_total.csv")
    elif option == "Humanities":
        df = pd.read_csv("roll_numbers_total-hum1.csv")
    elif option == "Business Studies":
        df = pd.read_csv("roll_numbers_total-com.csv")
    return df

# Function to find rank for a given roll number
def find_rank(roll_number, df):
    # Assign ranks based on the 'Total Number' column
    df['Rank'] = df['Total Number'].rank(ascending=False, method='min')
        
        # Check if the roll number exists in the DataFrame
    if roll_number in df['Roll Number'].values:
        # Find the rank of the roll number
        rank = int(df[df['Roll Number'] == roll_number]['Rank'])
        return rank
    else:
        return None

def main():

    st.title("SSC-2024 Rank Finder Khagrachari")

    # Select box for group selection
    option = st.selectbox("Select Group:", ["Science", "Humanities", "Business Studies"])

    # Load data based on the selected group
    df = load_data(option)

    # User input
    roll_number = st.text_input("Enter Roll Number:")
    if roll_number:
        if st.button("Find Rank"):
            try:
                # Convert roll number to integer
                roll_number_int = int(roll_number)
                # Find rank
                rank = find_rank(roll_number_int, df)
                if rank is not None:
                    st.success(f"The rank of roll number {roll_number} in {option} group is: {rank}")
                else:
                    st.error(f"Roll number {roll_number} not found in {option} group.")
            except ValueError:
                st.error("Please enter a valid roll number.")
    
    st.markdown(
        """
        ### Data Summary
        - **Science**: 1458
        - **Humanities**: 3383
        - **Business Studies**: 1615
        - **The 2nd timers are not considered**
        """
    )

if __name__ == "__main__":
    main()


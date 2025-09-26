
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data():
    # Replace this with your COVID-19 dataset file
    data = pd.read_csv("clean_data.csv")
    return data

df = load_data()

# -------------------------
# Layout - Title and Description
# -------------------------
st.title("COVID-19 Publication Dashboard 🦠")
st.markdown("""
This dashboard provides an overview of COVID-19 data.  
You can interact with the charts using filters below.
""")


# Show Sample of Data

st.subheader("Sample of the Dataset")
st.write(df.head())


# Interactive Widgets

st.sidebar.header("Filters")

# Dropdown for publication year
pub_year = df["publication_year"].unique()
selected_pub_year = st.sidebar.selectbox("Select year", pub_year)

# Slider for date range
if "Date" in df.columns:
    
    min_date = df["publication_date"].min()
    max_date = df["publication_date"].max()
    date_range = st.sidebar.slider("Select Date Range", min_date, max_date, (min_date, max_date))
    filtered_df = df[(df["publication_year"] == selected_pub_year) &
                     (df["publication_date"] >= date_range[0]) & (df["publication_date"] <= date_range[1])]
else:
    filtered_df = df[df["Country"] == selected_pub_year]

# -------------------------
# Visualization
# -------------------------
st.subheader(f"COVID-19 Trends in {selected_pub_year}")

if "Date" in filtered_df.columns:
    fig, ax = plt.subplots(figsize=(10, 5))
    top_5_publication_year = df['publication_year'].value_counts().head()
    top_5_publication_year_sorted=top_5_publication_year.sort_values(ascending=True)
    # Plot number of publications over time
    plt.figure(figsize=(8,6))
    top_5_publication_year_sorted.plot(kind='bar')
    plt.title('Number of publication per year')
    st.pyplot(fig)
else:
    st.warning("No publication Date column found in dataset to plot trends.")

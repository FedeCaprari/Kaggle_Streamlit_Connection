from connection import KaggleDatasetConnection
import streamlit as st

st.set_page_config(page_title="Kaggle-Streamlit Connection Demo App")
st.title("Kaggle-Streamlit Connector App")
st.info(
    "This is a demo app that presents basic use of custom Kaggle-Streamlit connector built using ExperimentalBaseConnection"
)
st.subheader("Loading dataset from Kaggle Through API")
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
# dataset_path = st.text_input(
#     "Kaggle Link Of Dataset", "varsharam/walmart-sales-dataset-of-45stores"
# )
# dataset_name = st.text_input(
#     "Kaggle Dataset Name", "walmart-sales-dataset-of-45stores.csv"
# )
dataset_path = st.text_input(
    "Kaggle Link Of Dataset", "rmisra/news-headlines-dataset-for-sarcasm-detection"
)
dataset_name = st.text_input(
    "Kaggle Dataset Name", "Sarcasm_Headlines_Dataset.json"
)
if st.button("Load Data"):
    try:
        df = conn.get(path=dataset_path, filename=dataset_name, ttl=3600)
        st.write("Data Preview:")
        st.dataframe(df.head(20))
    except Exception as e:
        st.error(f"Oops...{e.args}")

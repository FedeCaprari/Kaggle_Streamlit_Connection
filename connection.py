from streamlit.connections import ExperimentalBaseConnection
import os
import pandas as pd
import zipfile
import streamlit as st
class KaggleDatasetConnection(ExperimentalBaseConnection):
    def _connect(self):
        # Set Kaggle credentials
        os.environ['KAGGLE_USERNAME'] = self._secrets.KAGGLE_USERNAME
        os.environ['KAGGLE_KEY'] = self._secrets.KAGGLE_KEY
        from kaggle.api.kaggle_api_extended import KaggleApi
        self.conn = KaggleApi()
    def get(self, path, filename, ttl):
        @st.cache_data(ttl=ttl)
        def _get(path=path):
            self.conn.authenticate()
            self.conn.dataset_download_files(path)
            file_name = path.split('/')[-1] + ".zip"
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall('.')
            df = pd.DataFrame() 
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
            elif filename.endswith(".json"):
                df = pd.read_json(filename)
            return df
        return _get(path)

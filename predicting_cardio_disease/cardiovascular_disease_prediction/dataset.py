import os
import requests
import zipfile
from cardiovascular_disease_prediction.config import DATASET_LINK, DATASET_DIR, DATASET_ZIPFILE_NAME, DATASET_NAME

def download_file():
    '''
    Download the dataset from the Kaggle link and save it to the specified directory.
    '''
    parent_dir = os.path.dirname(os.path.abspath(os.getcwd()))
    try:
        # Check if the directory exists, if not create it
        os.makedirs(os.path.join(parent_dir, DATASET_DIR), exist_ok=True)
    except Exception as e:
        print(f"Error creating directory: {e}")

    # Download the dataset
    try:
        response = requests.get(DATASET_LINK, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        zip_file_path = os.path.join(parent_dir, DATASET_DIR, DATASET_ZIPFILE_NAME)
        with open(zip_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Dataset downloaded successfully and saved to {zip_file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the dataset: {e}")
        return

def extract_zipfile():
    '''
    Extract the zip file to the specified directory.
    '''
    try:
        parent_dir = os.path.dirname(os.path.abspath(os.getcwd()))
        zip_file_path = os.path.join(parent_dir, DATASET_DIR, DATASET_ZIPFILE_NAME)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            print(f'ZipFile list - {zip_ref.namelist()}')
            zip_ref.extractall(os.path.dirname(zip_file_path))
        print(f"Dataset extracted successfully to {zip_file_path}")
    except zipfile.BadZipFile as e:
        print(f"Error extracting the dataset: {e} from {zip_file_path}")

def load_dataset():
    '''
    Load the dataset from the zip file and extract it to the specified directory.
    '''
    import pandas as pd

    parent_dir = os.path.dirname(os.path.abspath(os.getcwd()))
    dataset_file_path = os.path.join(parent_dir, DATASET_DIR, DATASET_NAME)
    print(f"Attempting to load dataset from: {dataset_file_path}")
    try:
        df = pd.read_csv(dataset_file_path, sep=';', header=0)
        print(f"Dataset loaded successfully from {dataset_file_path}")
        return df
    except FileNotFoundError as e:
        print(f"Error loading the dataset: {e} from {dataset_file_path}")
        return None


if __name__ == '__main__':
    # pipeline to download and extract the dataset
    download_file()
    extract_zipfile()
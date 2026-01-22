# 🌍 Climate Data Analysis: Savoie Temperature (CAMS)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Data](https://img.shields.io/badge/Data-Copernicus_CAMS-green)
![Library](https://img.shields.io/badge/Lib-Pandas%20%7C%20Xarray-orange)

This project analyzes the **2m Temperature** variations in the Savoie region (Chambéry area, France) for **July 2023**.
It utilizes the **CAMS Global Reanalysis (EAC4)** dataset retrieved via the Copernicus API, processes the NetCDF data, and generates visualizations (Time Series & Spatial Heatmap).

## 📂 Project Structure

The workflow is divided into three distinct steps:

* `step1_fetch_data.py`: Connects to the CDS API and downloads raw NetCDF data.
* `step2_process_data.py`: Converts NetCDF to CSV, handles unit conversion (Kelvin to Celsius), and cleans the dataset.
* `step3_visualize.py`: Generates a daily cycle graph and a spatial heatmap.
* `requirements.txt`: List of necessary Python libraries.

## 🛠️ Prerequisites

### 1. Copernicus API Key
You need a valid API key from the [Atmosphere Data Store (ADS)](https://ads.atmosphere.copernicus.eu/api-how-to).
* **Important:** Edit `step1_fetch_data.py` to insert your own `url` and `key` or configure your `.cdsapirc` file.

### 2. Installation
Install the required dependencies using pip:

```bash
pip install -r requirements.txt

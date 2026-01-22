import xarray as xr
import pandas as pd
import os
import sys

# --- CONFIGURATION ---
INPUT_FILE = "temperature.nc"
OUTPUT_FILE = "final_data_simple.csv"
KELVIN_OFFSET = 273.15  # Constant for unit conversion

def process_temperature_data(input_path: str, output_path: str) -> None:
    """
    Reads a NetCDF file, converts temperature to Celsius, and saves key metrics to CSV.

    Args:
        input_path (str): Path to the source .nc file.
        output_path (str): Destination path for the .csv file.
    """
    
    # 1. Validation check
    if not os.path.exists(input_path):
        print(f"❌ Error: The file '{input_path}' was not found.")
        sys.exit(1)

    print(f"📂 Processing file: {input_path}...")

    try:
        # 2. Load Dataset
        ds = xr.open_dataset(input_path)

        # 3. Unit Conversion (Kelvin -> Celsius)
        # We modify the dataset directly before converting to DataFrame for efficiency
        if 't2m' in ds.variables:
            ds['t2m'] = ds['t2m'] - KELVIN_OFFSET

        # 4. Conversion to DataFrame
        # reset_index() flattens the multi-index to make columns accessible
        df = ds.to_dataframe().reset_index()

        # 5. Cleaning and Renaming
        # Mapping generic CDS names to readable column headers
        column_mapping = {
            'valid_time': 'time', 
            't2m': 'Temperature_C'
        }
        df.rename(columns=column_mapping, inplace=True)

        # 6. Column Selection
        # Explicitly keeping geospatial coordinates as requested
        target_columns = ['time', 'latitude', 'longitude', 'Temperature_C']
        
        # Safe filtering: only keep columns that actually exist in the dataframe
        final_columns = [col for col in target_columns if col in df.columns]
        df_final = df[final_columns]

        # 7. Export
        df_final.to_csv(output_path, index=False)
        print(f"✅ Success: Data saved to '{output_path}'")
        print(f"📊 Columns included: {final_columns}")

    except Exception as e:
        print(f"❌ Processing Error: {e}")
        sys.exit(1)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    process_temperature_data(INPUT_FILE, OUTPUT_FILE)
import cdsapi
import os
from typing import List

# --- CONFIGURATION ---
# Note: In a production environment, use os.getenv("CDS_API_KEY") for security.
CDS_API_URL = "https://ads.atmosphere.copernicus.eu/api"
CDS_API_KEY = "INSERT YOUR KEY" 

def fetch_temperature_data(
    year: str, 
    month: str, 
    area: List[float], 
    output_filename: str
) -> None:
    """
    Retrieves 2m temperature monthly mean data from CAMS global reanalysis.

    Args:
        year (str): Target year (e.g., '2023').
        month (str): Target month (e.g., '07').
        area (List[float]): Bounding box [North, West, South, East].
        output_filename (str): Destination path for the NetCDF file.
    """
    print(f"🌡️  1/2: Initiating download for 2m Temperature ({year}-{month})...")

    try:
        # Initialize the CDS Client
        client = cdsapi.Client(url=CDS_API_URL, key=CDS_API_KEY)

        # Define the request payload
        request_params = {
            "variable": "2m_temperature",  # Single variable request
            "year": year,
            "month": month,
            "product_type": "monthly_mean_by_hour_of_day",
            "time": [f"{h:02d}:00" for h in range(24)],  # Generates 00:00 to 23:00
            "area": area,
            "format": "netcdf",
        }

        # Execute retrieval
        client.retrieve(
            "cams-global-reanalysis-eac4-monthly",
            request_params,
            output_filename
        )
        print(f"✅ Success: Data saved to '{output_filename}'")

    except Exception as e:
        print(f"❌ Error during download: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Region of Interest (Savoie / USMB Area)
    # Format: [North, West, South, East]
    ROI_SAVOIE = [46, 5.5, 45, 6.5]

    fetch_temperature_data(
        year="2023",
        month="07",
        area=ROI_SAVOIE,
        output_filename="temperature.nc"
    )
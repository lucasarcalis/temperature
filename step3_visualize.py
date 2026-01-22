import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# --- CONFIGURATION ---
INPUT_FILE = "final_data_simple.csv"
OUTPUT_GRAPH = "result_temperature_graph.png"
OUTPUT_MAP = "result_temperature_map.png"

def load_data(filepath):
    """
    Loads CSV data and converts the time column to datetime objects.
    """
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found.")
        sys.exit(1)
        
    df = pd.read_csv(filepath)
    df['time'] = pd.to_datetime(df['time'])
    return df

def plot_time_series(df):
    """
    Generates a line chart for the first 24 hours of data.
    """
    print("📈 Generating Time Series Graph...")
    
    # Subset: First 24 data points (assuming hourly data)
    subset = df.head(24)

    plt.figure(figsize=(10, 6))
    plt.plot(subset['time'], subset['Temperature_C'], 
             color='crimson', marker='o', label='Temperature (°C)')
    
    # Styling
    plt.title('Daily Cycle (July 2023)')
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Time')
    plt.grid(True, alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # Save
    plt.savefig(OUTPUT_GRAPH)
    print(f"✅ Time series saved to: {OUTPUT_GRAPH}")
    plt.close() # Close memory reference

def plot_spatial_heatmap(df):
    """
    Generates a spatial heatmap using a scatter plot grid.
    Aggregates temperature by Latitude/Longitude.
    """
    print("🗺️  Generating Spatial Heatmap...")
    
    plt.figure(figsize=(8, 6))

    # Calculate average temperature for each grid point (lat, lon)
    map_data = df.groupby(['latitude', 'longitude'])['Temperature_C'].mean().reset_index()

    # Create the scatter plot acting as a heatmap
    # 's=500' and 'marker=s' create large squares to simulate grid pixels
    sc = plt.scatter(
        map_data['longitude'], 
        map_data['latitude'], 
        c=map_data['Temperature_C'], 
        cmap='YlOrRd',  # Yellow to Red colormap
        s=500,          # Size of points
        marker='s',     # Square marker
        edgecolors='none'
    )

    # Styling
    cbar = plt.colorbar(sc)
    cbar.set_label('Average Temperature (°C)')
    plt.title('Mean Heatmap - Chambéry Area (July 2023)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save
    plt.tight_layout()
    plt.savefig(OUTPUT_MAP)
    print(f"✅ Heatmap saved to: {OUTPUT_MAP}")
    plt.close()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Load Data
    data = load_data(INPUT_FILE)
    
    # 2. Create Plots
    plot_time_series(data)
    plot_spatial_heatmap(data)
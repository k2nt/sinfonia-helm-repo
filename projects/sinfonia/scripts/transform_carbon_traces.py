import os
import pandas as pd
from datetime import datetime


CARBON_TRACES_FOLDER = 'carbon_traces'


# Get the list of CSV files in the carbon_traces folder
csv_files = [file for file in os.listdir(CARBON_TRACES_FOLDER) if file.endswith('.csv')]

# Iterate over each CSV file
for file in csv_files:
    print(file)
    
    # Read the CSV file
    df = pd.read_csv(os.path.join(CARBON_TRACES_FOLDER, file))
    
    # Convert the 'Datetime (UTC)' column to Unix timestamp
    if 'Datetime (UTC)' in df.columns:
        df['Datetime (UTC)'] = df['Datetime (UTC)'].apply(lambda x: int(datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timestamp()))
    
    # Rename the 'Datetime (UTC)' column to 'timestamp'
    df = df.rename(
        columns={
            'Datetime (UTC)': 'timestamp',
            'Country': 'country',
            'Zone Name': 'zone',
            'Zone Id': 'zone_id',
            'Carbon Intensity gCO₂eq/kWh (direct)': 'carbon_intensity_gco2_kwh_direct',
            'Carbon Intensity gCO₂eq/kWh (LCA)': 'carbon_intensity_gco2_kwh_lca',
            'Data Estimated': 'is_data_estimated',
            }
        )
    
    # Rewrite the file with the updated data
    df.to_csv(os.path.join(CARBON_TRACES_FOLDER, file), index=False)


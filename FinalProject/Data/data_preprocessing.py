'''
Author: Drew Mortenson, with ChatGPT's guidance (eda_chat.txt)
'''

import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, 'section_of_road')

station_metadata = {
    715898: {"Type": "Mainline", "Lat": 33.880183, "Lon": -118.021787},
    715901: {"Type": "On Ramp", "Lat": 33.8834, "Lon": -118.027451},
    762355: {"Type": "Off Ramp", "Lat": 33.8834, "Lon": -118.027451},
    716899: {"Type": "Mainline", "Lat": 33.8834, "Lon": -118.027451},
    716900: {"Type": "Mainline", "Lat": 33.886992, "Lon": -118.034125},
    715903: {"Type": "On Ramp", "Lat": 33.886992, "Lon": -118.034125},
    762353: {"Type": "Mainline", "Lat": 33.890697, "Lon": -118.041009},
    775012: {"Type": "Mainline", "Lat": 33.892607, "Lon": -118.044468},
    716904: {"Type": "Mainline", "Lat": 33.894587, "Lon": -118.048098},
    716903: {"Type": "Off Ramp", "Lat": 33.894587, "Lon": -118.048098},
    715905: {"Type": "On Ramp", "Lat": 33.894587, "Lon": -118.048098},
    718358: {"Type": "Mainline", "Lat": 33.896767, "Lon": -118.052213},
    769625: {"Type": "Mainline", "Lat": 33.900806, "Lon": -118.059282}, 
    769626: {"Type": "Off Ramp", "Lat": 33.900806, "Lon": -118.059282},
    762357: {"Type": "On Ramp", "Lat": 33.905186, "Lon": -118.065055}, # This is labelled as an Off Ramp on PeMS. It geographically cannot be an offramp.
    718081: {"Type": "Mainline", "Lat": 33.905186, "Lon": -118.065055},  
    718360: {"Type": "Mainline", "Lat": 33.907717, "Lon": -118.067667},
}

all_stations_data = []

for station_id, meta in station_metadata.items():
    # pick flow file name
    if meta['Type'] == 'Mainline':
        base = f"Mainline VDS {station_id} Flow & Occup"
    else:
        base = f'{meta["Type"]} VDS {station_id} Flow & Occup'
    
    # load all three weeks
    flow_occ_dfs = []
    for suffix in ['', '2', '3']:
        fn = f"{base}{suffix}.xlsx"
        path = os.path.join(data_folder, fn)
        if os.path.exists(path):
            df_part = pd.read_excel(path)
            flow_occ_dfs.append(df_part)
    flow_occ_df = pd.concat(flow_occ_dfs, ignore_index=True)
    
    # no speed/Q merge—just use flow_occ_df
    merged_df = flow_occ_df

    # add your metadata columns
    merged_df['Station_ID']   = station_id
    merged_df['Station_Type'] = meta['Type']
    merged_df['Latitude']     = meta['Lat']
    merged_df['Longitude']    = meta['Lon']

    all_stations_data.append(merged_df)

    all_stations_data.append(merged_df)

# Concatenate all station DataFrames into one big DataFrame
full_data = pd.concat(all_stations_data, ignore_index=True)

# Save master DataFrame
full_data.to_pickle('full_station_data.pkl')  # Fast loading
full_data.to_csv('full_station_data.csv', index=False)  # Human-readable backup

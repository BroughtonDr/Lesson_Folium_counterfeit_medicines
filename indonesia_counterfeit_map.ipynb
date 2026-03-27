# =============================================================
# Counterfeit & Illegal Medicines in Indonesia (2015–2026)
# Interactive Map using Folium
# =============================================================
# This notebook builds an interactive map of BPOM enforcement
# actions against counterfeit medicines in Indonesia.
#
# Based on: Kesmas: National Public Health Journal (2017).
# Counterfeit Medicines in Socioeconomic Perspective, 11(4), 153.
# https://doi.org/10.21109/kesmas.v11i4.1440
#
# Run each cell in order using Shift + Enter.
# =============================================================


# ── Cell 1 - install and import libraries ─────────────────────
# if folium is not installed yet, uncomment the line below and run it first
# !pip install folium

import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap, MarkerCluster
import warnings
warnings.filterwarnings('ignore')

print('pandas:', pd.__version__)
print('folium:', folium.__version__)
print('ready!')


# ── Cell 2 - load the dataset ─────────────────────────────────
df = pd.read_csv('../data/indonesia_counterfeit_medicines_2015_2026.csv')

# remove rows where coordinates are missing
df = df.dropna(subset=['latitude', 'longitude'])

# make sure lat/lng are numbers
df['latitude']  = pd.to_numeric(df['latitude'],  errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['year']      = pd.to_numeric(df['year'],       errors='coerce')

# FIX: convert case_id to numeric and drop rows where year or case_id is NaN
df['case_id'] = pd.to_numeric(df['case_id'], errors='coerce')
df = df.dropna(subset=['year', 'case_id'])
df['year']    = df['year'].astype(int)
df['case_id'] = df['case_id'].astype(int)

# fill empty text fields
text_cols = ['city', 'province', 'drug_category', 'brands_seized',
             'action_taken', 'channel', 'notes', 'source_url']
df[text_cols] = df[text_cols].fillna('-')

# FIX: count cases per city for weighting
cases_by_city = df.groupby('city').size().reset_index(name='num_cases')
df = df.merge(cases_by_city, on='city', how='left')
max_cases = df['num_cases'].max()

print(f'{len(df)} cases loaded')
df[['year', 'city', 'province', 'drug_category', 'channel']].head()


# ── Cell 3 - create the base map ──────────────────────────────
m = folium.Map(
    location=[-2.5, 118.0],
    zoom_start=5,
    tiles='CartoDB positron'
)

m


# ── Cell 4 - add markers ──────────────────────────────────────
# colour is based on drug category
# icon is based on whether it was sold online or physically

def get_colour(category):
    cat = str(category).lower()
    if 'vaccine' in cat:                            return 'red'
    elif 'erectile' in cat or 'slimming' in cat:   return 'purple'
    elif 'traditional' in cat or 'jamu' in cat:    return 'green'
    elif 'syrup' in cat:                            return 'orange'
    elif 'psychotropic' in cat or 'pcc' in cat:    return 'darkred'
    elif 'supplement' in cat:                       return 'cadetblue'
    elif 'stem cell' in cat or 'secretome' in cat: return 'pink'
    else:                                           return 'blue'

def get_icon(channel):
    return 'cloud' if 'online' in str(channel).lower() else 'home'

cluster = MarkerCluster(name='All cases').add_to(m)

for _, row in df.iterrows():
    try:
        val = f"Rp {int(float(row['estimated_value_idr'])):,}"
    except:
        val = 'not reported'

    popup_html = f"""
    <b>Case {row['case_id']} — {row['year']}</b><br>
    Location: {row['city']}, {row['province']}<br>
    Drug type: {row['drug_category']}<br>
    Channel: {row['channel']}<br>
    Value seized: {val}<br>
    Action: {row['action_taken']}<br>
    Cases in this city: {row['num_cases']}<br><br>
    <i>{str(row['notes'])[:120]}...</i><br>
    <a href="{row['source_url']}" target="_blank">Source</a>
    """

    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"{row['year']} | {row['city']} | {row['drug_category']}",
        icon=folium.Icon(
            color=get_colour(row['drug_category']),
            icon=get_icon(row['channel']),
            prefix='glyphicon'
        )
    ).add_to(cluster)

print(f'{len(df)} markers added')
m


# ── Cell 5 - add heatmap ──────────────────────────────────────
# FIX: weight by num_cases per city instead of messy estimated_value_idr

df['weight'] = df['num_cases'] / max_cases

heat_data = [[row['latitude'], row['longitude'], row['weight']]
             for _, row in df.iterrows()]

HeatMap(
    heat_data,
    name='Heatmap',
    radius=40,
    blur=25,
    max_zoom=8,
    gradient={'0.2': 'blue', '0.5': 'orange', '1.0': 'red'}
).add_to(m)

print('heatmap added')
m


# ── Cell 6 - separate layers for online vs physical cases ─────
online_layer   = folium.FeatureGroup(name='Online cases',   show=False)
physical_layer = folium.FeatureGroup(name='Physical raids', show=False)

for _, row in df.iterrows():
    channel = str(row['channel']).lower()
    colour  = '#e74c3c' if 'online' in channel else '#27ae60'
    # FIX: scale circle radius by num_cases
    radius  = 5 + (row['num_cases'] / max_cases) * 20

    circle = folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=radius,
        color=colour,
        fill=True,
        fill_color=colour,
        fill_opacity=0.7,
        tooltip=f"{row['year']} | {row['city']} | Cases: {row['num_cases']}"
    )

    if 'online' in channel:
        circle.add_to(online_layer)
    else:
        circle.add_to(physical_layer)

online_layer.add_to(m)
physical_layer.add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

print('layers added')
m


# ── Cell 7 - add legend and title ─────────────────────────────
legend_html = """
<div style="position:fixed; bottom:30px; left:30px; z-index:1000;
     background:white; padding:12px; border-radius:8px;
     border:1px solid #ccc; font-size:13px;">
  <b>Indonesia Counterfeit Medicines 2015–2026</b><br><br>
  <b>Marker colour:</b><br>
  🔴 Counterfeit vaccines<br>
  🟣 ED / slimming drugs<br>
  🟢 Illegal traditional medicines<br>
  🟠 Contaminated syrups<br>
  🩷 Stem cell / biologics<br>
  🔵 Multiple / online<br><br>
  <b>Icon:</b> ☁ Online &nbsp; ⌂ Physical<br><br>
  <b>Circle size:</b> number of cases in city<br><br>
  <i>Source: BPOM press releases 2015–2026</i>
</div>
"""

title_html = """
<div style="position:fixed; top:10px; left:50%; transform:translateX(-50%);
     z-index:1000; background:white; padding:8px 16px;
     border-radius:8px; border:1px solid #ccc; font-size:15px;">
  <b>Counterfeit & Illegal Medicines — Indonesia 2015–2026</b><br>
  <center>BPOM Enforcement Data</center>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))
m.get_root().html.add_child(folium.Element(title_html))

print('legend and title added')
m


# ── Cell 8 - save the final map ───────────────────────────────
import os
os.makedirs('../outputs', exist_ok=True)
m.save('../outputs/indonesia_counterfeit_map.html')
print('map saved to outputs/indonesia_counterfeit_map.html')
print('open that file in any browser to view the full interactive map')

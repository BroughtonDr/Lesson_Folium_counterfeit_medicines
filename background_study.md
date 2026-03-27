# 🗺️ Counterfeit & Illegal Medicines in Indonesia — Interactive Folium Map

## Description

This repository contains the Python code and dataset for an interactive 
geospatial map visualising counterfeit and illegal medicine enforcement 
actions in Indonesia between 2015 and 2026.

Paper found that counterfeit herbal medicines in Indonesia 
are increasing alongside the growing number of registered herbal drugs. 
Around 81% of falsified herbal drugs involved both adulteration and 
tampering. Lifestyle drugs accounted for 51% of cases and 
health-condition drugs 49%, with paracetamol being the most common 
substitute chemical drug added illegally.

This Folium map extends those findings by visualising **where** BPOM 
enforcement actions took place across Indonesia (2015–2026), showing 
the geographic spread of counterfeit medicines — from physical markets 
and illegal factories to online platforms such as Shopee, Tokopedia, 
and Lazada.

---

## What the Map Shows

- 📌 28 BPOM enforcement cases plotted as colour-coded markers
- 🔥 A heatmap showing raid density by province
- 🔀 Toggleable layers for online vs physical cases
- 💬 Clickable popups with full case details and source links

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Load and clean the CSV dataset |
| `folium` | Build the interactive HTML map |
| `folium.plugins.HeatMap` | Density heatmap layer |
| `folium.plugins.MarkerCluster` | Group overlapping markers |
| `numpy` | Log-scale heatmap weights |

---

## How to Run
# 1. Install libraries
pip install -r requirements.txt

# 2. Open Jupyter
jupyter notebook
```
# 3. code available in this github
---

## References

Kesmas: National Public Health Journal (2017). Counterfeit Medicines 
in Socioeconomic Perspective, 11(4), 153. 
https://doi.org/10.21109/kesmas.v11i4.1440

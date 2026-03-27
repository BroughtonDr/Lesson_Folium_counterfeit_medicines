# 🗺️ Counterfeit & Illegal Medicines in Indonesia — Interactive Folium Map

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Folium](https://img.shields.io/badge/Folium-0.15+-green)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Description

This repository contains the Python code and dataset for an interactive geospatial map visualising counterfeit and illegal medicine enforcement actions by **BPOM** (Badan Pengawas Obat dan Makanan — Indonesia's National Agency of Drug and Food Control) between **2015 and 2026**.

This project was developed as a practical data visualisation companion to:

> **Counterfeit Medicines in Socioeconomic Perspective**
> *Kesmas: National Public Health Journal*, Vol. 11(4):153, May 2017
> DOI: [10.21109/kesmas.v11i4.1440](https://doi.org/10.21109/kesmas.v11i4.1440)
> Licence: CC BY-SA 4.0

The paper examines counterfeit medicines from a socioeconomic angle — exploring why they are produced, who is affected, and what drives demand. This Folium map extends those findings by visualising **where** BPOM enforcement actions took place across Indonesia, showing the geographic spread of counterfeit medicines from physical markets and illegal factories to online platforms such as Shopee, Tokopedia, and Lazada.

---

## 🗂️ Repository Structure

```
Lesson_Folium/
│
├── README.md                                            ← You are here
├── requirements.txt                                     ← Libraries to install
├── LICENSE                                              ← MIT licence
│
├── data/
│   └── indonesia_counterfeit_medicines_2015_2026.csv   ← Dataset (28 cases)
│
├── notebooks/
│   └── indonesia_counterfeit_map.ipynb                 ← Main Jupyter notebook
│
└── outputs/
    └── indonesia_counterfeit_map.html                  ← Generated interactive map
```

---

## 🗺️ What the Map Shows

- 📌 **28 BPOM enforcement cases** plotted as colour-coded markers
- 🔥 A **heatmap** showing raid density across Indonesian provinces
- 🔀 **Toggleable layers** for online vs physical raid cases
- 💬 **Clickable popups** with full case details, drug type, value seized, and original BPOM source link

**Marker colours encode drug type:**

| Colour | Drug Category |
|--------|--------------|
| 🔴 Red | Counterfeit vaccines |
| 🟣 Purple | Erectile dysfunction / slimming drugs |
| 🟢 Green | Illegal traditional medicines (jamu with BKO) |
| 🟠 Orange | Contaminated syrups (EG/DEG crisis 2022) |
| ⚫ Dark red | Psychotropic drug abuse |
| 🔵 Blue | Multiple categories / online rings |
| 🩷 Pink | Stem cell / biological products |

**Marker icon encodes sales channel:**
- ☁️ Cloud icon = Online (Shopee, Tokopedia, Lazada, social media)
- 🏠 Home icon = Physical location (warehouse, factory, market)

---

## 📦 Libraries Used and Why

| Library | What it does | Why we need it |
|---------|-------------|----------------|
| `pandas` | Reads and manages data tables | Opens the CSV, cleans the data, and loops through rows to feed into Folium |
| `folium` | Creates interactive HTML maps | Draws the base map, markers, popups, heatmap, and layer control panel |
| `folium.plugins.HeatMap` | Density heatmap layer | Shows where enforcement actions cluster across Indonesian provinces |
| `folium.plugins.MarkerCluster` | Groups overlapping markers | Prevents the map looking cluttered when many cases are in the same city |
| `numpy` | Number operations | Scales heatmap weights using log transformation. Auto-installed with Pandas |

---

## 🚀 How to Run

### Option A — Jupyter Notebook (recommended)

**Step 1 — Clone this repository**
```bash
git clone https://github.com/BroughtonDr/Lesson_Folium.git
cd Lesson_Folium
```

**Step 2 — Install required libraries**
```bash
pip install -r requirements.txt
```

> If you use Anaconda, Pandas and NumPy are already installed. You only need:
> ```bash
> pip install folium
> ```

**Step 3 — Open Jupyter**
```bash
jupyter notebook
```

**Step 4 — Open the notebook**

Navigate to `notebooks/indonesia_counterfeit_map.ipynb` and open it.

**Step 5 — Run all cells**

Go to **Kernel → Restart & Run All**

The interactive map will render inline in the notebook and save to `outputs/indonesia_counterfeit_map.html`.

---

### Option B — Google Colab (no installation needed)

Click below to open directly in Google Colab — no Python installation required:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BroughtonDr/Lesson_Folium/blob/main/notebooks/indonesia_counterfeit_map.ipynb)

The first cell will install all libraries automatically.

---

## 📖 Notebook Structure

| Cell | What it does | Expected output |
|------|-------------|----------------|
| Cell 1 | Import all libraries | Prints ✓ version numbers |
| Cell 2 | Load and clean the CSV | Prints ✓ 28 cases loaded + table preview |
| Cell 3 | Create base map centred on Indonesia | Empty map renders inline |
| Cell 4 | Add colour-coded markers with HTML popups | 28 pins appear on map |
| Cell 5 | Add heatmap layer weighted by seized value | Red density overlay appears |
| Cell 6 | Add online vs physical layers + layer control | Toggle panel appears top-right |
| Cell 7 | Add legend and title | Legend box appears bottom-left |
| Cell 8 | Save final map to outputs/ | HTML file saved |

---

## 📊 The Dataset

**File:** `data/indonesia_counterfeit_medicines_2015_2026.csv`

28 cases compiled from official BPOM press releases and Indonesian news sources (2015–2026).

| Column | Description |
|--------|-------------|
| `case_id` | Unique case number |
| `year` | Year of enforcement action |
| `city` | City where raid occurred |
| `province` | Indonesian province |
| `latitude` | Geographic coordinate |
| `longitude` | Geographic coordinate |
| `venue_type` | Type of location raided |
| `drug_category` | Type of illegal drug |
| `brands_seized` | Specific brands found |
| `quantity_units` | Number of items seized |
| `estimated_value_idr` | Estimated value in IDR |
| `enforcement_agency` | Who conducted the raid |
| `action_taken` | Outcome of enforcement |
| `channel` | How drugs were sold (online/physical) |
| `source_url` | Original BPOM source link |
| `notes` | Full case description |

### Data Sources

- [BPOM Official Press Releases](https://www.pom.go.id/siaran-pers) ← primary source
- [Antara News](https://www.antaranews.com)
- [Kompas](https://www.kompas.id)
- [Tempo](https://www.tempo.co)
- [Media Indonesia](https://mediaindonesia.com)

---

## ⚠️ Common Issues

**Map not showing in Jupyter?**
Go to **File → Trust Notebook**. Folium maps will not render inline in an untrusted notebook.

**`ModuleNotFoundError: No module named 'folium'`**
Run `!pip install folium` in a new cell (with the `!`), then restart the kernel and try again.

**`FileNotFoundError` when loading the CSV**
Make sure `indonesia_counterfeit_medicines_2015_2026.csv` is inside the `data/` folder.

**Map shows 0 markers**
Check that Cell 2 printed `✓ 28 cases loaded`. If not, the CSV path is wrong.

---

## 📚 Reference

*Kesmas: National Public Health Journal* (2017). Counterfeit Medicines in Socioeconomic Perspective, 11(4), 153.
https://doi.org/10.21109/kesmas.v11i4.1440

---

## 📄 How to Cite This Repository

```
BroughtonDr (2026). Counterfeit & Illegal Medicines in Indonesia 2015–2026:
An Interactive Geospatial Analysis Using Python and Folium.
GitHub: https://github.com/BroughtonDr/Lesson_Folium
```

---

## 📜 Licence

This project is licensed under the **MIT Licence** — see [LICENSE](LICENSE) for details.
The dataset is compiled from publicly available government and news sources.
All original sources are credited in the `source_url` column.

---

## 🙋 Questions or Contributions

Found a missing case or spotted an error in the data?

- Open an [Issue](https://github.com/BroughtonDr/Lesson_Folium/issues)
- Or submit a Pull Request with your correction and source link

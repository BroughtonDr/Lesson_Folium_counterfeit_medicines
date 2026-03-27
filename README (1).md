# 🗺️ Counterfeit & Illegal Medicines in Indonesia — Interactive Folium Map

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Folium](https://img.shields.io/badge/Folium-0.15+-green)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Description

This repository contains the Python code, dataset, and Jupyter notebooks for an **interactive geospatial map** visualising counterfeit and illegal medicine enforcement actions by **BPOM** (Badan Pengawas Obat dan Makanan — Indonesia's National Agency of Drug and Food Control) between **2015 and 2026**.

### Academic Background

This project was developed as a practical data visualisation companion to:

> **Counterfeit Medicines in Socioeconomic Perspective**
> *Kesmas: National Public Health Journal*, Vol. 11(4):153, May 2017
> DOI: [10.21109/kesmas.v11i4.1440](https://doi.org/10.21109/kesmas.v11i4.1440)
> Licence: CC BY-SA 4.0

The paper examines counterfeit medicines through a socioeconomic lens — exploring the structural factors that drive their production, the populations most vulnerable to harm, and the regulatory challenges that allow counterfeit medicines to persist in the Indonesian market. It situates the problem within Indonesia's broader health system, where high out-of-pocket costs, limited regulatory enforcement capacity, and fragmented supply chains create conditions that counterfeit medicine producers exploit.

### Why This Map?

The Kesmas paper provides the theoretical and socioeconomic framework. This repository translates that framework into a **spatial analysis** — asking not just *why* counterfeit medicines circulate, but *where* they circulate, *how* they are sold, and *whether* the geography of enforcement matches the geography of the problem.

By mapping 28 confirmed BPOM enforcement actions across Indonesia from 2015 to 2026, this project reveals several patterns that are difficult to see in tabular data alone:

- **Geographic concentration** — enforcement actions cluster heavily in Java, particularly Jakarta, West Java, and Central Java, reflecting both higher population density and stronger BPOM institutional presence in those areas
- **The online shift** — cases from 2021 onwards increasingly involve e-commerce platforms (Shopee, Tokopedia, Lazada), suggesting that counterfeit medicine sellers have migrated to digital channels to evade physical enforcement
- **Outer island gaps** — Sumatra, Kalimantan, Sulawesi, and Papua show very few enforcement markers despite BPOM data showing widespread distribution of counterfeit products to those regions — pointing to a surveillance gap rather than an absence of the problem
- **Escalating scale** — the 2025 Magelang stem cell case (Rp 230 billion) represents a qualitative shift in the nature of pharmaceutical crime, moving beyond traditional pill counterfeiting into high-value biological products
- **Recidivism** — the Banyuwangi case (raided in 2021 and again in 2023 with the same suspect) illustrates the deterrence failure identified in the socioeconomic literature, where penalties are insufficient to stop repeat offending

Together, the paper and this map argue that counterfeit medicines in Indonesia are not a marginal problem — they are a structural feature of a health system under socioeconomic pressure, and they require both stronger enforcement and systemic reform.

---

## 📁 Repository Structure

```
Lesson_Folium_counterfeit_medicines/
│
├── README.md                                            ← You are here
├── requirements.txt                                     ← Libraries to install
├── LICENSE                                              ← MIT licence
│
├── data/
│   └── indonesia_counterfeit_medicines_2015_2026.csv   ← Dataset (28 cases)
│
├── notebooks/
│   ├── folium_official_exercises.ipynb                 ← Official Folium docs exercises
│   └── indonesia_counterfeit_map.ipynb                 ← Main analysis notebook
│
└── outputs/
    └── indonesia_counterfeit_map.html                  ← Generated interactive map
```

---

## 🗺️ What the Map Shows

- 📌 **28 BPOM enforcement cases** plotted as colour-coded markers
- 🔥 A **heatmap** showing raid density weighted by value of medicines seized
- 🔀 **Toggleable layers** separating online vs physical enforcement cases
- 💬 **Clickable popups** with full case details — drug type, quantity, value seized, enforcement agency, and direct link to the original BPOM press release

### Marker Colours — Drug Type

| Colour | Drug Category |
|--------|--------------|
| 🔴 Red | Counterfeit vaccines |
| 🟣 Purple | Erectile dysfunction / slimming drugs |
| 🟢 Green | Illegal traditional medicines (jamu containing BKO) |
| 🟠 Orange | Contaminated syrups (EG/DEG crisis 2022) |
| ⚫ Dark red | Psychotropic drug abuse (e.g. PCC tablets) |
| 🔵 Blue | Multiple categories / online rings |
| 🩷 Pink | Stem cell / biological products |

### Marker Icon — Sales Channel

| Icon | Meaning |
|------|---------|
| ☁️ Cloud | Online — sold via Shopee, Tokopedia, Lazada, or social media |
| 🏠 Home | Physical — warehouse, illegal factory, or market |

---

## 📦 Libraries Used and Why

| Library | What it does | Why we need it |
|---------|-------------|----------------|
| `pandas` | Reads and manages data tables | Opens the CSV, cleans missing values, converts data types, and loops through rows to feed coordinates into Folium |
| `folium` | Creates interactive HTML maps | Draws the base map tiles, markers, popups, heatmap, and layer control panel — the core mapping tool |
| `folium.plugins.HeatMap` | Density heatmap layer | Visualises where enforcement actions cluster, weighted by the estimated value of medicines seized so high-value cases glow brighter |
| `folium.plugins.MarkerCluster` | Groups overlapping markers | Prevents the map from looking cluttered when multiple cases fall in the same city (e.g. Jakarta has several cases) |
| `numpy` | Number operations | Applies log-scale transformation to heatmap weights so extreme values (e.g. Rp 230 billion Magelang case) do not dominate the map entirely |

---

## 🚀 How to Run

### Option A — Jupyter Notebook (recommended)

**Step 1 — Clone this repository**
```bash
git clone https://github.com/BroughtonDr/Lesson_Folium_counterfeit_medicines.git
cd Lesson_Folium_counterfeit_medicines
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

**Step 4 — Choose your notebook**

- Start with `notebooks/folium_official_exercises.ipynb` if you are new to Folium
- Then open `notebooks/indonesia_counterfeit_map.ipynb` for the full analysis

**Step 5 — Run all cells**

Go to **Kernel → Restart & Run All**

The interactive map renders inline in the notebook and saves to `outputs/indonesia_counterfeit_map.html`.

---

### Option B — Google Colab (no installation needed)

Open directly in Google Colab — no Python installation required:

**Official Folium exercises:**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BroughtonDr/Lesson_Folium_counterfeit_medicines/blob/main/notebooks/folium_official_exercises.ipynb)

**Indonesia counterfeit medicines map:**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BroughtonDr/Lesson_Folium_counterfeit_medicines/blob/main/notebooks/indonesia_counterfeit_map.ipynb)

The first cell in each notebook installs all libraries automatically.

---

## 📖 Notebook 1 — Official Folium Exercises

`notebooks/folium_official_exercises.ipynb`

These exercises follow the **official Folium Getting Started documentation** step by step:
> https://python-visualization.github.io/folium/latest/getting_started.html

| Exercise | Topic |
|----------|-------|
| 1 | Installing Folium |
| 2 | Creating a basic map and saving to HTML |
| 3 | Changing the tileset (map background) |
| 4 | Adding markers with popups and tooltips |
| 5 | Drawing lines with PolyLine |
| 6 | Grouping markers with FeatureGroup + LayerControl |
| 7 | Loading GeoJSON boundary data |
| 8 | Building a choropleth map from a DataFrame |

---

## 📖 Notebook 2 — Indonesia Counterfeit Medicines Map

`notebooks/indonesia_counterfeit_map.ipynb`

The main analysis notebook. 8 cells, one task each:

| Cell | What it does | Expected output |
|------|-------------|----------------|
| Cell 1 | Import all libraries | Prints ✓ version numbers |
| Cell 2 | Load and clean the CSV | Prints ✓ 28 cases loaded + table preview |
| Cell 3 | Create base map centred on Indonesia | Empty map renders inline |
| Cell 4 | Add colour-coded markers with HTML popups | 28 pins appear on map |
| Cell 5 | Add heatmap weighted by seized value | Red density overlay appears |
| Cell 6 | Add online vs physical layers + layer control | Toggle panel appears top-right |
| Cell 7 | Add legend and title | Legend box appears bottom-left |
| Cell 8 | Save final map to outputs/ | HTML file saved |

---

## 📊 The Dataset

**File:** `data/indonesia_counterfeit_medicines_2015_2026.csv`

28 enforcement cases compiled from official BPOM press releases and Indonesian news sources (2015–2026).

| Column | Description |
|--------|-------------|
| `case_id` | Unique case number |
| `year` | Year of enforcement action |
| `date` | Date if known |
| `city` | City where raid occurred |
| `province` | Indonesian province |
| `latitude` | Geographic coordinate |
| `longitude` | Geographic coordinate |
| `venue_type` | Type of location raided |
| `drug_category` | Type of illegal drug |
| `brands_seized` | Specific brands found |
| `quantity_units` | Number of items seized |
| `estimated_value_idr` | Estimated value in Indonesian Rupiah |
| `enforcement_agency` | Who conducted the raid |
| `action_taken` | Outcome of enforcement action |
| `channel` | How drugs were sold (online / physical) |
| `source_url` | Original BPOM press release link |
| `notes` | Full case description and context |

### Data Sources

- [BPOM Official Press Releases](https://www.pom.go.id/siaran-pers) ← primary source
- [Antara News](https://www.antaranews.com)
- [Kompas](https://www.kompas.id)
- [Tempo](https://www.tempo.co)
- [Media Indonesia](https://mediaindonesia.com)
- [Indonesia.go.id](https://indonesia.go.id)

---

## ⚠️ Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| Map not showing in Jupyter | Go to **File → Trust Notebook** — Folium maps do not render in untrusted notebooks |
| `ModuleNotFoundError: No module named 'folium'` | Run `!pip install folium` in a new cell, then restart the kernel |
| `FileNotFoundError` when loading CSV | Make sure the CSV is inside the `data/` folder, not somewhere else |
| Map shows 0 markers | Check that Cell 2 printed `✓ 28 cases loaded` — if not, the CSV path is wrong |
| Map shows only a grey box | Wait a few seconds — the map tiles need to load from the internet |

---

## 📚 Reference

*Kesmas: National Public Health Journal* (2017). Counterfeit Medicines in Socioeconomic Perspective, 11(4), 153.
https://doi.org/10.21109/kesmas.v11i4.1440

---

## 📄 How to Cite This Repository

```
BroughtonDr (2026). Counterfeit & Illegal Medicines in Indonesia 2015–2026:
An Interactive Geospatial Analysis Using Python and Folium.
GitHub: https://github.com/BroughtonDr/Lesson_Folium_counterfeit_medicines
```

---

## 📜 Licence

This project is licensed under the **MIT Licence** — see [LICENSE](LICENSE) for details.

The dataset is compiled from publicly available government and news sources. All original sources are credited in the `source_url` column of the dataset.

---

## 🙋 Questions or Contributions

Found a missing enforcement case? Spotted an error in the data? Want to extend the analysis to a different region or time period?

- Open an [Issue](https://github.com/BroughtonDr/Lesson_Folium_counterfeit_medicines/issues)
- Or submit a Pull Request with your correction and a link to the source

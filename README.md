🗺️ Counterfeit & Illegal Medicines in Indonesia — Interactive Folium Map

📋 Description
This repository contains the Python code, dataset, and Jupyter notebooks for an interactive geospatial map visualising counterfeit and illegal medicine enforcement actions by BPOM (Badan Pengawas Obat dan Makanan — Indonesia's National Agency of Drug and Food Control) between 2015 and 2026.
Academic Background
This project was developed as a practical data visualisation companion to:

Counterfeit Medicines in Socioeconomic Perspective
Kesmas: National Public Health Journal, Vol. 11(4):153, May 2017
DOI: 10.21109/kesmas.v11i4.1440
Licence: CC BY-SA 4.0

The paper examines counterfeit medicines through a socioeconomic lens — exploring the structural factors that drive their production, the populations most vulnerable to harm, and the regulatory challenges that allow counterfeit medicines to persist in the Indonesian market. It situates the problem within Indonesia's broader health system, where high out-of-pocket costs, limited regulatory enforcement capacity, and fragmented supply chains create conditions that counterfeit medicine producers exploit.
Why This Map?
The Kesmas paper provides the theoretical and socioeconomic framework. This repository translates that framework into a spatial analysis — asking not just why counterfeit medicines circulate, but where they circulate, how they are sold, and whether the geography of enforcement matches the geography of the problem.
By mapping 28 confirmed BPOM enforcement actions across Indonesia from 2015 to 2026, this project reveals several patterns that are difficult to see in tabular data alone:

Geographic concentration — enforcement actions cluster heavily in Java, particularly Jakarta, West Java, and Central Java, reflecting both higher population density and stronger BPOM institutional presence in those areas
The online shift — cases from 2021 onwards increasingly involve e-commerce platforms (Shopee, Tokopedia, Lazada), suggesting that counterfeit medicine sellers have migrated to digital channels to evade physical enforcement
Outer island gaps — Sumatra, Kalimantan, Sulawesi, and Papua show very few enforcement markers despite BPOM data showing widespread distribution of counterfeit products to those regions — pointing to a surveillance gap rather than an absence of the problem
Escalating scale — the 2025 Magelang stem cell case (Rp 230 billion) represents a qualitative shift in the nature of pharmaceutical crime, moving beyond traditional pill counterfeiting into high-value biological products
Recidivism — the Banyuwangi case (raided in 2021 and again in 2023 with the same suspect) illustrates the deterrence failure identified in the socioeconomic literature, where penalties are insufficient to stop repeat offending

Together, the paper and this map argue that counterfeit medicines in Indonesia are not a marginal problem — they are a structural feature of a health system under socioeconomic pressure, and they require both stronger enforcement and systemic reform.

📁 Repository Structure
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

🗺️ What the Map Shows

📌 28 BPOM enforcement cases plotted as colour-coded markers
🔥 A heatmap showing raid density weighted by value of medicines seized
🔀 Toggleable layers separating online vs physical enforcement cases
💬 Clickable popups with full case details — drug type, quantity, value seized, enforcement agency, and direct link to the original BPOM press release

Marker Colours — Drug Type
ColourDrug Category🔴 RedCounterfeit vaccines🟣 PurpleErectile dysfunction / slimming drugs🟢 GreenIllegal traditional medicines (jamu containing BKO)🟠 OrangeContaminated syrups (EG/DEG crisis 2022)⚫ Dark redPsychotropic drug abuse (e.g. PCC tablets)🔵 BlueMultiple categories / online rings🩷 PinkStem cell / biological products
Marker Icon — Sales Channel
IconMeaning☁️ CloudOnline — sold via Shopee, Tokopedia, Lazada, or social media🏠 HomePhysical — warehouse, illegal factory, or market

📦 Libraries Used and Why
LibraryWhat it doesWhy we need itpandasReads and manages data tablesOpens the CSV, cleans missing values, converts data types, and loops through rows to feed coordinates into FoliumfoliumCreates interactive HTML mapsDraws the base map tiles, markers, popups, heatmap, and layer control panel — the core mapping toolfolium.plugins.HeatMapDensity heatmap layerVisualises where enforcement actions cluster, weighted by the estimated value of medicines seized so high-value cases glow brighterfolium.plugins.MarkerClusterGroups overlapping markersPrevents the map from looking cluttered when multiple cases fall in the same city (e.g. Jakarta has several cases)numpyNumber operationsApplies log-scale transformation to heatmap weights so extreme values (e.g. Rp 230 billion Magelang case) do not dominate the map entirely

🚀 How to Run
Option A — Jupyter Notebook (recommended)
Step 1 — Clone this repository
bashgit clone https://github.com/BroughtonDr/Lesson_Folium_counterfeit_medicines.git
cd Lesson_Folium_counterfeit_medicines
Step 2 — Install required libraries
bashpip install -r requirements.txt

If you use Anaconda, Pandas and NumPy are already installed. You only need:
bashpip install folium

Step 3 — Open Jupyter
bashjupyter notebook
Step 4 — Choose your notebook

Start with notebooks/folium_official_exercises.ipynb if you are new to Folium
Then open notebooks/indonesia_counterfeit_map.ipynb for the full analysis

Step 5 — Run all cells
Go to Kernel → Restart & Run All
The interactive map renders inline in the notebook and saves to outputs/indonesia_counterfeit_map.html.

Option B — Google Colab (no installation needed)
Open directly in Google Colab — no Python installation required:
Official Folium exercises:
Show Image
Indonesia counterfeit medicines map:
Show Image
The first cell in each notebook installs all libraries automatically.

📖 Notebook 1 — Official Folium Exercises
notebooks/folium_official_exercises.ipynb
These exercises follow the official Folium Getting Started documentation step by step:

https://python-visualization.github.io/folium/latest/getting_started.html

ExerciseTopic1Installing Folium2Creating a basic map and saving to HTML3Changing the tileset (map background)4Adding markers with popups and tooltips5Drawing lines with PolyLine6Grouping markers with FeatureGroup + LayerControl7Loading GeoJSON boundary data8Building a choropleth map from a DataFrame

📖 Notebook 2 — Indonesia Counterfeit Medicines Map
notebooks/indonesia_counterfeit_map.ipynb
The main analysis notebook. 8 cells, one task each:
CellWhat it doesExpected outputCell 1Import all librariesPrints ✓ version numbersCell 2Load and clean the CSVPrints ✓ 28 cases loaded + table previewCell 3Create base map centred on IndonesiaEmpty map renders inlineCell 4Add colour-coded markers with HTML popups28 pins appear on mapCell 5Add heatmap weighted by seized valueRed density overlay appearsCell 6Add online vs physical layers + layer controlToggle panel appears top-rightCell 7Add legend and titleLegend box appears bottom-leftCell 8Save final map to outputs/HTML file saved

📊 The Dataset
File: data/indonesia_counterfeit_medicines_2015_2026.csv
28 enforcement cases compiled from official BPOM press releases and Indonesian news sources (2015–2026).
ColumnDescriptioncase_idUnique case numberyearYear of enforcement actiondateDate if knowncityCity where raid occurredprovinceIndonesian provincelatitudeGeographic coordinatelongitudeGeographic coordinatevenue_typeType of location raideddrug_categoryType of illegal drugbrands_seizedSpecific brands foundquantity_unitsNumber of items seizedestimated_value_idrEstimated value in Indonesian Rupiahenforcement_agencyWho conducted the raidaction_takenOutcome of enforcement actionchannelHow drugs were sold (online / physical)source_urlOriginal BPOM press release linknotesFull case description and context
Data Sources

BPOM Official Press Releases ← primary source
Antara News
Kompas
Tempo
Media Indonesia
Indonesia.go.id


⚠️ Common Issues and Solutions
ProblemSolutionMap not showing in JupyterGo to File → Trust Notebook — Folium maps do not render in untrusted notebooksModuleNotFoundError: No module named 'folium'Run !pip install folium in a new cell, then restart the kernelFileNotFoundError when loading CSVMake sure the CSV is inside the data/ folder, not somewhere elseMap shows 0 markersCheck that Cell 2 printed ✓ 28 cases loaded — if not, the CSV path is wrongMap shows only a grey boxWait a few seconds — the map tiles need to load from the internet

📚 Reference
Kesmas: National Public Health Journal (2017). Counterfeit Medicines in Socioeconomic Perspective, 11(4), 153.
https://doi.org/10.21109/kesmas.v11i4.1440

📄 How to Cite This Repository
BroughtonDr (2026). Counterfeit & Illegal Medicines in Indonesia 2015–2026:
An Interactive Geospatial Analysis Using Python and Folium.
GitHub: https://github.com/BroughtonDr/Lesson_Folium_counterfeit_medicines

📜 Licence
This project is licensed under the MIT Licence — see LICENSE for details.
The dataset is compiled from publicly available government and news sources. All original sources are credited in the source_url column of the dataset.

🙋 Questions or Contributions
Found a missing enforcement case? Spotted an error in the data? Want to extend the analysis to a different region or time period?

Open an Issue
Or submit a Pull Request with your correction and a link to the source

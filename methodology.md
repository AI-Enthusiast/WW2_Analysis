---
layout: default
title: Methodology
---

# Methodology

## Data Collection

The initial dataset was sourced from two Wikipedia pages that list all the German U-Boats from U-1 to U-4712. The data collection process involved:

1. **Primary Sources**: Wikipedia pages listing German U-Boats
2. **Secondary Collection**: Individual U-Boat pages for commissioning dates
3. **Data Fields**: U-Boat name, year, type, notable commanders, damage statistics, fate, and notes

## Data Processing Pipeline

### Step 1: Web Scraping
- **Tool**: Python with BeautifulSoup and requests
- **Process**: Automated scraping of U-Boat data from Wikipedia
- **Output**: Raw CSV files with U-Boat information

### Step 2: Data Cleaning
- **Tool**: R with tidyverse
- **Process**: 
  - Removed unnecessary columns
  - Calculated active service days (commissioning to fate date)
  - Standardized categorical variables
- **Output**: Clean dataset ready for analysis

### Step 3: Survival Analysis
- **Tools**: R with survival and survminer packages
- **Methods**: 
  - Kaplan-Meier survival curves
  - Cox Proportional Hazards modeling
  - Log-rank tests for group comparisons

## Statistical Methods

### Survival Analysis Approach
We treated U-Boat "death" (sinking, capture, scuttling) as events and calculated time-to-event from commissioning date.

### Key Metrics
- **Active Service Days**: Primary outcome variable
- **Event Status**: Binary indicator of U-Boat fate
- **Covariates**: U-Boat type, commissioning year, notable commanders

### Model Validation
- Proportional hazards assumption testing
- Residual analysis
- Cross-validation techniques

## Limitations

1. **Data Quality**: Reliance on Wikipedia may introduce inaccuracies
2. **Missing Data**: Some commissioning dates were unavailable
3. **Survival Bias**: Focus only on documented U-Boats
4. **Historical Context**: Limited accounting for operational changes during war

[Back to Main Analysis](/)

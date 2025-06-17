---
layout: default
title: Data Sources
---

# Data Sources and Downloads

## Primary Data Sources

### Wikipedia Sources
1. **[List of German U-boats in World War II (1-599)](https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(1-599))**
   - Comprehensive listing of early war U-Boats
   - Includes technical specifications and operational history

2. **[List of German U-boats in World War II (600-4712)](https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(600-4712))**
   - Late war U-Boat documentation
   - Coverage of advanced submarine designs

3. **Individual U-Boat Pages**
   - Detailed commissioning and fate information
   - Commander assignments and operational records

## Dataset Downloads

### Raw Data
- **[uboats.csv](uboats.csv)** - Original scraped data from Wikipedia
  - 1,162 U-Boats documented
  - Fields: Name, Year, Type, Commanders, Damage, Fate, Notes

### Processed Data
- **[uboats_cleaned.csv](uboats_cleaned.csv)** - Analysis-ready dataset
  - Active service days calculated
  - Standardized categorical variables
  - Missing data handled

### Supplementary Data
- **[uboat_commanders.csv](uboat_commanders.csv)** - Commander information
  - Notable commander classifications
  - Command tenure data

## Data Quality Notes

### Completeness
- **Commissioning Dates**: 94% complete
- **Fate Information**: 98% complete
- **Type Classification**: 100% complete

### Validation Methods
1. Cross-reference with historical records
2. Consistency checks across related fields
3. Outlier detection and manual verification

### Known Limitations
- Some early U-Boats have incomplete records
- Wikipedia editing may introduce temporal inconsistencies
- Operational vs. commissioning dates occasionally conflated

## Usage License

This dataset is compiled from public Wikipedia sources and is available under the same Creative Commons licensing. Please cite this repository if used in academic work.

## Citation Format

```
Dacker, C. (2024). Depths of Survival: U-Boat Longevity Analysis Dataset. 
GitHub Repository: https://github.com/yourusername/WW2_Analysis
```

[Back to Main Analysis](/)

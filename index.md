---
layout: default
title: Home
---

# Depths of Survival: U-Boat Longevity Analysis

![Analysis Status](https://img.shields.io/badge/Analysis-Complete-green)
![Data Source](https://img.shields.io/badge/Data-Wikipedia-blue)
![Language](https://img.shields.io/badge/Language-R%2FPython-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Quick Navigation
- [📊 View Results](results.html)
- [🔬 Methodology](methodology.html)
- [📁 Data Sources](data.html)
- [💻 GitHub Repository](https://github.com/AI-Enthusiast/WW2_Analysis)

## Project Overview

This project analyzes the survival patterns of German U-Boats during World War II using statistical survival analysis techniques. We examine over 1,000 U-Boats to understand what factors contributed to their longevity in combat.

### Key Questions Answered
- How did U-Boat survival rates change during the war?
- Which U-Boat types had the best survival rates?
- Did notable commanders improve crew survival chances?

## Major Findings

<div style="background-color: #f8f9fa; padding: 20px; border-left: 4px solid #007bff; margin: 20px 0;">
<h3>🔍 Key Discovery</h3>
<p><strong>Notable commanders increased U-Boat survival time by 400-800 days on average</strong> - highlighting the critical importance of experienced leadership in submarine warfare.</p>
</div>

### War Period Impact
U-Boats commissioned during WWII had dramatically shorter lifespans than those from the interwar period, reflecting the intensification of anti-submarine warfare.

### Type VIIC Advantage  
The most common U-Boat type (VIIC) showed the best survival rates, likely due to crew familiarity and easier maintenance.

## Interactive Visualizations

<div class="image-gallery">
  <div class="image-item">
    <img src="slides/km_by_war.png" alt="Survival by War Period" style="width: 100%; max-width: 500px;">
    <p><em>Survival curves by war period show the harsh reality of WWII operations</em></p>
  </div>
  
  <div class="image-item">
    <img src="slides/km_by_cmd.png" alt="Survival by Commander" style="width: 100%; max-width: 500px;">
    <p><em>The dramatic impact of notable commanders on U-Boat survival</em></p>
  </div>
</div>

## Technical Approach

This analysis uses **survival analysis** techniques including:
- Kaplan-Meier survival curves
- Cox Proportional Hazards modeling
- Log-rank statistical tests

**Technologies**: R, Python, ggplot2, survival package, BeautifulSoup

## Quick Start

```bash
# Clone the repository
git clone https://github.com/AI-Enthusiast/WW2_Analysis.git

# Install R dependencies
R -e "install.packages(c('tidyverse', 'survival', 'survminer'))"

# View the analysis
open u-boat_analysis.rmd
```

## Dataset

- **1,162 German U-Boats** from U-1 to U-4712
- **Primary Source**: Wikipedia comprehensive listings
- **Time Period**: 1935-1945
- **Key Variables**: Commissioning date, fate, type, commanders

[📥 Download Clean Dataset](uboats_cleaned.csv)

---

<div style="text-align: center; margin-top: 40px; padding: 20px; background-color: #f1f1f1;">
<p><strong>Author:</strong> Cormac Dacker, 2024</p>
<p>📧 Contact | 🐙 GitHub | 💼 LinkedIn</p>
</div>

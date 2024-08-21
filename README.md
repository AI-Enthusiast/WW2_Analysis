# Depths of Survival: Analyzing U-Boat Longevity in the World Wars

##### Cormac Dacker, 2024

## Introduction

Submarines have been a staple of naval warfare since the American Revolutionary war[1], but it wasn't until the World
Wars that they became a major player in the world's navies. The German U-Boats, in particular, were a major threat to
Allied shipping during both World Wars.[2]  In this project, I will analyze the longevity of U-Boats in the World Wars,
focusing on the factors that contributed to their survival or destruction.

## Methodology

### Data

The initial dataset was sourced from two wikipedia pages[3][4] that list all the German U-Boats from U-1 to U-4712. The
data includes the U-Boat name, year (unexplained), type, notable commanders, the damage it did to warships and merchant
ships, its fate, and notes which can be various things such as (but not limited to) the cause of its fate. To this table
I doubled back to each of the U-Boats respective wikipedia pages to gather the date of commissioning, which I considered
the most useful in terms of survival analysis. With the fate date and commissioning date, I was able to calculate the
number of days each U-Boat saw service, called active service. This was the primary metric I used to analyze the
longevity of the U-Boats.

### EDA

<img src="slides/avg_lifespan_by_year.png?raw=true"/>

Here we get a bar chart of the average lifespan of U-Boats by year. This shows that the average lifespan of U-Boats has
been decreasing over time. This could be due to a number of factors, such as improved technology, better tactics, or
simply the fact that the U-Boats were being used more aggressively (and recklessly) as the war went on.

<img src="slides/hist_of_lifespan.png?raw=true"/>

This histogram shows the distribution of the lifespan of U-Boats. The majority of U-Boats had a lifespan of less than
1000 days. While clearly left leaning losses do steady out to just under a dozen every 100 days (a bins width), after
the 1000 day mark. Shockingly there are even a few U-Boats that make it past 3000 days (over 8 years).

<img src="slides/unique_fates_by_count.png?raw=true"/>

This bar chart shows the number of U-Boats that had each fate. This informs our survival analysis by showing us the
which U-Boats survived and which did not. The majority of U-Boats were sunk, but there were also a significant number
that were scuttled, captured, or surrendered.

<img src="slides/unique_types_by_count.png?raw=true"/>

This bar chart shows the number of U-Boats of each type. This informs our survival analysis by showing us the which
U-Boats were most common. The majority of U-Boats were Type VIIC, but there were also a significant number of Type IX
and Type IXC U-Boats. For the purposes of this analysis we will only be focusing on the top 5 as I feel there is
sufficient data to inform our analysis.

### Process

1. **Data Collection**: Scraped data from Wikipedia using Python and BeautifulSoup.
2. **Data Cleaning**: Cleaned the data in R, removing unnecessary columns and calculating active service days.
3. **Data Analysis**: Analyzed the data in R using survival analysis techniques.
4. **Data Visualization**: Visualized the data using ggplot2 and survminer.
5. **Hypothesis Testing**: Tested the impact of U-Boat type and notable commanders on active service days.
6. **Modeling**: Used a Cox Proportional Hazards model to analyze the impact of U-Boat type and notable commanders on
   active service days.
7. **Visualization**: Used a Kaplan-Meier curve to visualize the survival of the U-Boats over time.
8. **Results**: Analyzed the results and drew conclusions based on the data.

### Technologies

The initial data was compiled in a Python notebook (wiki_scraper_proto.ipynb) using the pandas, requests, and
BeautifulSoup, and tqdm libraries. The data was then cleaned and using R (u-boat_cleaner.rmd) calculating the active
service days for each U-Boat, using the tidyverse library. The data was then analyzed in R (u-boat_analysis.rmd) using
the survival, and fitdistrplus. The data was visualized using ggplot2 and the survminer libraries.

### Hypothesis

I hypothesize that the type of U-Boat will have a significant impact on its longevity. Specifically, I believe that the
type of U-Boat will be a significant predictor of the number of days it saw active service. I also hypothesize that the
notable commanders of a U-Boat will have a significant impact on its longevity. I believe that the U-Boats with the most
notable commanders will have the longest active service days.

## Evaluation

To evaluate the hypothesis, I will use a Cox Proportional Hazards model to analyze the impact of the type of U-Boat and
the notable commanders on the active service days of the U-Boats. I will also use a Kaplan-Meier curve to visualize the
survival of the U-Boats over time.

### Results

#### War Year
<img src="slides/km_by_com_year.png?raw=true"/>

#### Ship Type

<img src="slides/km_by_type.png?raw=true"/>

#### Notable Commanders

<img src="slides/km_by_cmd.png?raw=true"/>


[//]: # (Heinz-Otto Schultze)

[//]: # (Wolfgang Lüth)

[//]: # (Günther Prien)

## Conclusion

## References

[1] https://en.wikipedia.org/wiki/Turtle_(submersible)

[2] https://en.wikipedia.org/wiki/U-boat

[3] https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(1-599)

[4] https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(600-4712)
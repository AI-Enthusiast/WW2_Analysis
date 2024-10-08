# Depths of Survival: Analyzing U-Boat Longevity in the World Wars

##### Cormac Dacker, 2024 [work in progress]

## Introduction

Submarines have been a staple of naval warfare since the American Revolutionary war[1], but it wasn't until the World
Wars that they became a major player in the world's navies. The German U-Boats, in particular, were a major threat to
Allied shipping during both World Wars.[2]  In this project, I will analyze the longevity of U-Boats in the Second World
War,
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

To evaluate the hypothesis, I will use a ~~Cox Proportional Hazards~~ model to analyze the impact of the type of U-Boat and
the notable commanders on the active service days of the U-Boats. I will also use a Kaplan-Meier curve to visualize the
survival of the U-Boats over time.

### Results

#### War Year

<img src="slides/km_by_com_year.png?raw=true"/>

This colorful spaghetti plot shows the survival of U-Boats over time. The different colors represent the different
years. While there is clearly a problem with too much being shown and some of the pre war years not having many
commisioned datas so the margins of error are significantly wide and obscuring our view of the data. This is a good
starting point, but we need to refine our data to get a clearer picture.

<img src="slides/km_by_war.png?raw=true"/>

By grouping the data into WWII and interwar years we get a much clearer picture of the survival of U-Boats over time.
The U-Boats that were commissioned during WWII had a much shorter lifespan than those that were commissioned during the
interwar years. This is likely due to the increased aggression and intensity of the war. The losses of interwar U-Boats
experiences increased infant mortality probably but stead out after the 500 day mark. This may be because the interwar
U-Boats were outdated and their crews were moved to newer U-Boats. Once resources became scare in the latter third of
the war U-Boast where used more sparingly and thus losses were less frequent.

#### Ship Type

<img src="slides/km_by_type.png?raw=true"/>

Here there is a clear trend that all the U-Bots have a similar survival rate. The best performing U-Boat type is the
Type VIIC, which is the most common type of U-Boat. This probably results in its higher survival rates, both in terms of
training and repairability. It is noted that while these boats were smaller, that allowed them to crash dive faster than
larger boats, perhaps spareing the men aboard of depth charges.[5] Unfortunately, these factors also lead it to be th
only
type in our analysis to be used till almost the end, with only 25% chance to make it to the last half of the WWII.

#### Notable Commanders

<img src="slides/km_by_cmd.png?raw=true"/>

This plot shows the survival of U-Boats by notable commanders. This clearly shows that boats with notable commanders
typically survive between 400-800 (due to margins of error) days longer than those without. This is likely due to the
experience and skill of the commanders, as well as the morale boost they provide to the crew. Boats without a notable
commander have a 50% chance of surviving to ~500 days, while those with a notable commander have a 50% chance of
surviving to 900 days. Shockingly boats with notable commanders have a 25% chance of surviving to 2000 days.

## Conclusion

[placeholder for conclusion]

In conclusion, the longevity of U-Boats in the Second World War was influenced by a number of factors. The survival
rates of U-Boats were worse for boats that were commissioned during the war, likely due to the increased aggression and
intensity of the war. The top 5 boats shared similar survival curves, probably due to being commissioned during the war.
The Type VIIC boats had the best survival rates, probably due to being the most common and smaller. Boats with notable
commanders had better survival rates, probably due to the experience and morale boost they provided to the crew.


## References

[1] https://en.wikipedia.org/wiki/Turtle_(submersible)

[2] https://en.wikipedia.org/wiki/U-boat

[3] https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(1-599)

[4] https://en.wikipedia.org/wiki/List_of_German_U-boats_in_World_War_II_(600-4712)

[5] https://en.wikipedia.org/wiki/Type_VII_submarine
---
layout: page
title: Power Outages 🔋
description: Description of the power outages dataset in Project 3.
parent: 'Project 3'
nav_exclude: true
---

# Power Outages 🔋
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This dataset has major power outage data in the continental U.S. from January 2000 to July 2016.

---

## Getting the Data

The data is downloadable [here](https://engineering.purdue.edu/LASCI/research-data/outages/outagerisks).

***Note***: If you are having a hard time with the "This dataset" link, hold shift and click the link to open it into a new tab and then refresh that new tab.

A data dictionary is available at this [article](https://www.sciencedirect.com/science/article/pii/S2352340918307182) under *Table 1. Variable descriptions*.

---

## Sample Questions

- Where and when do major power outages tend to occur?
- What are the characteristics of major power outages with higher severity? Variables to consider include location, time, climate, land-use characteristics, electricity consumption patterns, economic characteristics, etc. What risk factors may an energy company want to look into when predicting the location and severity of its next major power outage?
- What characteristics are associated with each category of cause?
- How have characteristics of major power outages changed over time? Is there a clear trend?

---

## Cleaning and EDA

Follow all of the steps in the [Requirement: Cleaning and EDA](../#requirement-cleaning-and-eda-exploratory-data-analysis) section. 

***Notes***:
- The data is given as an Excel file rather than a CSV. Open the data in Google Sheets or another spreadsheet application and determine which rows and columns of the sheet should be ignored when loading the data in `pandas`.
    - Note that `pandas` can load multiple filetypes: `pd.read_csv`, `pd.read_excel`, `pd.read_html`, `pd.read_json`, etc.
- The power outage start date and time is given by `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'`. It would be preferable if these two columns were combined into one `pd.Timestamp` column. Combine `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.START'`. Similarly, combine `'OUTAGE.RESTORATION.DATE'` and `'OUTAGE.RESTORATION.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.RESTORATION'`.
    - `pd.to_datetime` and `pd.to_timedelta` will be useful here.

***Tip***: To visualize geospatial data, consider [Folium](https://python-visualization.github.io/folium/) or another geospatial plotting library. You can even embed Folium maps in your website! If `fig` is a `folium.folium.Map` object, then `fig._repr_html_()` evaluates to a string containing your plot as HTML; use `open` and `write` to write this string to an `.html` file.

---

## Assessment of Missingness

Follow all of the steps in the [Requirement: Assessment of Missingness](../#requirement-assessment-of-missingness) section.

---

## Hypothesis Test

Follow all of the steps in the [Requirement: Hypothesis Testing](../#requirement-hypothesis-testing) section. You can use the sample questions for inspiration.
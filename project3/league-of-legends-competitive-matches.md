---
layout: page
title: League of Legends Competitive Matches ⌨️
description: Description of the League of Legends dataset in Project 3.
parent: 'Project 3'
nav_exclude: true
---

# League of Legends Competitive Matches ⌨️
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

Welcome to Summoner's Rift! This dataset contains information of players and teams from over 10,000 League of Legends competitive matches.

{: .note }
You'll probably want to be at least a little bit familiar with [*League of Legends*](https://en.wikipedia.org/wiki/League_of_Legends) and its terminology to use this dataset. If not, one of the other datasets may be more interesting to you.

---

## Getting the Data

The data can be found on the website [Oracle's Elixir](https://oracleselixir.com/tools/downloads) at the provided Google Drive link.

To make sure that you're able to satisfy the requirements of the project, use match data from 2022. You may use the older datasets if you wish, but keep in mind that League of Legends changes significantly between years; this can make it difficult to combine or make comparisons between datasets from different years.

---

## Sample Questions

- Looking at [tier-one professional leagues](https://en.wikipedia.org/wiki/List_of_League_of_Legends_leagues_and_tournaments), which league has the most "action-packed" games? Is the amount of "action" in this league significantly different than in other leagues? Note that you'll have to come up with a way of quantifying "action".
- Which competitive region has the highest win rate against teams outside their region? Note you will have to find and merge region data for this question as the dataset does not have it.
- Which role "carries" (does the best) in their team more often: ADCs (Bot lanes) or Mid laners?
- Is Talon (tutor Costin's favorite champion) more likely to win or lose any given match?

---

## Cleaning and EDA

Follow all of the steps in the [Requirement: Cleaning and EDA](../#requirement-cleaning-and-eda-exploratory-data-analysis) section. 

***Notes***:
- Each `'gameid'` corresponds to up to 12 rows – one for each of the 5 players on both teams and 2 containing summary data for the two teams (try to find out what distinguishes those rows). After selecting your line of inquiry, make sure to remove either the player rows or the team rows so as not to have issues later in your analysis.
- Many columns should be of type `bool` but are not.

---

## Assessment of Missingness

Follow all of the steps in the [Requirement: Assessment of Missingness](../#requirement-assessment-of-missingness) section.

---

## Hypothesis Testing

Follow all of the steps in the [Requirement: Hypothesis Testing](../#requirement-hypothesis-testing) section. You can use the sample questions for inspiration.
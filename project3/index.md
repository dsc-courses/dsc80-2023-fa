---
layout: page
title: Project 3
description: Description of Project 3.
nav_exclude: true
---

<script type="text/javascript" async="" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>

# Project 3 – Exploratory Data Analysis 📊
{:.no_toc}

### Due Date: Thursday, May 18th at 11:59PM (No Checkpoint!)
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Welcome to Project 3! 👋

This project contains no new material. Rather, it's a good opportunity to sharpen your understanding of the core concepts of the first half of the course. It'll also give you practice with creating visualizations and websites, and will give you something concrete to put on your resume and show to potential employers!

The project is broken into two parts:
- Part 1: An **analysis**, submitted as a Jupyter Notebook. This will contain the details of your work. **Focus on completing your analysis before moving to Part 2, as the analysis is the bulk of the project.**
- Part 2: A **report**, submitted as a website. This will contain a narrative "story" with visuals. **Focus on this after finishing _most_ of your analysis.**

{: .warning }
**The project is due on Thursday, May 18th at 11:59PM**. While there is no checkpoint, we encourage you to finish Part 1 by Monday, May 15th, to leave yourself three days to review your analysis and prepare your report.<br><br>Like other projects, you're welcome to work with a partner, though if you do, you must **both** work on all pieces together, simultaneously. You will only submit one notebook and create one website.

---

## Choosing a Dataset

In this project, you will perform an open-ended investigation into a **single dataset** (that's right – no autograders!). You must choose **one** of the following three datasets:

- [Recipes and Ratings 🍽](recipes-and-ratings)
- [Power Outages 🔋](power-outages)
- [League of Legends Competitive Matches ⌨️](league-of-legends-competitive-matches)

By clicking the above links, you'll find descriptions, download links, and guidelines for each dataset. When selecting which dataset you are going to use for your project, try choosing the one whose topic appeals to you the most as that will make finishing the project a lot more enjoyable. Furthermore, **Project 5 will also be an open-ended project and will require you to choose one of the same three datasets. We recommend that you choose the same dataset in both Project 3 and Project 5**, so that you don't have to relearn a new dataset for Project 5.

You may want to read the rest of this page before choosing a dataset.

---

## Part 1: Analysis

Before beginning your analysis, you'll need to set up a few things.
1. Pull the latest version of the [`dsc80-2023-sp`](https://github.com/dsc-courses/dsc80-2023-sp/) repo. Within the `projects/03-eda` folder, there is a `template.ipynb` notebook that you will use as a template for the project. If you delete the file or want another copy of the template, you can re-download it from [here](https://github.com/dsc-courses/dsc80-2023-sp/blob/master/projects/03-eda/template.ipynb). **This is where your analysis will live; you will submit this entire notebook to us.**
1. Select **one** of the three [datasets mentioned above](#choosing-a-dataset), download it, and load it into your template notebook.

Once you have your dataset loaded in your notebook, it's time for you to find meaning in the real-world data you've collected! Follow the steps below.

***Tip***: For each step, we specify what must be done in your notebook and what must go on your website. We recommend you write everything in your notebook first, and then move things over to your website once you've completed your analysis.

### Requirement: Introduction

| Step | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Introduction and Question Identification** | Understand the data you have access to. Brainstorm a few questions that interest you about the dataset. Pick **one** question you plan to investigate further. (As the [data science lifecycle](https://dsc80.com/resources/lectures/lec01/lec01.html#The-data-science-lifecycle) tells us, this question may change as you work on your project.) | Provide an introduction to your dataset, and clearly state the one question your analysis is centered around. Why should readers of your website care about the dataset and your question specifically? Report the number of rows in the dataset, the names of the columns that are relevant to your question, and descriptions of those relevant columns. |

### Requirement: Cleaning and EDA (Exploratory Data Analysis)

| Step | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Data Cleaning** | Clean the data appropriately. For instance, you may need to replace data that should be missing with `NaN` or create new columns out of given ones (e.g. compute distances, scale data, or get time information from time stamps). | Describe, in detail, the data cleaning steps you took and how they affected your analyses. The steps should be explained in reference to the data generating process. Show the `head` of your cleaned DataFrame (see [Part 2: Report](#part-2-report) for instructions). |
| **Univariate Analysis** | Look at the distributions of relevant columns separately by using DataFrame operations and drawing at least two relevant plots. | Embed **at least one** `plotly` plot you created in your notebook that displays the distribution of a single column (see [Part 2: Report](#part-2-report) for instructions). Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one univariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.) |
| **Bivariate Analysis** | Look at the statistics of pairs of columns to identify possible associations. For instance, you may create scatter plots and plot conditional distributions, or box-plots. You must plot at least two such plots in your notebook. The results of your bivariate analyses will be helpful in identifying interesting hypothesis tests! | Embed **at least one** `plotly` plot that displays the relationship between two columns. Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one bivariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.) |
| **Interesting Aggregates** | Choose columns to group and pivot by and examine aggregate statistics. | Embed at least one grouped table or pivot table in your website and explain its significance. |

### Requirement: Assessment of Missingness

| Step | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **NMAR Analysis** | Recall, to determine whether data are likely NMAR, you must reason about the data generating process; you cannot conclude that data are likely NMAR solely by looking at your data. As such, there's no code to write here (and hence, nothing to put in your notebook). | State whether you believe there is a column in your dataset that is NMAR. Explain your reasoning and any additional data you might want to obtain that could explain the missingness (thereby making it MAR). Make sure to explicitly use the term "NMAR." |
| **Missingness Dependency** | Pick a column in the dataset with non-trivial missingness to analyze, and perform permutation tests to analyze the dependency of the missingness of this column on other columns.<br><br>Specifically, find at least one other column that the missingness of your selected column **does** depend on, and at least one other column that the missingness of your selected column **does not** depend on.<br><br>***Tip***: Make sure you know the difference between the different types of missingness before approaching that section. Many students in the past have lost credit for mistaking one type of missingness for another. | Present and interpret the results of your missingness permutation tests with respect to your data and question. Embed a `plotly` plot related to your missingness exploration; ideas include:<br>• The distribution of column $$Y$$ when column $$X$$ is missing and the distribution of column $$Y$$ when column $$X$$ is not missing, as was done in [Lecture 12](https://dsc80.com/resources/lectures/lec12/lec12.html).<br>• The empirical distribution of the test statistic used in one of your permutation tests, along with the observed statistic. |

### Requirement: Hypothesis Testing

| Step | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Hypothesis Testing** | Clearly state a pair of hypotheses and perform a **hypothesis test or permutation test** that is not related to missingness. Feel free to use the "sample questions" in each of the dataset descriptions or create your own. This should be the question that is stated clearly at the top of your report. | Clearly state your null and alternative hypotheses, your choice of test statistic and significance level, the resulting $$p$$-value, and your conclusion. Justify why these choices are good choices for answering the question you are trying to answer.<br><br>***Optional***: Embed a visualization related to your hypothesis test in your website.<br><br>***Tip***: When making writing your conclusions to the statistical tests in this project, **never** use language that implies an absolute conclusion; since we are performing statistical tests and not randomized controlled trials, we cannot prove that either hypothesis is 100% true or false.<br><br>_“Only a Sith deals in absolutes” - Obi-Wan Kenobi_ | 

### Style

While your website will neatly organized and tailored for public consumption, it is important to keep your analysis notebook organized as well. Follow these guidelines:
* Your work for each of the three project sections (Cleaning and EDA, Assessment of Missingness, and Hypothesis Testing) described above should be completed in code cells underneath the Markdown header of that section's name.
* You should **only include work that is relevant** to posing, explaining, and answering the question(s) you state in your report. You should include data quality, cleaning, and missingness assessments, though these should broadly be relevant to the question at hand.
* Make sure to clearly explain what each component of your notebook **means**. Specifically:
    - All plots should have titles, labels, and a legend (if applicable), even if they don't make it into your website. Plots should be self-contained – readers should be able to understand what they describe without having to read anything else.
    - All code cells should contain a comment describing how the code works (unless the code is self-explanatory – use your best judgement).

---

## Part 2: Report

The purpose of your website is to provide the general public – your classmates, friends, family, recruiters, and random internet strangers – with an overview of your project and its findings, without forcing them to understand every last detail. We don't expect the website creation process to take very much time, but it will certainly be rewarding. Once you've completed your analysis and know _what_ you will put in your website, start reading this section.

Your website must clearly contain four headings:
- Introduction
- Cleaning and EDA
- Assessment of Missingness
- Hypothesis Testing

The specific content your website needs to contain is described in the "Report on Website" columns above. Make sure to also give your website a creative title that relates to the question you're trying to answer, and clearly state your name(s).

Your report will be in the form of a _static_ website, hosted for free on GitHub Pages. More specifically, you'll use [Jekyll](https://jekyllrb.com), a framework built into GitHub Pages that allows you to create professional-looking websites just by writing Markdown ([dsc80.com](https://dsc80.com) is built using Jekyll!). GitHub Pages does the "hard" part of converting your Markdown to HTML.

If you'd like to follow the official [GitHub Pages & Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll) tutorial, you're welcome to, though we will provide you with a perhaps simpler set of instructions here. A very basic site with the required headings and one embedded visualization can be found at [rampure.org/dsc80-proj3-test1/](http://rampure.org/dsc80-proj3-test1/); the source code for the site is [here](https://github.com/surajrampure/dsc80-proj3-test1).

### Step 1: Initializing a Jekyll GitHub Pages Site

1. Create a GitHub account, if you don't already have one.
1. Create a new GitHub repository for your project.
    - GitHub Pages sites live at `<username>.github.io/<reponame>` (for instance, the site for [github.com/dsc-courses/dsc80-2023-sp](https://github.com/dsc-courses/dsc80-2023-sp) is [dsc-courses.github.io/dsc80-2023-sp](https://dsc-courses.github.io/dsc80-2023-sp)).
    - As such, **don't** include "DSC 80" or "Project 3" in your repo's name – this looks unprofessional to future employers, and gives you a generic-sounding URL. Instead, mention that this is a project for DSC 80 at UCSD in the repository description.
    - **Make sure to make your repository public.**
    - Select "ADD a README file." This ensures that your repository starts off non-empty, which is necessary to continue.
1. Click "Settings" in the repository toolbar (next to "Insights"), then click "Pages" in the left menu.
1. Under "Branch", click the "None" dropdown, change the branch to "main", and then click "Save." You should soon see "GitHub Pages source saved." in a blue banner at the top of the page. This initiates GitHub Pages in your repository.
1. After 30 seconds, reload the page again. You should see "**Your site is live at http://username.github.io/reponame/**". Click that link – you now have a site!
1. Click "Code" in the repo toolbar to return to the source code for your repo.

Note that the source code for your site lives in `README.md`. **As you push changes to `README.md`, they will update on your site automatically within a few minutes!** Before moving forward, make sure that you can make basic edits:
1. Clone your repo locally.
1. Make some edits to `README.md`.
1. Push those changes back to GitHub, using the following steps:
    - Add your changes to "staging" using `git add README.md` (repeat this for any other files you add).
    - Commit your changes using `git commit -m '<some message here>'`, e.g. `git commit -m 'changed title of website'`.
    - Push your changes using `git push`.

Moving forward, we recommend making edits to your website source code locally, rather than directly on GitHub. This is in part due to the fact that you'll be creating folders and adding files to your source code.

### Step 2: Choosing a Theme

The default "theme" of a Jekyll site is not all that interesting.

To change the theme of your site:
1. Create a file in your repository called `_config.yml`.
1. Go [here](https://pages.github.com/themes/), and click the links of various themes until you find one you like.
1. Open the linked repository for the theme you'd like to use and scroll down to the "Usage" section of the README. Copy the necessary information from the README to your `_config.yml` and push it to your site.

For instance, if I wanted to use the Merlot theme, I'd put the following in my `_config.yml`:

```yml
remote_theme: pages-themes/merlot@v0.2.0
plugins:
- jekyll-remote-theme # add this line to the plugins list if you already have one
```

Note that you're free to use any Jekyll theme, not just the ones that appear [here](https://pages.github.com/themes/). You are required to choose _some_ theme other than the default, though. See more details about themes [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll).

### Step 3: Embedding Content

Now comes the interesting part – actually including content in your site. The [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) contains tips on how to format text and other page components in Markdown (and if you'd benefit by seeing an example, you could always look at the Markdown source of [this very page](https://raw.githubusercontent.com/dsc-courses/dsc80-2023-sp/gh-pages/project3/index.md) – meta!).

What will be a bit trickier is embedding `plotly` plots in your site so that they are interactive. Note that you are **required** to do this, you cannot simply take screenshots of plots from your notebooks and embed them in your site. Here's how to embed a `plotly` plot directly in your site.
1. First, you'll need to convert your plot to HTML. If `fig` is a `plotly` `Figure` object (for instance, the result of calling `px.express`, `go.Figure`, or `.plot` when `pd.options.plotting.backend = "plotly"` has been run), then the method `fig.write_html` saves the plot as HTML to a file. Call it using `fig.write_html('file-name.html', include_plotlyjs='cdn')`.
    - Change `'file-name.html'` to the path where you'd like to initially save your plot.
    - `include_plotlyjs='cdn'` tells `write_html` to load the source code for the `plotly` library from a server, rather than including the entire source code in your HTML file. This drastically reduces the size of the resulting HTML file, keeping your repo size down.
1. Move the `.html` file(s) you've created into a folder in your website repo called `assets` (or something similar).
    - Depending on where your template notebook is saved, you could combine this step with the step above by calling `fig.write_html` with the correct path (e.g. `fig.write_html('../league-match-analysis/assets/matches-per-year.html')).
1. In `README.md`, embed your plot using the following syntax:

```html
<iframe src="assets/file-name.html" width=800 height=600 frameBorder=0></iframe>
```
- `iframe` stands for "inline frame"; it allows us to embed HTML files within other HTML files.
- You can change the `width` and `height` arguments, but don't change the `frameBorder` argument.

Refer [here](https://github.com/surajrampure/dsc80-proj3-test1) for a working example.

{: .note }
Try your best to make your plots look professional and unique to your group – add axis labels, change the font and colors, add annotations, etc. Remember, potential employers will see this – you don't want your plots to look like everyone else's!

To convert a DataFrame in your notebook to Markdown source code (which you need to do for both the **Data Cleaning** and **Interesting Aggregates** sections of the cleaning and EDA requirement), use the `.to_markdown()` method on the DataFrame. For instance,

```py
print(counts[['Quarter', 'Count']].head().to_markdown(index=False))
```

displays a string, containing the Markdown representation of the first 5 rows of `counts`, including only the `'Quarter'` and `'Count'` columns (and not including the index). You can see how this appears [here](http://rampure.org/dsc80-proj3-test1/#assessment-of-missingness); remember, no screenshots.

### Local Setup

The above instructions give you all you need to create and make updates to your site. However, you _may_ want to set up Jekyll locally, so that you can look at how changes to your site would look without having to push and wait for GitHub to re-build your site. To do so, follow the steps [here](https://jekyllrb.com/docs/installation/) and then [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).

---

## Submission and Rubric

### Submission

You will submit your project in two ways:
1. By uploading a **PDF version** of your notebook to the specific "Project 3 Notebook PDF (Dataset)" assignment on Gradescope **for your dataset**.
    - To export your notebook as a PDF, first, restart your kernel and run all cells. Then, go to "File > Print Preview". Then, save a print preview of the webpage as a PDF. There are other ways to save a notebook as a PDF but they may require that you have additional packages installed on your computer, so this is likely the most straightforward.
    - It's fine if your `plotly` graphs don't render in the PDF output of your notebook.
    - This notebook asks you to include a link to your website; make sure to do so.
2. By submitting a **link to your website** to the "Project 3 Website Link (All Datasets)" assignment on Gradescope.

To both submissions, make sure to tag your partner. You don't need to submit your actual `.ipynb` file anywhere. **While your website must be public and you should share it with others, you should _not_ make your code for this project available publicly.**

Since there are two assignments you need to submit to on Gradescope, we will treat your submission time as being the **latter** of your two submissions. So, if you submit to the "Project 3 Notebook PDF" assignment before the deadline but to the "Project 3 Website Link (All Datasets)" website one day late, overall, you will be charged a slip day.

{: .warning }
There are a lot of moving parts to this assignment – don't wait until the last minute to try and submit!

### Rubric

Your project will be graded out of 100 points. The rough rubric is shown below. If you satisfy these requirements as described above, you will receive full credit.

| Component | Weight |
| --- | --- |
| Provided an introduction to the dataset and the analyses  | 8 points |
| Cleaned data | 8 points |
| Performed univariate analyses  | 8 points |
| Performed bivariate analyses and aggregation  | 8 points |
| Addressed NMAR question | 4 points|
| Performed permutation tests for missingness  | 8 points|
| Interpreted missingness test results  | 8 points|
| Selected relevant columns for a hypothesis or permutation test  | 4 points|
| Explicitly stated a null hypothesis  | 4 points|
| Explicitly stated an alternative hypothesis  | 4 points|
| Performed a hypothesis or permutation test  | 8 points|
| Used a valid test statistic  | 4 points|
| Computed a p-value and made a decision  | 4 points|
| Included all necessary components on the website | 20 points |
| **Total** | **100 points** |

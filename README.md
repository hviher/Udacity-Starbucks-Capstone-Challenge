<h2 align="center">Udacity Data Scientist Nanodegree Program Project 1</h2>

<h3 align="center">Starbucks-Capstone-Challenge</h3>

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#project_motivation)
3. [File Descriptions](#file_description)
4. [Findings](#findings)
5. [Licensing, Authors, Acknowledgments](#licensing)

## Installation <a name="installation"></a>
There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

## Project Motivation <a name="project_motivation"></a>
My motivation for this project was to complete the 'Data Scientist Capstone project' for the Data Scientist Nanodegree Program.  For this project I chose the Starbucks Capstone Challenge.  For this project, Starbucks provided data that contained simulated data that mimics it's customer behavior on the Starbucks reward mobile app.  Once every few days Starbucks will send out an offer to it's mobile app users which can be in the form of a reward or simply an advertisement for a product. I will use this data to identify which demographic groups are most responsive to each type of offer.

## File Descriptions <a name="file_descriptions"></a>
This repository contains a Jupyter Notebook (Starbucks_Capstone_notebook.ipynb) that showcases the work related to this project. The notebook is an exploratory analysis of the data to answer the question above. Markdown cells were used to assist in walking through the thought process for individual steps.

There were three data files provided for this project.  The three files were:
- `portfolio.json` - containing offer ids and meta data about each offer (duration, type, etc.)
- `profile.json` - demographic data for each customer
- `transcript.json` - records for transactions, offers received, offers viewed, and offers completed
  
portfolio metadata:
- id (string) - offer id
- offer_type (string) - type of offer ie BOGO, discount, informational
- difficulty (int) - minimum required spend to complete an offer
- reward (int) - reward given for completing an offer
- duration (int) - time for offer to be open, in days
- channels (list of strings)
  
profile metadata:
- age (int) - age of the customer
- became_member_on (int) - date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income

transcript metadata:
- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since start of test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record

## Findings <a name="findings"></a>
The main findings of the analysis can be found at the post available [here](https://hrviher.medium.com/optimizing-app-offers-with-starbucks-a32d802cd670).

## Licensing, Authors, Acknowledgments <a name="licensing"></a>
Must give credit to Udacity and Starbucks for the data.

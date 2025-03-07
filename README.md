# 📊 MAP - Marketing ADS Predictor

MAP is an educational project made for Zurich x Generation that analyzes and predict campaign sales using different types of media.\
This tool is designed to help businesses optimize their advertising investments by leveraging machine learning techniques.

## Project request

> The project requires the analysis of a dataset (Advertising_modified.csv) containing information on investments in advertising campaigns, categorized into TV, Radio, and Newspaper campaigns.
The goal of the project is to identify potential correlations between the different campaigns, determine which marketing strategies (TV, Radio, and/or Newspaper) lead to the highest sales increase, and develop a machine learning algorithm based on regression to predict sales projections based on a given investment in one or more of these strategies.
Finally, the project should be documented by creating a report using a Python notebook (.ipynb).

📂 You can read and check the .csv file [at this link](https://drive.google.com/file/d/1Wc-Sd3K2FjpfbUFHPabOoDTl2PM1fEco/view?usp=sharing)

## Installation

To install MAP and run the program, you can use your bash console:

```
git clone https://github.com/matteobpunto/MAP_marketing_ads_predictor.git  
cd MAP_marketing_ads_predictor  
pip install -r requirements.txt  
python main.py
```

## Program languages and utility tools

🐍 Python as main program language (to extend, we used powerful libraries such as [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/) for data visualization) for various queries;\
🐒 MongoDB as non-relational database platform (this was used only for an educational purpose);\
🐳 MySQL (in particular, MariaDB) as relational database platform to manage different datasets.

## How it works

MAP is a standalone application built using Python as program language, one of the best tool for its flexibility, spreadability and simplicity as well.\
Using MAP you will be able to show how your investments in advertising will be perceived by your audience according to previous results.

## Data Cleaning

A Python script for data cleaning is available in the 'data_cleaning' directory. This script removes null values
from the dataset, ensuring data consistency before analysis and model training

## Machine Learning

We implemented a regression-based Machine Learning model to predict sales outcomes based on advertising investments.
The model was trained using [scikit-learn](https://scikit-learn.org/stable/)

## Power BI

We developed a **Power BI dashboard** to provide interactive data visualization and insights. The dashboard includes:
- Sales trend analysis
- Correlation between investments and revenue
- Predictive analysis based on the trained Machine Learning model

## Website development

A **web-based interface** was created to make MAP more accessible and user-friendly. The website was built
using **Flask (backend) and HTML/CSS (frontend)**, allowing users to:
- Upload their own advertising investment data
- View dynamic visualizations
- Access Machine Learning predictions in real-time

## Notebook

A **Google Colab Notebook (.ipynb)** was added to the project, containing scripts to:
- Create a **MySQL database** to store advertising campaign data
- Inserte and manage datasets efficiently
- Perform SQL queries for data retrieval and analysis (C.R.U.D. operations)

## Credits

This project was made by Matteo Balestra, Oleksandr Butko, Davide Ghidelli, Alice Monti, Anna Occoffer and Alessandro Terrazzano.
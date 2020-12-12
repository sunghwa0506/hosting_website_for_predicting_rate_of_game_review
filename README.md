### This website will take user input for game reviews and return predicting rate based on dictionary built from https://www.kaggle.com/jvanelteren/boardgamegeek-reviews?select=bgg-15m-reviews.csv
### This website is hosting on pythonanywhere

## Libraries used:
from flask import Flask, redirect, url_for, request, render_template  
import re  
import string  
import pandas as pd  
import nltk  
from nltk.corpus import stopwords  

You might need to download nltk stopwords.  
Please use this command nltk.download('stopwords') on pythonanywhere console if you get an NLTK error.   

## Edit WSGI.py
Login pythonanywhere -> Web -> code -> WSGI configuration file  
The defalt setting is "from flask_app import app as application"  
Please change flask_app to corresponding .py file for your website  

## Download directory folder from my github
This folder contains preprocessed data.  
There are 11 CSV files. Each files have words and number of time the words appear in that rate.  
For example, word_all_rate.csv has a word "game" and it appears 2269345 times in the total reviews from rate 1 to 10.  
The word "game" presents 20131 times in rate 1 reviews.  

## Download templates folder from my github  
Templates folder has html files. 

## Import directory and templates forders to pythonanywhere

## Ready to deploy your website


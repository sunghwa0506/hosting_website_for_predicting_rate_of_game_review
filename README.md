# This website will take user input for game reviews and return predicting rate based on dictionary built from https://www.kaggle.com/jvanelteren/boardgamegeek-reviews?select=bgg-15m-reviews.csv


## Libraries used:
from flask import Flask, redirect, url_for, request, render_template
import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:51:23 2020

@author: dchidraw

Command to run below program: runfile('prices.py', args='MFST', wdir='C:\Datta\Personal\HBA Program\Jan 2020\PDSS\Week 4\Assignment 4')
"""


import csv
import requests
import sys

# Used Spyder instead ATOM hence the message is different below
if len(sys.argv) != 2:
    sys.exit("Usage: runfile('prices.py', args='SYMBOL', wdir='C:\Datta\Personal\HBA Program\Jan 2020\PDSS\Week 4\Assignment 4')")
symbol = sys.argv[1]

API_KEY = "P3J3SL3A90NPAYNM"

if not API_KEY:
    sys.exit("Missing API_KEY")

url = f"https://www.alphavantage.co/query?apikey={API_KEY}&datatype=csv&function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full"
response = requests.get(url)

# Parse CSV
reader = csv.DictReader(response.text.splitlines())

for row in reader:   
    print(f"${row['timestamp']} {row['close']}")

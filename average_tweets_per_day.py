from datetime import datetime as dt
from dateutil import parser
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

days = []
all_days = {}

with open("tweet.js", 'r') as f:
	text = f.read().split('=', 1)[1].lstrip()

data = json.loads(text)
for tweet in data:
	date = parser.parse(tweet["tweet"]["created_at"], fuzzy=True)
	days.append(date.strftime("%Y-%m-%d"))

counter = dict(Counter(days).items())
counts = counter.values()
print(sum(counts) / len(counts))

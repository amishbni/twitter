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

counter = Counter(days).items()
counterl = list(counter)
counterd = dict(counter)
sorted_days = sorted(counterl, key= lambda x: dt.strptime(x[0], "%Y-%m-%d"))
sdate = dt.strptime(sorted_days[0][0], "%Y-%m-%d")
edate = dt.strptime(sorted_days[-1][0], "%Y-%m-%d")
days_range = pd.date_range(sdate,edate, freq='d')
months_range = pd.date_range(sdate, edate, freq='m')
for day in list(pd.Series(days_range.format())):
	if day in counterd:
		all_days[day] = counterd[day]
	else:
		all_days[day] = 0

fig, ax = plt.subplots()
ax.plot(list(all_days.keys()), list(all_days.values()))
ax.set_title("Tweets Rate - Daily")
ax.set_ylabel("Number of tweets")
ax.set_xticks(list(pd.Series(months_range.format())))
ax.tick_params(axis='x', labelrotation=90, labelsize=7)
fig.tight_layout()
fig.savefig("plot.png", dpi=200)


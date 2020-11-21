from datetime import datetime as dt
from dateutil import parser
from collections import Counter
import matplotlib.pyplot as plt
import json

days = []

with open("tweet.js", 'r') as f:
	text = f.read().split('=', 1)[1].lstrip()

data = json.loads(text)
for tweet in data:
	date = parser.parse(tweet["tweet"]["created_at"], fuzzy=True)
	days.append(date.strftime("%Y-%m-%d"))

counter = list(Counter(days).items())
day_freq = sorted(counter, key= lambda x: dt.strptime(x[0], "%Y-%m-%d"))
x, y = zip(*day_freq)

plt.figure()
plt.plot(list(x), list(y))
plt.title("Tweets Rate - Daily")
plt.xlabel("Days")
plt.ylabel("Number of tweets")
plt.xticks([], [])
plt.savefig("plot.png", dpi=200)

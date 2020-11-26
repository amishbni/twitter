from collections import Counter
import pandas as pd
import json

with open("tweet.js", 'r') as f:
    text = f.read().split('=', 1)[1].lstrip()

data = json.loads(text)
ids = []

for tweet in data:
    if "in_reply_to_user_id" in tweet["tweet"]:
        ids.append(tweet["tweet"]["in_reply_to_user_id"])

counter = Counter(ids)
print(len(counter))

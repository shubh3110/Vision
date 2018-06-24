import json
import sqlite3
import time
from datetime import datetime

total_posts = json.load(open('posts.json'))
db = sqlite3.connect("flaskblog/site.db")

for data in total_posts:
    c = db.cursor()
    date=datetime.utcnow()
    c.execute("INSERT INTO post (title, date_posted, content, user_id) VALUES (?, ?, ?, ?)",(data["title"], date, data["content"], data["user_id"]))
    cnt=cnt+1
    db.commit()

db.close()
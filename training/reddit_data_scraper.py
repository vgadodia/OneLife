import praw
import csv

reddit = praw.Reddit(client_id='_CYcLKpr91gSGw', client_secret='2g-RHmbHyeRtj-FE_O3V8ieTEoc', user_agent='webscraper123', username='webscraper123', password='webscraper123')


def process(k):
    x = k.lower()
    final = ""

    for i in x:
        if i.isalpha() == False and i != " ":
            if i == "'":
                continue
            else:

                final += " "
        else:
            final += i 

    return final 

def get_raw_text(a, b):
    final = ""
    for i in (a + " " + b).splitlines():
        final += process(i) + " "

    return final


subreddit = reddit.subreddit('SuicideWatch')
top_subreddit = subreddit.top(limit = 1000)


file = open('data.csv', 'w', newline='')
writer = csv.writer(file)

writer.writerow(["text", "label"])

for i in top_subreddit:
    x = i.title
    y = i.selftext
    writer.writerow([get_raw_text(x, y),"1"])

subreddit1 = reddit.subreddit('depression')
top_subreddit1 = subreddit1.top(limit = 1000)

for i1 in top_subreddit1:
    x1 = i1.title
    y1 = i1.selftext
    writer.writerow([get_raw_text(x1, y1),"1"])

subreddit2 = reddit.subreddit('CasualConversation')
top_subreddit2 = subreddit2.top(limit = 1000)

for i2 in top_subreddit2:
    x2 = i2.title
    y2 = i2.selftext
    writer.writerow([get_raw_text(x2, y2),"0"])

subreddit3 = reddit.subreddit('socialskills')
top_subreddit3 = subreddit3.top(limit = 1000)

for i3 in top_subreddit3:
    x3 = i3.title
    y3 = i3.selftext
    writer.writerow([get_raw_text(x3, y3),"0"])

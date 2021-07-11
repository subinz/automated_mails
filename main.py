import yagmail
import pandas
from news import NewsFeed
import datetime

# second testing of commit
# second line
df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                         to_date=datetime.datetime.now().strftime('%Y-%m-%d'))


    email = yagmail.SMTP(user="yourmail@domain.com", password='password')

    email.send(to=row['email'], subject=f"Your {row['interest']} news for today!",
                      contents=f"Hi {row['name']}\n\n See what's on about {row['interest']} today.\n{news_feed.get()} \nSparrowz Tech",)
    # print(row)
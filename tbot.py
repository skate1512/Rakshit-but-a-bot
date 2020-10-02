import praw
from tmsg import TelegramBot
import os


bot = TelegramBot()
print("Running")
reddit = praw.Reddit(client_id=os.environ.get('CI'),
                     client_secret=os.environ.get('CS'),
                     username=os.environ.get('usr'),
                     password=os.environ.get('Password'),
                     user_agent='find_me_posts')

reddit.read_only = True

subreddits = "Python+Check_your_bot+learnpython+madeinpython"
for submission in reddit.subreddit(subreddits).stream.submissions():
    if any(keyword in submission.title for keyword in ["project", "made",  "created", "implemented", "collaborate","automation", "automate", "script"]):
        send_this = str(submission.subreddit) + "-" + submission.title
        post_link = "\nhttps://www.reddit.com" + submission.permalink
        bot.send_it(send_this, post_link)
        

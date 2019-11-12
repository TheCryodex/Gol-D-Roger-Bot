import praw
import pdb
import re
import os

#Create reddit Instance: 
reddit = praw.Reddit('bot1')

#Maintains a file to keep track of replies already made

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", 'r') as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))
		
subreddit = reddit.subreddit('Onepiece')

for submission in subreddit.hot(limit=5):
	if submission.id not in posts_replied_to:
		if re.search("Gold Roger", submission.title, re.IGNORECASE):
			submission.reply("My name is Gol D. Roger")
			print("Bot replying to : ", submission.title)
			
			posts_replied_to.append(submission.id)
			
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")


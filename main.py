import smtplib
from email.message import EmailMessage
import praw

from datetime import datetime
from pytz import timezone

# list of regular expressions in separate python file (might get kinda long)
import regex_list

# Reddit API and account info
import settings

# NLP library flair
from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('sentiment')



# initialize Reddit API and account info
reddit = settings.reddit_init()
# specify subreddit - monitoring the USC subreddit here
subreddit = reddit.subreddit("USC")

# # not finished - initialize slackbot with slackbot_init()
#

# write to file (probably shouldn't declare it here, will fix later)
file = open('posts.md', 'w+')

# format the timestamp of Reddit post/comment
def print_convert_timestamp(utc):

	date_format = '%Y-%m-%d %H:%M:%S'
	time_stamp_utc = datetime.fromtimestamp(utc)
	time_stamp_pst = time_stamp_utc.astimezone(timezone('US/Pacific'))
	time_formatted = time_stamp_pst.strftime(date_format)
	return time_formatted

def send_email():

    email_file = open('posts.md', 'r')

    email = EmailMessage()
    email["From"] = "email@email.com"
    email["Subject"] = "r/USC"
    email["To"] = ['email@email.com', 'email2@email.com'] 

    email.set_content(email_file.read()) # body of email

    smtpObj = smtplib.SMTP('yourmailserver.com')
    smtpObj.send_message(email)         
    print("sent email with Reddit posts")

# print a Reddit post's title and body
def post_printing_format(submission):

	# print to terminal
	if __debug__:
		print(submission.title)
		print("---")
		print(submission.selftext)
		print("---")
		print(submission.url)
		# timestamp for Post
		timestamp = print_convert_timestamp(submission.created_utc)
		print(timestamp)

		print()
		print()
	

    # write to file for email - clean this up 
	# this will be irrevelant once I implement the slack bot
	file.write("---------------------------------------------------------------------------------------------------------\n")
	try:
		file.write(submission.title)
	except: 
		print("An exception occured when reading the title of the post (likely an emoji). Post ID: " + submission.id)
	file.write("\n")
	file.write("---\n")
	try:
		file.write(submission.selftext)
	except: 
		# sometimes there are emojis in posts, find a better way to handle this
		print("An exception occured when reading the body of a post (likely an emoji). Post ID: " + submission.id)
	file.write("\n")
	file.write("---\n")
	file.write(submission.url)
	file.write("\n")
	file.write("\n")
	timestamp = print_convert_timestamp(submission.created_utc)
	file.write(timestamp)
	file.write("---------------------------------------------------------------------------------------------------------\n")
	file.write("\n")
	file.write("\n")
	file.write("\n") 






def flagged_posts():

	# pull regexes from regex_list.py 
	regexes = regex_list.pull_regexes() 
	# check if they are actually compiled before hitting the below if statement
	# think they aren't, so maybe compile each and place into new list?

	# when I finish program and set main.py to scan subreddit every ~5 minutes, decrease this limit
	for submission in subreddit.new(limit=100): 

		if (any(regex.search(submission.title) for regex in regexes) 
				or any(regex.search(submission.selftext) for regex in regexes)):

			# NLP - not yet using it to filter, only displaying the results
			
			sentence_body = Sentence(submission.selftext) #post body
			sentence_title = Sentence(submission.title) #post title

			# positive or negative classification
			classifier.predict(sentence_body) 
			print("sentiment analysis on post body: " + str(sentence_body.labels)) 
			file.write("sentiment analysis on post body: " + str(sentence_body.labels))
			file.write("\n")

			classifier.predict(sentence_title) 
			print("sentiment analysis on post title: " + str(sentence_title.labels)) 
			file.write("sentiment analysis on post title: " + str(sentence_title.labels))
			file.write("\n")

			# naive approach: return all posts that match regexes
			post_printing_format(submission)
    
	file.close()

			

def top_posts(lim):

	# time filter can be: all, day, hour, week, month, year
	# limit is number of posts returned

	for submission in subreddit.top("day", limit=lim):
		post_printing_format(submission)



def main():
    

	# current naive approach: return all posts that match your regexes in regex_list.py
	# soon: add some sentiment analysis with the NLP library Flair to further filter results
	#  ---- (if a post matched a regex but is "happy" and not "angry", don't include it in the return set)
	flagged_posts()

	# # Perhaps use as a Daily Digest, return top posts via slackbot every evening at 7pm?
	# top_posts(5)

	# if you have a mail server, you can send update emails with the top_posts() or flagged_posts() content
	send_email()
    

    

if __name__ == "__main__":
	main()

import praw

def reddit_init():

    #replace these with your Reddit API info and Reddit account credentials

    reddit_settings = praw.Reddit(
        client_id = "",
        client_secret = "",
        user_agent = "",
        username = "",
        password = "",
    )

    return reddit_settings

def slackbot_init():

    # to do
    print()
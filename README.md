# reddit-alerts
Monitor a subreddit with regular expressions and NLP-based filtering 

## Requirements
Using a virtual environment in an Anaconda Prompt is a good way to simplify Python package management and deployment. For reddit-alerts, you will need Python 3.6+. [Here is a link](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) that can help you set up Anaconda and Python. If you have a preferred package management tool, feel free to use that instead.

Creating and entering a virtual environment in Anaconda:

```
conda create --name reddit python=3.6
conda activate reddit
```

The Natural Language Processing (NLP) framework [Flair](https://github.com/flairNLP/flair) is based on Python 3.6 but has support for higher versions. If you prefer to use a higher version of Python, that should be fine.

The following dependencies are required:

```
pip install praw
pip install pytz
pip install flair
```

Praw has good documentation on using the Reddit API. Here is their [Quick Start guide](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html). We will be using an OAuth authentication method called [Password Flow](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow). 

Collect the necessary information - Client ID, Client Secret, User Agent, and the username and password of a Reddit account - and paste it into the fields in the reddit_init() function in settings.py. Avoid displaying your Reddit account and API credentials in a public repository - don't push your completed settings.py!

## Example Usage
This project isn't finished yet. Here's what it does for now.

Run the program with the below command:

```
py -O main.py
```

Currently, the function flagged_posts() in main.py will output posts that match the regexes in regex_list.py, and display the sentiment analysis of the post body and title (positive/negative). This information will be placed in posts.txt. There is a posts.txt file in this repository if you would like to view an example.

If you run the below command omitting the -O flag, the output will be displayed in the terminal in addition to in posts.txt.

```
py main.py
```

## Development
- Integrate with Slack, rather than sending updates via email
- Find more regular expressions related to service issues
  - Use these regexes in combination with others, something like 'blackboard AND (outage OR \bdown\b OR error OR ......)'
- Decide how to use the NLP sentiment analysis data to filter and report posts based on displayed negativity


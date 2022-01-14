# reddit-alerts
Monitor a subreddit with regular expressions and NLP-based filtering 

#### Requirements
Using a virtual environment in an Anaconda Prompt is a good way to simplify Python package management and deployment. For reddit-alerts, you will also need Python 3.6+. [Here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) is a link that can help you set up Anaconda and Python. If you have a preferred package management tool, feel free to use that instead.

Creating and entering a virtual environment in Anaconda:

'''
  > conda create --name reddit python=3.6
  > conda activate reddit
'''

The Flair library is based on Python 3.6 but has support for higher versions. If you prefer to use a higher version, that should be fine.

Then install the following dependencies:

'''
  > pip install praw
  > pip install pytz
  > pip install flair
'''



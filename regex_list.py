import re


def pull_regexes():

    return [

    # the purpose of this program - identify service-related issues!
    # this is just a sample
    # to do: test more specific matches like: 'blackboard AND (outage OR \bdown\b OR error OR ......)'
    re.compile(r'\bwifi\b', re.I), 
    re.compile(r'outage', re.I),
    re.compile(r'blackboard', re.I),

    # # three digit number, will return a lot of results (good for testing)
    # # i.e. Physics 151, BUAD 304, CSCI 102
    # re.compile(r'\b[0-9]{3}\b') 

    # # also good for testing
    # re.compile(r'class', re.I)
    # re.compile(r'COVID', re.I),

    ]
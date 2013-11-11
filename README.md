hattai-fortune
==============

Hattai's Fortune: a script to be used by a bot, that gives news (from Público)

Build status: [![Build Status](https://travis-ci.org/nunonunes/hattai-fortune.png?branch=master)](https://travis-ci.org/nunonunes/hattai-fortune)

## Script's behaviour

This is the behaviour of the script, as extracted from the previous implementation.


When run the script will:

1. Read the RSS feed of the Público newspaper
   (http://http://feeds.feedburner.com/publicoRSS)
2. Exclude the articles which contain any word from a given list of "bad words"
   (the match is case **insensitive**)
3. Exclude articles which have an empty title
4. Add new articles to the article list
5. Trim the article list up to a given maximum size
6. Pick the "best" article from the article list and:
    1. Store the title in a file called _title_
    2. Store the URL in a file called _link_
    3. Print out the title to STDOUT
7. Save the current article list for the next run


The way the "best article" is chosen is roughly like this:

- Look for the articles which have been used the least (ideally never)
- Pick the most recent one

We assume the feed delivers the articles ordered by date, so no check is done on the script.

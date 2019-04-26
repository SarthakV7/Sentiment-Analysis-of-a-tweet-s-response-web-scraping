# Sentiment-Analysis-of-a-tweet-s-response-web-scraping
Sentiment analysis of the comments on a tweet by web scraping using Selenium, bs4, NLTK (Vader) and Regular Expressions.

#### Libraries used-
 - Selenium (Automation tool)
 - bs4 (BeautifulSoup)
 - re (Regular Expressions)
 - matplotlib.pyplot
 - nltk (nltk.sentiment.vader)

#### Algorithms used-
 - Sentiment Intensity Analyzer (NLTK)
 
#### Summary-
 - The program uses selenium webdriver to scroll through the twitter comments, then it gathers the wabpage data and uses buautifulSoup to
   extract the comments. The comments are filtered of any unwanted data using RegEx and then stored in a list and are passed through 
   Sentiment Intensity Analyzer that returns the "polarity-score" of the comments and using the polarity scores the overall sentiment of 
   the tweet's response is calculated.
   
#### Explaining a few steps-
 - The program asks for a 'url' as input: The url should be copied from the page after selecting the tweet such that the page that is 
       opened has comments visible on scrolling. (Checkout the 'how to copy url.gif' file attached).
 - The program asks for the number of comments to process: The input will decide the number of comments to be selected for analyzing
       the data and producing a response, note that 'n' number of comments will be selected from top to bottom.
       
#### Note-
 - The Sentiment Intensity Analyzer library of NLTK is one among the best for Sentiment Analysis but it still has some issues detecting
   sarcastic comments or words that are unavailable in the librariy like emoji etc. So it should be kept in mind that the output can be
   unexpected at times.

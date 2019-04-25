from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url = input('paste the twitter url here: ')

num = int(input('Enter the number of comments to process: '))

driver = webdriver.Chrome()

def scroll(n):
    t,i = 1, 1
    while(i<n):
        driver.execute_script("window.scrollBy(0, 5000);")
        print(" --------- please wait ---------  ")
        time.sleep(3)
        t+=1

        html = driver.page_source
        soupeddata = BeautifulSoup(html, "html.parser")
        tw_links = soupeddata.find_all("li", class_ = "ThreadedConversation--loneTweet")

        i = len(tw_links)
    print('completed!!')
    return tw_links

driver.get(url)

tw_links = scroll(num)

total = len(tw_links)
if(total > num):
    total = num
    tw_links = tw_links[:num]

pattern = r"twitter.com"
r = []
for x in tw_links:
    ep = x.find("p", class_ = "TweetTextSize")
    text = ep.text.strip()
    d = re.findall(pattern, text)
    if len(d):
        continue
    r.append(text)

sid = SentimentIntensityAnalyzer()

pol = []
po = []
for a in r:
    score = sid.polarity_scores(a)
    comp = score['compound']
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if(comp >= 0):
        if(pos >= neu - 0.1):
            pol.append('positive')
        else:
            pol.append('negative')
    else:
        pol.append('negative')
    po.append(score)

pos_num, neg_num = 0,0
for e in pol:
    if e == 'positive':
        pos_num += 1
    elif e == 'negative':
        neg_num += 1
unprocessed = total - (pos_num + neg_num)

labels = 'Positive', 'Unprocessed', 'Negative'
data = [pos_num, unprocessed, neg_num]

print('\n\n')

for i,k in enumerate(r):
    print (i+1,': ',k)

print('\n\n')

for i,k in enumerate(labels):
    print (k,': ',data[i])

print('\n\n')

explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Unprocessed')

fig1, ax1 = plt.subplots(figsize = (8, 8))
ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=120)
plt.xlabel("\nPercentage representation of the reviews!")
plt.legend(labels)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

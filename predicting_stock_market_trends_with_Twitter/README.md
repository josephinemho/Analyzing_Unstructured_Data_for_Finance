# Taking the Tweets of 30 thought leaders to predict the NASDAQ-100 Technology Sector Index (NDXT) 


## Outline
shows all the topics that were discussed, the sentiment around them, and how these two things related to stock changes?

Over a 5 day period, we collected about 77,000 tweets about the Web Summit 2015 using the Twitter Streaming API and in this blog series, we're going to explore them and see what we can extract.
Note: This is a step by step guide which contains all you need to accomplish (almost) the same results, so feel free to try it for yourself by forking the Jupyter notebook from our GitHub repository.



In the first part of this series, we're going to build a 2D map of the tweets that we've collected, to get a better sense of what people talked about at a high level. We're going to try and put the similar tweets closer together on this map, and the dissimilar ones further apart.
We'll try out a few different methods such as classical document vectors with tf-idf scoring, K-means clustering, Latent Dirichlet Allocation (LDA), averaged Word Vectors (using GloVe word embeddings), Paragraph Vectors (using gensim's doc2vec implementation) and finally Skip-Thought Vectors to group together similar tweets, and we will then use a dimensionality reduction algorithm called t-SNE to give each tweet an (x,y) co-ordinate in a 2D space, that allows us to put the tweets on a scatter plot.



* There are many articles on Tweets predicting/reflecting stock market:
    * A famous study tied 6 dimensions of "mood" (based on GPOMS) to the stock market. Their mood dimension were: Calm, Alert, Sure, Vital, Kind and Happy. But their training set was made up of 9 months of data, which then predicted one month of actual data. Other studies had just good/bad/neutral. Most studies used past stock prices to predict future stock prices, but recently there's been a surge on using Sentiment Analysis. But I want to let the machine do all the work. 

**WHY STOCKS?**
Major financial firms like JP Morgan, Goldman Sachs, Morgan Stanley, CitiGroup hire quantitative traders for years to build predictive models on past market data. It is not totally random and can be predicted by: sentiment analysis, past prices, sales growth and dividends. About 70% of all orders on Wall Street are now placed by software, run by Machine Learning experts. 


**WHY TWITTER?**
Traditionally, psychologists would formulate a hypothesis, test it by finding a subset of people, bring them to a lab, tell them to do a task and record the results.

Fast forward: Twitter is a freely available psychology tool, where people around the world post thousands of reactions and opinions of every second of every day. It's like one big psychological database that's constantly being updated, and we can use it to analyze millions of text snippets with the power of Machine Learning. 

**OUTCOMES**
Market opportunities happen in real time; and people who tweet about them can deliver the information faster than the news media can. Stocks are constantly changing in price, and tweets of comments and opinions can act as timely alerts.

**SELECTION OF USERS**
* Find traders with more than 1,000 followers and who posts actionable stock-alert tweets.
* Look at his/her last tweet and make sure it was posted within the hour to ensure he/she tweets regularly and often.
* Some sophisticated traders with automated programs are using computer algorithms that instantly capture Trump’s Twitter remarks and then immediately buy or sell the affected stocks, analysts said.
    * *"I can't recall another president singling out companies for public comment -- certainly not on a regular basis -- but he seems to be willing to do that on an almost daily basis," he noted. "If his words have consequences and he acts on it, then investors are going to respond and I’d buckle in. There's going to be a lot of volatility in markets."*


## File and Directory Organization

```
/data - Directory for storing fixed data sets (twitter_users_30.csv)

/ipynb - Python notebooks
/ipynb/LSA - Unsupervised clustering of Latent Sentiment Analysis 
/ipynb/EDA - Exploratory Data Analysis
/ipynb/Feature_Engineering - Tracking feature engineering experiments peformed on that data
/ipynb/Model_Selection - Tracking model selection experiments peformed on that data
/ipynb/tweet_scraper - Collects tweets using REST and Realtime API

/doc - Documents related to the project
/src - lib?
/bin - ?

main.py - Bundled Functions
sentiment.sh - Sentiment Analyzer
tweets.sh - Tweet Collector

Organized according to: http://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1000424&type=printable
```


## Tools

The Twitter Sentiment Classifier is powered using Python and Ruby on Rails. Tweets are collected using Twitter's REST API ( TWITTER MODULE ). These tweets are then scored based on already collected reviews in the database ( REVIEWS MODULE ). The exchange between the database and Python code is handled using a Ruby on Rails REST API ( API MODULE ). Direct access to the MYSQL Server is also possible using the MYSQL MODULE. Further libraries such as NLTK are used to improve performance as well as accuracy of the analyzer.


## Premise

* <b>Use BOTH Sentiment Analysis (text) and Engagement (replies, retweets, mentions, hashtags, etc.) to predict stocks of the new tech companies</b></br>
    * What if I gave more weight to verified accounts (e.g. Elon Musk, Trump, etc.) or the # of followers?
    * What if I added another source of features (e.g. Google searches, price history)?
    * Narrow the scope:
        * Look at less established companies (Chipotles, McDonalds, Wendy's (sassy tweets), Arby's) - lots of people are having experiences with that company and they are less stable, therefore more susceptible to the effects of public sentiment. 
        * TECH COMPANIES GOING PUBLIC - Snap, FB, Tesla and SpaceX and Hyperloop 
        
        1. Check out Scott's historical twitter thing
        2. Research tech companies' quarterly activity
 
DataMinr strategy: test for changes in sentiment and use that as an alert to a human trader. The guys over at DataMinr have an incredible n-gram based sentiment approach that alerts stocks traders when sentiment changes (they use 30 day moving averages, tests for subject frequency, etc.).  Those guys identified the Osama event after 15 tweets came through on the subject. 
 

<b>My features will be <u>tweets AND engagement</u>.
My target will be stock prices.</b>


## Steps
* SCRAPE ASAP & let it run (can't get historical tweets with Twitter - check out Scott's link) - start pulling tweets that have my keywords. Use Tweepy to pull the data. Opening the firehose. 
    * filter: US, English
        * keywords: (snapchat, snap, tech, stocks, stock, instagram, stories, facebook live, discover, spectacles, public, IPO, etc.), stock acronyms, names, CEO's,  
    * Get target data (finance.google.com), code: https://www.youtube.com/watch?v=SSu00IRRraY
        * Stock value? Did it change (up/down)? 
* Set up MongoDB
* Install dependencies (Tweepy, sklearn, matplotlib, etc.)
* Store pulled Tweets in Mongo
* Store models in Redis (so you don't have to wait for your model to fit all that data again)

* Set up folders (doc, ipynb, etc.)
* Create helper text files (\__init\__.py, systemhelper.py, etc.)
* Store Twitter keys in seperate text file 
* Edit git ignore file in terminal (to make sure Twitter keys don't get pushed)

* Create new Mongo database with big volume attached on an AWS instance (T2 Micro) 
* Recreate NLP notebook 
* AWS with tmux, you can turn computer off and still be pulling Tweets (start pulling tweets and not touch it)


## NLP Strategy
* Sentiment Analysis (determining the "feeling" of text): Bag of Words or TFIDF or Word2Vec?
    * TruncatedSVD to find top words 
    
    * NOT DOING LEXICON APPROACH: Split text into smaller tokens (words) and count # of times the words show up in proportion (TFIDF) 
        * Compare to Sentiment Lexicon developed by researchers about sentiment  
    * DOING MACHINE LEARNING: more accurate because there are subtleties in language (sarcasm)
        * Deep neural nets can understand these subtleties because they don't analyze text at face value, they create abstract representation of what they learn (vectors) and we can use them to classify data
        
        1. import tflearn, from tflearn import to_categorical, pad_sequences
        2. DATA PREPROCESSING: vectorize the words 
        
        Selenium (getting text from HTML) + BeautifulSoup

## ML Strategy
* Use ARIMA to get rid of time series element (Autoregressive integrated moving average)
    * Read up on Autoregressive models
* Model stacking (learning on Friday)
* Support Vector Machines can be used to predict new data points on a graph
* Keras on TensorFlow?

* RandomForestClassifier (don't use linear models) to make a prediction

MODEL STACKING

- if using Random Forest, run it a few times without random state to see if results are consistent. THEN for final project, add randomstate for consistency. 
- HOLD OUT A VALIDATION DATA SET (base estimator can be overfit to training data, but we want blender to be trained on the predictions the base estimators will make on data they havent seen before 
    - Three layers? Three splits. 

## Success
* Success will be meastured by prediction score

## Additional Notes:
* Entries in the notebook should be dated and relatively verbose, with links or embedded images or tables displaying the results of the experiments that you performed. In addition to describing precisely what you did, the notebook should record your observations, conclusions, and ideas for future work.
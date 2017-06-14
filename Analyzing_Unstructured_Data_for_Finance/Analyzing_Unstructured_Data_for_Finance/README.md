# Analyzing Unstructured Data for Finance
## (a.k.a. Sentiment Analysis of Twitter to predict the rise and fall of stock prices)

**In this project, I took the tweets of 30 thought leaders and news outlets to predict the SP500 Index (^GSPC)**


## Outline

**WHY STOCKS?**
Major financial firms like JP Morgan, Goldman Sachs, Morgan Stanley, CitiGroup hire quantitative traders for years to build predictive models on past market data. About 70% of all orders on Wall Street are now placed by software, run by Machine Learning experts. 



**WHY TWITTER?**
Usually when we talk about financial data, we think pricing data. Financial analysis techniques for studying numeric, well-structured data are very mature. 

While using unstructured (a.k.a. “text”) data in finance is not a new idea (annual reports, broker research, conference call transcripts, investor relations presentations, 3rd party research, news and press releases), the area is still very green. 

Market opportunities happen in real time; and people who tweet about them can deliver the information faster than the news media can. Stocks are constantly changing in price, and tweets of comments and opinions can act as timely alerts.


**SELECTION OF USERS**
* Find traders with more than 1,000 followers and who posts actionable stock-alert tweets.
* Look at his/her last tweet and make sure it was posted within the hour to ensure he/she tweets regularly and often.
* Some sophisticated traders with automated programs are using computer algorithms that instantly capture Trump’s Twitter remarks and then immediately buy or sell the affected stocks, analysts said.
    * *"I can't recall another president singling out companies for public comment -- certainly not on a regular basis -- but he seems to be willing to do that on an almost daily basis," he noted. "If his words have consequences and he acts on it, then investors are going to respond and I’d buckle in. There's going to be a lot of volatility in markets."*


## File and Directory Organization

```
/data - fixed data sets and pickled objects
/doc - images
/ipynb - Python notebooks
/lib - source code for modules
```


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
* Entries in the notebook should be dated and relatively verbose, with links or embedded images or tables displaying the results of the experiments that you performed. In addition to describing precisely what you did, the notebook should record your observations, conclusions, and ideas for future work.# Analyzing_Unstructured_Data_for_Finance

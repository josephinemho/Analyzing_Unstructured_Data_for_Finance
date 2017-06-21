# Analyzing Unstructured Data for Finance
## a.k.a. Sentiment Analysis of Twitter to predict the rise and fall of stock prices

**Objective: Build an algorithm that can predict whether the S&P 500 index (^GSPC) goes up/down based on correlations with raw, unstructured text data extracted from Twitter.**


## Outline

**WHY STOCKS?**<br>
Major financial firms like JP Morgan, Goldman Sachs, Morgan Stanley, CitiGroup hire quantitative traders for years to build predictive models on past market data.<br>
About 70% of all orders on Wall Street are now placed by software, run by Machine Learning experts. 

**WHY TWITTER?**<br>
Usually when we talk about financial data, the first thing that comes to mind is pricing data (smoothing/ARIMA). Traditionally, it involves a lot of information about a company’s performance in numbers, you have traditional providers like Bloomberg and Reuters, which offer an abundance of pricing data related to specific companies, and techniques for studying numeric, well-structured data are very well-developed.<br>

On the other hand, using unstructured (“text”) data in finance is still a very green area. There are some experts who are looking at things like annual reports, broker research, investor relations presentations, 3rd party research and news and press releases. But it’s still an emerging field. 

**APPROACH**<br>
Minimal data cleaning (our benchmark) -> run it through a couple models -> explore data and results -> iterate (more data cleaning) -> repeat


## File and Directory Organization

```
/data - 1st iteration of project without data cleaning (our benchmark)
/data_cleaned  - 2nd iteration of project with data cleaning
/doc - supporting images & documents
/ipynb - Python notebooks
/lib - source code for modules
```


## Approach

**Part 1 -- Setup and Collection of Tweets**<br>
Pull Tweets from the Twitter API (using Tweepy) and collect tweets from 30 thought leaders and news outlets using MongoDB as a task manager (manual distributed processing).

**Part 2 -- Pre-Processing and Text Cleaning**<br>
Next we're going to do some basic pre-processing, like converting the text to lower case and deleting URLs. We don't need to remove stopwords such as "the" and "a", which will be done when we pass our data through a NLTK model later. 

**Part 3 -- Get Target Data (S&P 500)**<br>
Get our target data (the S&P 500 index) from the Yahoo Finance website and perform calculations. We want to look at the Adj Close price to determine whether stocks went up/down/neutral compared to the previous day. This will be a **classification model** and we will set our threshold of up/down/neutral to a change of 0.01%.

**Part 4 -- Combine Features and Target**<br>
Since our feature data (tweets) and target data (stocks) are pulled from different sources and have different numbers of rows and columns, we will need to do some cleaning to make sure our X's and y's share the same number of rows. This is important for when we feed our data into models.

**Part 5 -- Transform Target Data (SP500)**<br>
LabelEncode our y's so we can have more flexibility running it through models (e.g. LogisticRegression).

**Part 6 -- Model Selection**<br>
Using pipelines to find the best predictive model for our data.

## How to Follow Along

Notebooks found in the `/ipynb` folder are labeled 1-10, representing steps taken to complete this project. Every notebook has a step number, a brief description in the title of what to expect, and are annotated with comments describing the reasoning behind what Machine Learning methodologies were used. 


## Additional Notes:
A full presentation can be found at `Analyzing_Unstructured_Data_for_Finance/doc/Analyzing Unstructured Data for Finance.pptx`
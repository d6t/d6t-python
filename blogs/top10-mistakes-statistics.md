# Top 10 Statistics Mistakes Made by Data Scientists

A data scientist is a "person who is better at statistics than any software engineer and better at software engineering than any statistician". In [Top 10 Coding Mistakes Made by Data Scientists](https://github.com/d6t/d6t-python/blob/master/blogs/top10-mistakes-coding.md) we discussed how statisticians can become a better coders. Here we discuss how coders can become better statisticians.

## Not fully understand objective function

Data scientists want to build the "best" model. But beauty is in the eye of the beholder. If you don't know what the goal and objective function is and how it behaves, it is unlikely you will be able to build the "best" model. The objective may not even be a mathematical function but perhaps improving a business metric.

**Solution**: most kaggle winners spend a lot of time understanding the objective function and how the data and model relates to the objective function. If you are optimizing a business metric, you need to map it to an appropriate mathematical objective function.

## Not have a hypothesis why something should work

Commonly data scientists want to build "models". They heard xgboost and random forests work best so lets use those. I read about deep learning, maybe that will improve results further. They throw models at the problem without having looked at the data and without having formed a hypothesis which model is most likely to best capture the features of the data. It makes explaining your work really hard too because you are just randomly throwing models at data.

**Solution**: look at the data! understand its characteristics and form a hypothesis which model is likely to best capture those characteristics. 


## Not looking at the data before interpreting results

Another problem with not looking at the data is that your results can be heavily driven by outliers or other artifacts. This is especially true for models that minimize squared sums. Even without outliers, you can have problems with imbalanced datasets, clipped or missing values and all sorts of other weird artifacts of real-life data that you didn't see in school.

**Solution**: it's so important it's worth repeating: look at the data! Understand how the nature of the data is impacting model results. 

## Not having a naive baseline model

Modern ML libraries almost make it too easy... Just change a line of code and you can run a new model. And another. And another. Tweak parameters. With all the model fanciness you can forget the dumb way of forecasting data. Which means you don't have a good benchmark for your model, they may all overfit or be completely biased.

**Solution**: what's the dumbest way you can predict a value? Build a "model" using the last known value, the (rolling) mean or some constant eg 0. Compare your model performance against a zero-intelligence forecast monkey!

## Unaware of look-ahead bias

In school you rarely get time series data but in practice most data is time series data, likely panel data. With time series data, if you have data from the future, it's really easy to forecast data in the past! If you are not careful, any time you do feature engineering, scaling, cross-validation, data from the future can easily creep in and inflate performance. The model looked great in R&D but worked horrible in production. The model you said will do wonders is causing really bad business outcomes, potentially ruining your career!

**Solution**: make features, scaling and cross-validation such that you only use data that was available at the point of decision making.

## Subtle Overtraining

The more time you spend on a dataset, the more likely you are to overtrain it. You keep tinkering with features and optimizing model parameters. You used cross-validation so everything must be good.

**Solution**: After you have finished building the model, try to find another "version" of the datasets that can be a surrogate for a true out-sample dataset. If you are a manager, deliberately withhold data so that it does not get used for training.

## No simulated "live" outsample performance

You were taught cross-validation is all you need. sklearn even provides you some nice convenience functions, you think you have checked all the boxes. Especially with time series data that likely means data from the future creeped in and inflated your results. If the company makes big bets based on your predictions and loses, you can again ruin your career.

**Solution**: do a rolling out-sample forward test. If I had used this model in production, what would my training data look like, ie what data do you have to make predictions? That's the training data you use to make a true out-sample production test

## Not fully understand pros/cons of different models

Again ML libraries make it easy to just throw different models at a problem and see which model best minimizes errors. 

**Solution**: understand how a model works. Why does model 2 reduce the error vs model 1? Not just mathematically but using economic intuition.

## Cannot explain results

You've crunched the data and kept optimizing results. The error is low, everything is great. You take it back to the person who asked you to do the analysis and s/he starts asking questions: what does this variable mean? Why is the coefficient like this? What about when xyz happens? You hadn't thought about those questions because you were busy building models instead of applying the output. You don't look so smart anymore...

**Solution**: know the data, models and results inside out! And think like a user of the data, not just like the data cruncher.

## "need more data" fallacy

Counterintuitively, often the best way to get started analyzing data is by working on a representative sample of the data. That allows you to familiarize yourself with the data and build the data pipeline without waiting for data processing and model training. But data scientists seem not to like that - more data is better. 

**Solution**: start working with a small representative sample and see if you can get something useful out of it. Give it back to the end user, can they use it? does it solve a real pain point? If not, the problem is likely not because you have too little data but with your approach.

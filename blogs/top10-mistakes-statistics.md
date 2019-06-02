# Top 10 Statistics Mistakes Made by Data Scientists

A data scientist is a "person who is better at statistics than any software engineer and better at software engineering than any statistician". In [Top 10 Coding Mistakes Made by Data Scientists](https://github.com/d6t/d6t-python/blob/master/blogs/top10-mistakes-coding.md) we discussed how statisticians can become a better coders. Here we discuss how coders can become better statisticians.

Code for each of the examples is available in [github](folder link) and in an [interactive notebook](mybinder link). The code uses workflow management library [d6tflow](https://github.com/d6t/d6tflow) and data is shared with dataset management library [d6tpipe](https://github.com/d6t/d6tpipe).

## 1. Not fully understand objective function

Data scientists want to build the "best" model. But beauty is in the eye of the beholder. If you don't know what the goal and objective function is and how it behaves, it is unlikely you will be able to build the "best" model. And fwiw the objective may not even be a mathematical function but perhaps improving a business metric.

**Solution**: most kaggle winners spend a lot of time understanding the objective function and how the data and model relates to the objective function. If you are optimizing a business metric, map it to an appropriate mathematical objective function.

**Example**: F1 is typically used to assess classification models. We once built a classification model whose success depended on the % of occurances it was right. The F1 was misleading because it shows the model was correct ~60% of the time whereas in fact it was correct only 40% of the time.


## 2. Not have a hypothesis why something should work

Commonly data scientists want to build "models". They heard xgboost and random forests work best so lets use those. They read about deep learning, maybe that will improve results further. They throw models at the problem without having looked at the data and without having formed a hypothesis which model is most likely to best capture the features of the data. It makes explaining your work really hard too because you are just randomly throwing models at data.

**Solution**: look at the data! understand its characteristics and form a hypothesis which model is likely to best capture those characteristics. 

**Example**: Without running any models by just plotting this sample data, you can already have a strong view that x1 is linearly related with y and x2 doesn't have much of a relationship with y.
![Example2](reports/example2.png?raw=true "Example2")

## 3. Not looking at the data before interpreting results

Another problem with not looking at the data is that your results can be heavily driven by outliers or other artifacts. This is especially true for models that minimize squared sums. Even without outliers, you can have problems with imbalanced datasets, clipped or missing values and all sorts of other weird artifacts of real-life data that you didn't see in the classroom.

**Solution**: it's so important it's worth repeating: look at the data! Understand how the nature of the data is impacting model results. 

**Example**: with outliers, x1 slope changed from 0.906 to -0.375!
![Example3](reports/example3.png?raw=true "Example3")

## 4. Not having a naive baseline model

Modern ML libraries almost make it too easy... Just change a line of code and you can run a new model. And another. And another. Error metrics are decreasing, tweak parameters - great - error metrics are decreasing further... With all the model fanciness, you can forget the dumb way of forecasting data. And without that naive benchmark, you don't have a good absolute comparison for how good your models are, they may all be bad in absolute terms.

**Solution**: what's the dumbest way you can predict a value? Build a "model" using the last known value, the (rolling) mean or some constant eg 0. Compare your model performance against a zero-intelligence forecast monkey!

**Example**: With this time series data, model1 must be better than model2 with MSE of 0.21 and 0.45 respectively. But wait! By just taking the last known value, the MSE drops to 0.003!

## 5. Insufficient out-sample testing

This is the one that could derail your career! The model you built looked great in R&D works horrible in production. The model you said will do wonders is causing really bad business outcomes, potentially costing the company $m+. It's so important all the remaining mistakes bar the last one focus on it.

[Example: RF vs OLS in sample vs out sample]

**Solution**: Make sure you've run your model in realistic outsample conditions and understand when it will perform well and when it doesn't.

## 6. Incorrect out-sample testing: time series data

In school you rarely get time series data but in practice most data has a time element to it. If you have data from the future, it might be really easy to make predictions about the past! If you are not careful, any time you do feature engineering or cross-validation, data from the future can easily creep in and inflate performance. 

**Solution**: generate test data such that you capture any time-dependant relationships that could occur in production use.

**Example**: Here preprocessing is applied to the full dataset, not seperately for the train and test set.

```python

# bad
df = scipy.stats.zscore(df) # everything just became training data!
sklearn.model_selection.cross_validate(model,X,y, cv=10) # mixing training and test data

# better
for idx_train, idx_test in sklearn.model_selection.KFold(n_splits=10).split(df_ts2):
	# process train and test data seperately
    X_train, X_test = scipy.stats.zscore(X[train_index]), scipy.stats.zscore(X[test_index])
    y_train, y_test = scipy.stats.zscore(y[train_index]), scipy.stats.zscore(y[test_index])
    m_ols.fit(X_train,y_train)
    m_ols.predict(X_test) # using true test data

```

## 7. Incorrect out-sample testing: cross-sectional data & panel data

You were taught cross-validation is all you need. sklearn even provides you some nice convenience functions so you think you have checked all the boxes. But most cross-validation methods do random sampling so you might end up with training data in your test set which inflates performance.

[Example: ]

**Solution**: generate test data such that you capture any time-dependant relationships that could occur in production use.

## 8. Not considering which data is available at point of decision

When you run a model in production, it gets fed with data that is available when you run the model. That data might be different than what you assumed to be available in training. For example the data might be published with delay so by the time you run the model other inputs have changed and you are making predictions with wrong data.

**Solution**: do a rolling out-sample forward test. If I had used this model in production, what would my training data look like, ie what data do you have to make predictions? That's the training data you use to make a true out-sample production test. Furthermore, think about if you acted on the prediction, what result would that generate at the point of decision?

## 9. Subtle Overtraining

The more time you spend on a dataset, the more likely you are to overtrain it. You keep tinkering with features and optimizing model parameters. You used cross-validation so everything must be good.

Example: [cv optimize rf, apply to another dataset, check if cv test is similar to df1 cv error]

**Solution**: After you have finished building the model, try to find another "version" of the datasets that can be a surrogate for a true out-sample dataset. If you are a manager, deliberately withhold data so that it does not get used for training.

## 10. "need more data" fallacy

Counterintuitively, often the best way to get started analyzing data is by working on a representative sample of the data. That allows you to familiarize yourself with the data and build the data pipeline without waiting for data processing and model training. But data scientists seem not to like that - more data is better. 

**Solution**: start working with a small representative sample and see if you can get something useful out of it. Give it back to the end user, can they use it? Does it solve a real pain point? If not, the problem is likely not because you have too little data but with your approach.

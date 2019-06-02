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

**Example**: With this time series dataset, model1 must be better than model2 with MSE of 0.21 and 0.45 respectively. But wait! By just taking the last known value, the MSE drops to 0.003!

## 5. Insufficient out-sample testing

This is the one that could derail your career! The model you built looked great in R&D works horrible in production. The model you said will do wonders is causing really bad business outcomes, potentially costing the company $m+. It's so important all the remaining mistakes bar the last one focus on it.

**Solution**: Make sure you've run your model in realistic outsample conditions and understand when it will perform well and when it doesn't.

**Example**: In-sample the random forest does a lot better than linear regression with mse 0.048 vs ols mse 0.183 but out-sample it does a lot worse with mse 0.259 vs linear regression mse 0.187. The random forest overtrained and would not perform well live in production!

## 6. Incorrect out-sample testing: applying preprocessing to full dataset

In school you rarely get time series data but in practice most data has a time element to it. If you have data from the future, it might be really easy to make predictions about the past! If you are not careful, any time you do feature engineering or cross-validation, data from the future can easily creep in and inflate performance. 

**Solution**: make sure you have a true test set free of any leakage from training set. Especially beware of any time-dependant relationships that could occur in production use.

**Example**: Preprocessing is applied to the full dataset BEFORE it is split into train and test, meaning you do not have a true test set. Preprocessing needs to be applied seperately AFTER data is split into train and test sets to make it a true test set. The MSE between the two methods (mixed out-sample CV mse 0.187 vs true out-sample CV mse 0.181) in this case is not all that different because the distributional properties between train and test are not that different but that might not always be the case.

## 7. Incorrect out-sample testing: cross-sectional data & panel data

You were taught cross-validation is all you need. sklearn even provides you some nice convenience functions so you think you have checked all the boxes. But most cross-validation methods do random sampling so you might end up with training data in your test set which inflates performance.

**Solution**: generate test data such that it accurately reflects data on which you would make prdictions in live production use. Especially with time series and panel data you likely will have to generate custom cross-validation data or do roll-forward testing.

**Example**: here you have panel data for two different entities (eg companies) which are cross-sectionally highly correlated. If you randomly split data you make accurate predictions using data you did not actually have available during test, overstating model performance. You think you avoided mistake #5 by using cross-validation and found the random forest performs a lot better than linear regression in cross-validation. But running a roll-forward out-sample test which prevents future data from leaking into test, it performs a lot worse again! (random forest MSE goes from 0.047
to 0.211, higher than linear regression!)

## 8. Not considering which data is available at point of decision

When you run a model in production, it gets fed with data that is available when you run the model. That data might be different than what you assumed to be available in training. For example the data might be published with delay so by the time you run the model other inputs have changed and you are making predictions with wrong data or your true y variable is incorrect.

**Solution**: do a rolling out-sample forward test. If I had used this model in production, what would my training data look like, ie what data do you have to make predictions? That's the training data you use to make a true out-sample production test. Furthermore, think about if you acted on the prediction, what result would that generate at the point of decision?

## 9. Subtle Overtraining

The more time you spend on a dataset, the more likely you are to overtrain it. You keep tinkering with features and optimizing model parameters. You used cross-validation so everything must be good.

**Solution**: After you have finished building the model, try to find another "version" of the datasets that can be a surrogate for a true out-sample dataset. If you are a manager, deliberately withhold data so that it does not get used for training.

**Example**: Applying the models that were trained on dataset 1 to dataset 2 shows the MSEs more than doubled. Are they still acceptable...? This is a judgement call but your results from #4 might help you decide.

## 10. "need more data" fallacy

Counterintuitively, often the best way to get started analyzing data is by working on a representative sample of the data. That allows you to familiarize yourself with the data and build the data pipeline without waiting for data processing and model training. But data scientists seem not to like that - more data is better. 

**Solution**: start working with a small representative sample and see if you can get something useful out of it. Give it back to the end user, can they use it? Does it solve a real pain point? If not, the problem is likely not because you have too little data but with your approach.

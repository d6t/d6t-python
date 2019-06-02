Better at coding than stats, better at stats than coding. Not quite enough, need a commercial sense as well. 

## 1. Not understand business objective

## focus on data not the user

## overengineering instead of prototyping

Counterintuitively, often the best way to get started analyzing data is by working on a representative sample of the data. That allows you to familiarize yourself with the data and build the data pipeline without waiting for data processing and model training. But data scientists seem not to like that - more data is better. 


## 9. Cannot explain results

You've crunched the data and kept optimizing results. The error is low, everything is great. You take it back to the person who asked you to do the analysis and s/he starts asking questions: what does this variable mean? Why is the coefficient like this? What about when xyz happens? You hadn't thought about those questions because you were busy building models instead of applying the output. You don't look so smart anymore...

**Solution**: know the data, models and results inside out! And think like a user of the data, not just like the data monkey.

## 9. Not intuitively understand pros/cons of different models

Again ML libraries make it easy to just throw different models at a problem and see which model best minimizes errors. 

Example: We once built a model to understand human decisions. You could see decisions in the graphs decisions were very clustered and indeed a tree model performed much better than a linear regression. It made intuitive sense because human decision making is more like a decision tree than a regression.

**Solution**: understand how a model works. Why does model 2 reduce the error vs model 1? Not just mathematically but using economic intuition.

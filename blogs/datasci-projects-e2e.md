
# Guide to managing end-to-end data science projects

## Problem formulation:

### Business context / requirements

* target users: who are the target users of information? 
	* economic BUYER: who is the economic BUYER? 

* user flow: what is the user flow? where will the information/model be used? how does the user interact with the model?
	* user pain points: pain points? how do they solve it today?

* business impact goals: how does the model improve business outcomes?
	* critical bottleneck: what’s the critical problem that needs to be solved to have max impact?
	* business metric: what business metric are we trying to impact?
		* baseline: business metric status quo?
	* ideal outcome: what’s the ideal outcome here? what goal should be met?
	* success measure: how do we measure success?


### Design goals

* goals: goals of the project from a user perspective
* tradeoffs: ?
	* biz intel vs real-time decision making
	* accuracy: ?
	* interpretability: ?
	* speed: ?
	* online learning requirements?
	* deployment plan: where/how will it be used?
		* retraining: ?
		* evaluation: ?

optional:
* what should we avoid/be careful of? common pitfalls?
* what are some potential bottlenecks/issues in solving this?
* how would you deal with xyz?

### Target model output

* model output: model should predict/produce what?
	* how relate to business metric? direct vs approx/indirect measure?
	* V ideal output: target model
	* V 1.0 output: early model
* supporting output: what does a full prediction look like? incl meta data

### Model evaluation

* model score: which metric reflects success measure?
* loss function: how to optimize the model score?

###  Roadmap/project plan

* prototyping: build something the user can interact with
	* user feedback:
		* what does the output look like?
		* if we give you xyz does it work?
* early/easy wins: optimize impact ROI early on
* roadmap: how to sequence to achieve impact quickly and expand over time


##  Data pipeline

* Best practices
	* use [d6tflow data DAGs](https://github.com/d6t/d6tflow)
	* modularize code, see [d6tflow project templates for highly effective data science workflows](https://github.com/d6t/d6tflow-template)
	* use unit tests
	* don’t use jupyter notebooks, except viz or UI prototype

### Data sources

* Preferred data sources: What did we wish we had?
* Actual data sources: What are the sources and how can we acquire?
	* Tearsheet available?
	* Data dictionary available?
* How much labeled data do you have?

### Infrastructure requirements/constraints

* data prep: how large is input data?
* model training: type and complexity of model?
* dev vs prod: prod bottlenecks? storage/compute/memory

### Data preprocessing

* Data DAG: preparing data for analysis

### Exploratory data analysis

* Look at the data!
	* Start with a representative sample
* Summary visualizations
	* Distributions
	* Relationships
		* Stability over time
* Categorical variables
* Quirks: skews/non-normal, Outliers, Missing values, imbalanced data, non-stationarity, autocorrel, multicolinearity, heteroskedasticity
* Biases: lookahead.  
* AutoML output
* Hypothesis on what should/should not work: Which features are most likely to predict? Which features should/should not predict?

See [d6t EDA templates](https://github.com/d6t/d6tflow-template-datasci)

### Feature engineering

* Feature library:
	* Interaction features

### Feature preprocessing

* Normalize: N(0,1), mean relative
* Look-ahead bias: real-time decision making issues
* Fix quirks
* Other transforms
	* Dimension reduction
		* PCA
		* GBM feature encoding
	* Embeddings


## Model building

* baseline models:
* candidate models:
	* ability to meet design goals?
	* address tradeoffs: accuracy / interpretability / speed?
	* handle quirks?
	* scalability?
* train / validation / test
* feature selection
* model training
	* parameters
		* weights: input, class
		* learnings rates, # trees
	* regularization: penalties. early stopping.
		* GBM: number of trees. tree depth
		* DL: dropout. 
	* execution infrastructure: total training size? model size?
* hyperparam tuning
* ensembling/stacking

## Model Evaluation

### Evaluation metrics 

* Comparing models:
	* In-sample: baseline vs model
	* Out-sample: baseline vs model
	* Bias-variance trade-off
* Visual inspection: sample. best/worst predictions. high influence.
* Overfitting assessment
	* Test lookahead bias
	* Stability of relationships
	* Stability of test errors

### Model interpretation

* Model output
* Feature importance
* SHAP plots
* Surrogate models

### User feedback

* performance drivers vs intuition
* single predictions for decision making

## Deployment 

* Data pipline best practices
	* Automated tests
* Model speedup
	* Surrogate models
	* Fewer features: remove marginal features
	* Fewer trees: stop after achieved majority of gains
* options: db vs API

### A / B testing


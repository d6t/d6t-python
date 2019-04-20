# Top 10 Coding Mistakes Made by Data Scientists

A data scientist is a "person who is better at statistics than any software engineer and better at software engineering than any statistician". Many data scientists have a statistics background and little experience with software engineering. I'm a senior data scientist ranked top 1% on Stackoverflow for python coding and work with a lot of (junior) data scientists. Here is my list of 10 common mistakes I frequently see.

## 1. Don't share data referenced in code

Data science needs code AND data. So for someone else to be able to reproduce your results, they need to have access to the data. Seems basic but a lot of people forget to share the data with their code.

```python

import pandas as pd
df1 = pd.read_csv('file-i-dont-have.csv') # fails
do_stuff(df)

```

**Solution**: Use [d6tpipe](https://github.com/d6t/d6tpipe) to share data files with your code or upload to S3/web/google drive etc or save to a database so the recipient can retrieve files (but don't add them to git, see below).

## 2. Hardcode inaccessible paths

Similar to mistake 1, if you hardcode paths others don't have access to, they can't run your code and have to look in lots of places to manually change paths. Booo!

```python

import pandas as pd
df = pd.read_csv('/path/i-dont/have/data.csv') # fails
do_stuff(df)

# or 
impor os
os.chdir('c:\\Users\\yourname\\desktop\\python') # fails

```

**Solution**: Use relative paths, global path config variables or [d6tpipe](https://github.com/d6t/d6tpipe) to make your data easily accessible.

## 3. Mix data with code

Since data science code needs data why not dump it in the same directory? And while you are at it, save images, reports and other junk there too. Yikes, what a mess!

```
├── data.csv
├── ingest.py
├── other-data.csv
├── output.png
├── report.html
└── run.py
```

**Solution**: Organize your directory into categories, like data, reports, code etc. See [Cookiecutter Data Science
](https://drivendata.github.io/cookiecutter-data-science/#directory-structure) or [d6tflow project templates](https://github.com/d6t/d6tflow-template) and use tools mentioned in #1 to store and share data.

## 4. Git commit data with source code

Most people now version control their code (if you don't that's another mistake!! See [git](https://git-scm.com/)). In an attempt to share data, it might be tempting to add data files to version control. That's ok for very small files but git is not optimized for data, especially large files.

```bash
git add data.csv
```

**Solution**:  Use tools mentioned in #1 to store and share data. If you really want to version control data, see [d6tpipe](https://github.com/d6t/d6tpipe), [DVC](https://dvc.org/) and [Git Large File Storage](https://git-lfs.github.com/).

## 5. Write functions instead of DAGs

Enough about data, lets talk about the actual code! Since one of the first things you learn when you learn to code are functions, data science code is mostly organized as a series of functions that are run linearly. That causes several problems, see [4 Reasons Why Your Machine Learning Code is Probably Bad](https://github.com/d6t/d6t-python/blob/master/blogs/reasons-why-bad-ml-code.rst). 

```python

def process_data(data, parameter):
    data = do_stuff(data)
    data.to_pickle('data.pkl')

data = pd.read_csv('data.csv')
process_data(data)
df_train = pd.read_pickle(df_train)
model = sklearn.svm.SVC()
model.fit(df_train.iloc[:,:-1], df_train['y'])

```

**Solution**: Instead of linearly chaining functions, data science code is better written as a set of tasks with dependencies between them. Use [d6tflow](https://github.com/d6t/d6tflow) or [airflow](https://airflow.apache.org/).

## 6. Write for loops

Like functions, for loops are the first thing you learn when you learn to code. Easy to understand, but they are slow and excessively wordy, typically indicating you are unaware of vectorized alternatives. 

```python

x = range(10)
avg = sum(x)/len(x); std = math.sqrt(sum((i-avg)**2 for i in x)/len(x));
zscore = [(i-avg)/std for x]
# should be: scipy.stats.zscore(x)

# or
groupavg = []
for i in df['g'].unique():
	dfg = df[df[g']==i]
	groupavg.append(dfg['g'].mean())
# should be: df.groupby('g').mean()

```

**Solution**: [Numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/) and [pandas](https://pandas.pydata.org/) have vectorized functions for most things that you think might require for loops.

## 7. Don't write unit tests

As data, parameters or user input change, your code might break, sometimes without you noticing. That can lead to bad output and if someone makes decisions based on your output, bad data will lead to bad decisions!

**Solution**: Use `assert` statements to check for data quality. [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/general_utility_functions.html#testing-functions) has equality tests, [d6tstack](https://github.com/d6t/d6tstack) has checks for data ingestion and [d6tjoin](https://github.com/d6t/d6tjoin/blob/master/examples-prejoin.ipynb) for data joins. Code for example data checks:

```python

assert df['id'].unique().shape[0] == len(ids) # have data for all ids?
assert df.isna().sum()<0.9 # catch missing values
assert df.groupby(['g','date']).size().max() ==1 # no duplicate values/date?
assert d6tjoin.utils.PreJoin([df1,df2],['id','date']).is_all_matched() # all ids matched?

```

## 8. Don't document code

I get it, you're in a hurry to produce some analysis. You hack things together to get results to your client or boss. Then a week later they come back and say "can you change xyz" or "can you update this please". You look at your code and can't remember why you did what you did. And now imagine someone else has to run it.

```python

def some_complicated_function(data):
	data = data[data['column']!='wrong']
	data = data.groupby('date').apply(lambda x: complicated_stuff(x))
	data = data[data['value']<0.9]
	return data

```

**Solution**: Take the extra time, even if it's after you've delivered the analysis, to document what you did. You will thank yourself and other will do so even more! You'll look like a pro!

## 9. Save data as csv or pickle

Back data, it's DATA science after all. Just like functions and for loops, CSVs and pickle files are commonly used but they are actually not very good. CSVs don't include a schema so everyone has to parse numbers and dates again. Pickles solve that but only work in python and are not compressed. Both are not good formats to store large datasets.

```python

def process_data(data, parameter):
    data = do_stuff(data)
    data.to_pickle('data.pkl')

data = pd.read_csv('data.csv')
process_data(data)
df_train = pd.read_pickle(df_train)

```

**Solution**: Use [parquet](https://github.com/dask/fastparquet) or other binary data formats with data schemas, ideally ones that compress data. [d6tflow](https://github.com/d6t/d6tflow) automatically saves data output of tasks as parquet so you don't have to deal with it.

## 10. Use jupyter notebooks

Lets conclude with a controversial one: jupyter notebooks are as common as CSVs. A lot of people use them. That doesn't make them good. Jupyter notebooks promote a lot of bad software engineering habits mentioned above, notably:

1. You are tempted to dump all files into one directory
2. You write code that runs top-bottom instead of DAGs
3. You don't modularize your code
4. Difficult to debug
5. Code and output gets mixed in one file
6. They don't version control well

It feels easy to get started but scales poorly.

**Solution**: Use [pycharm](https://www.jetbrains.com/pycharm/) and/or [spyder](https://www.spyder-ide.org/).

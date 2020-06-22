#Write Unit Tests: You will thank yourself later
One common mistake that data scientists, especially beginners, makes is not writing unit tests. When I learnt data science from school, the importance of writing proper tests for codes was rarely addressed. Yes, we already have enough to kill our time as beginners, but unit testing is one thing I wish I had spent time on and learnt sooner among all others. Compared to the time you invest in learning and writing unit tests, good pieces of simple tests will save you much more time later, especially when working on large projects or big data.

## Benefits of Unit Testing
* Detect bugs earlier: Running big data projects is time consuming. You don't want to get an unexpected output after 3-hour running when you could have easily avoided it.
* Easier to update codes: You will be no longer afraid of changing your code because you know what to expect and you can easily tell what is broken if it is boken.
* Push you to have a better structured code: You will write cleaner codes and prefer to write in DAGs instead of linearly chaining functions when you keep in mind you are gonna test your codes with isolated pieces.
* Give you confidence on the outputs: Bad data leads to bad decisions. Running unit tests gives you confidence on data quality because you know your code outputs what you want it ouputs.

## Things to check with unit testing
Depending on your projects, what you want to check with unit testing will be different. But there are some common tests you would wish to run for data science solutions.  
#### 1.missing values
```
assert df['column'].isna().sum()<1 #catch missing valus
```
#### 2.no duplicate
````
assert len(df['id'].unique())==df.shape[0]
assert df.groupby(['date','id']).size().max()==1
````
#### 3.shapes
```
assert df['id'].unique().shape[0] == len(ids) # have data for all ids?
assert all([some_funtion(df).shape == df[0].shape for df in dfs]) # function returns have shapes as expected
```  
#### 4.value ranges
```
assert df.groupby('date')['percentage'].sum()==1 
assert all (df['percentage']<=1)
assert df.groupby('name')['budget'].max()<=1000
```
#### 5.join quality
[d6tjoin](https://github.com/d6t/d6tjoin) has checks for join quality.
```
assert d6tjoin.Prejoin([df1,df2],['date','id']).is_all_matched()
```
#### 6.preprocess functions
```
assert preprocess_function("name\t10019\n")==["name",10019]
assert preprocess_missing_name("10019\n") is None
assert preprocess_text("Do you Realize those are genetically modified food?" ) == ["you","realize","gene","modify","food"]
```







 


   
# Unit Test Your Data Pipeline, You Will Thank Yourself Later
One common mistake that data scientists, especially beginners, make is not writing unit tests. Data scientists sometimes argue that unit testing is not applicable because there is no correct answer to a model that can be known ahead of time or to test with. However, most data science projects start with data transformation. While you cannot test model output, at least you should test that inputs are correct. Compared to the time you invest in writing unit tests, good pieces of simple tests will save you much more time later, especially when working on large projects or big data.

Coauthored with [Haijing Li](https://www.linkedin.com/in/haijing-li-7b50a11b2/), Data Analyst in Financial Services, MS Business Analytics@Columbia University.
## Benefits of Unit Testing
* Detect bugs earlier: Running big data projects is time consuming. You don't want to get an unexpected output after 3-hour running when you could have easily avoided it.
* Easier to update codes: You will be no longer afraid of changing your code because you know what to expect and you can easily tell what is broken if it is broken.
* Push you to have a better structured code: You will write cleaner codes and prefer to write in DAGs instead of linearly chaining functions when you keep in mind you are gonna test your codes with isolated pieces. (use [d6tflow](https://github.com/d6t/d6tflow) to build data science workflows easily)
* Give you confidence on the outputs: Bad data leads to bad decisions. Running unit tests gives you confidence on data quality. You know your code outputs what you want it to output.

## Pytest

To improve testing efficiency, use Pytest. If you are looking for tutorials on Pytest, I would recommend Dane Hillard's post [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/). In his post you will find out how to utilize basic and advanced Pytest features.

## Unit Testing for Data Science
Depending on your projects, what you want to check with unit testing will be different. But there are some common tests you would wish to run for data science solutions.  
#### 1.Missing values
```
#catch missing values
assert df['column'].isna().sum()<1 
```
#### 2.Duplicates
```
# check there is no duplicate
assert len(df['id'].unique())==df.shape[0]
assert df.groupby(['date','id']).size().max()==1
```
#### 3.Shapes
```
# have data for all ids?
assert df['id'].unique().shape[0] == len(ids)

# function returns have shapes as expected
assert all([some_funtion(df).shape == df[0].shape for df in dfs])
```  
#### 4.Value Ranges
```
assert df.groupby('date')['percentage'].sum()==1 
assert all (df['percentage']<=1)
assert df.groupby('name')['budget'].max()<=1000
```
#### 5.Join Quality
[d6tjoin](https://github.com/d6t/d6tjoin) has checks for join quality.
```
assert d6tjoin.Prejoin([df1,df2],['date','id']).is_all_matched()
```
#### 6.Preprocess Functions
```
assert preprocess_function("name\t10019\n")==["name",10019]
assert preprocess_missing_name("10019\n") is None
assert preprocess_text("Do you Realize those are genetically modified food?" ) == ["you","realize","gene","modify","food"]
```







 


   
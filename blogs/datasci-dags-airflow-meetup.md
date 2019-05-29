# Data Science needs DAGs too

We will be using the d6tflow open source python library to bring airflow-style DAGs to the data science research and development process. You will learn how to make building complex data science workflows easy, fast and intuitive.

## Data workflows are DAGs

Data science workflows typically look like this.

![Sample Data Workflow](https://github.com/d6t/d6tflow/blob/master/docs/d6tflow-docs-graph.png?raw=true "Sample Data Workflow")

This workflow involves chaining together parameterized tasks which pass multiple inputs and outputs between each other. The output data gets stored in multiple dataframes, files and databases but you have to manually keep track of where everything is. And often you want to rerun tasks with different parameters without inadvertently rerunning long-running tasks. The workflows get complex and your code gets messy, difficult to audit and doesn't scale well.

Read more at [4 Reasons Why Your Machine Learning Code is Probably Bad](https://github.com/d6t/d6t-python/blob/master/blogs/reasons-why-bad-ml-code.rst)

TLDR: passing data between functions or hardcoding file/database names without explicity defining task dependencies is a NOT good way of writing data science code.

```python

# bad data science code
def process_data(data, do_preprocess):
    data = do_stuff(data, do_preprocess)
    data.to_pickle('data.pkl')

data = pd.read_csv('data.csv')
process_data(data, True)
df_train = pd.read_pickle(df_train)
model = sklearn.svm.SVC()
model.fit(df_train.iloc[:,:-1], df_train['y'])

```

## R&D vs production workflows

Airflow is mostly used by data engineers in a production setting where the focus is on making sure everything is running smoothly and recovering from failures. 

In contrast, focus in the R&D workflow is on generating insights and assessing predictive power with different models and parameters. This workflow:  
* is less well defined
* involves trial and error
* frequent resetting of tasks and output as data, models and parameters change
* takes output from the data engineer

## How d6tflow is different from airflow/luigi

### Problems with airflow/luigi in R&D settings

Both libraries are a big step up for managing data workflows. But they are optimized for data engineering production settings, the UX for a data scientist was not great:  

* WET code for reading/writing data
* Manually keep track of filenames or database table names where data is saved
* Inconvenient to reset tasks as data, models and parameters change
* Inconvenient to keep track of model results with different parameter settings

d6tflow is optimized for data science settings.

![Filenames nightmare](images/d6tflow-filenames.png?raw=true "Filenames nightmare")


### Benefit: Tasks have input and ouput data

Instead of having to manually load and save data, this is handled by library.

```python
class TaskProcess(d6tflow.tasks.TaskPqPandas): # define output format

    def requires(self):
        return TaskGetData() # define dependency

    def run(self):
        data = self.input().load() # load input data
        data = do_stuff(data) # process data
        self.save(data) # save output data
```

### Benefit: Easily invalidate tasks

Common invalidation scenarios are implemented.

```python
# force execution including downstream tasks
d6tflow.run(TaskTrain(), force=TaskGetData())

# reset single task
TaskGetData().invalidate()

# reset all downstream tasks
d6tflow.invalidate_downstream(TaskGetData(), TaskTrain())

# reset all upstream tasks
d6tflow.invalidate_upstream(TaskTrain())

```

### Benefit: Easily train models using different paramters

Intelligently rerun workflow after changing a preprocessing parameter

```python
d6tflow.preview([TaskTrain(do_preprocess=False)])

'''
└─--[TaskTrain-{'do_preprocess': 'False'} (PENDING)]
   └─--[TaskPreprocess-{'do_preprocess': 'False'} (PENDING)]
      └─--[TaskGetData-{} (COMPLETE)] => this doesn't change and doesn't need to rerun
'''
```

### Benefit: Easily compare models

Different models that were trained with different parameters can be easily loaded.

```python
df_train = TaskPreprocess().output().load()
model1 = TaskTrain().output().load()
print(sklearn.metrics.accuracy_score(df_train['y'],model1.predict(df_train.iloc[:,:-1])))

model2 = TaskTrain(do_preprocess=False).output().load()
print(sklearn.metrics.accuracy_score(df_train['y'],model2.predict(df_train.iloc[:,:-1])))

```

### Not yet available

* Auto rerun on data changes
* Auto rerun on code changes

## d6tflow Quickstart

https://github.com/d6t/d6tflow#example-output

## Template for scalable ML projects

Template for real-life projects is available
https://github.com/d6t/d6tflow-template

## Data engineer to data scientist hand-off

To quickly share workflow output files, you can use [d6tpipe](https://github.com/d6t/d6tpipe). See [Sharing Workflows and Outputs](https://d6tflow.readthedocs.io/en/latest/collaborate.html).

Alternatively you can save outputs in a database using [d6tflow premium](https://pipe.databolt.tech/gui/request-premium/).

```python
d6tflow2.db.init('postgresql+psycopg2://usr:pwd@localhost/db', 'schema_name')

class Task2(d6tflow2.tasks.TaskSQLPandas):

    def run(self):
        df = pd.DataFrame()
        self.save(df)


```

Finally, the data scientist can inherit from tasks the data engineer has written to quickly load source data.

```python
import tasks_factors
import utils

class TaskFactorComposite(tasks_factors.TaskFactorComposite):
    external = True
    pipename = cfg.pipename_source
```

## Bonus: centralize (local) data science files

## Bonus: keeping credentials safe

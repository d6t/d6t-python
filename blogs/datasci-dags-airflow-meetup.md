# How to use airflow-style DAGs to build highly effective data science workflows

Airflow and Luigi are great for data engineering productions workflows but not optimized for data science r&d workflows. We will be using the d6tflow open source python library to bring airflow-style DAGs to the data science research and development process.

## Data science workflows are DAGs

Data science workflows typically look like this.

![Sample Data Workflow](https://github.com/d6t/d6tflow/blob/master/docs/d6tflow-docs-graph.png?raw=true "Sample Data Workflow")

This workflow is similar to data engineering workflows. It involves chaining together parameterized tasks which pass multiple inputs and outputs between each other. See [4 Reasons Why Your Machine Learning Code is Probably Bad](https://github.com/d6t/d6t-python/blob/master/blogs/reasons-why-bad-ml-code.rst) why passing data between functions or hardcoding file/database names without explicity defining task dependencies is NOT a good way of writing data science code.

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

## R&D vs production data workflows

Using airflow or luigi is a big step up from writing functional code for managing data workflows. But both libraries are designed to be used by data engineers in production settings where the focus is on making sure everything is running smoothly on time and recovering from failures. 

In contrast, focus in the r&d workflow is on:  
* prototyping speed
* generating insights
* assessing predictive power with different models and parameters
* visualizing output

As a result, the r&d workflow:  
* is less well defined
* involves trial and error
* requires frequent resetting of tasks and output as models, parameters and data change
* takes output from the data engineer

## Problems with airflow/luigi in R&D settings

Since both libraries are optimized for data engineering production settings, the UX for a data science r&d setting is not great:  

* WET code for reading/writing data
* Manually keep track of filenames or database table names where data is saved
* Inconvenient to reset tasks as models, parameters and data change
* Inconvenient to keep track of model results with different parameter settings

![Filenames nightmare](images/d6tflow-filenames.png?raw=true "Filenames nightmare")

## How d6tflow is different from airflow/luigi

d6tflow is optimized for data science research and development workflows. Here are benefits of using d6tflow in data science.

### Benefit: Tasks have input and ouput data

Instead of having to manually load and save data, this is outsourced to the library. This scales better and reduces maintanance because the location of input/output data could change without having to rewrite code. It also makes it easier for the data engineer to hand off data to the data scientist.

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

Common invalidation scenarios are implemented. This increases prototyping speed as you change code and data during trial & error.

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

You can intelligently rerun workflow after changing a parameter. Parameters are passed from the target task to the relevant downstream task. Thus, you no longer have to manually keep track of which tasks to update, increasing prototyping speed and reducing errors.

```python
d6tflow.preview([TaskTrain(do_preprocess=False)])

'''
└─--[TaskTrain-{'do_preprocess': 'False'} (PENDING)]
   └─--[TaskPreprocess-{'do_preprocess': 'False'} (PENDING)]
      └─--[TaskGetData-{} (COMPLETE)] => this doesn't change and doesn't need to rerun
'''
```

### Benefit: Easily compare models

Different models that were trained with different parameters can be easily loaded and compared. 

```python
df_train = TaskPreprocess().output().load()
model1 = TaskTrain().output().load()
print(sklearn.metrics.accuracy_score(df_train['y'],model1.predict(df_train.iloc[:,:-1])))

df_train = TaskPreprocess(do_preprocess=False).output().load()
model2 = TaskTrain(do_preprocess=False).output().load()
print(sklearn.metrics.accuracy_score(df_train['y'],model2.predict(df_train.iloc[:,:-1])))

```

## d6tflow Quickstart

Here is a full example of how to use d6tflow for a ML workflow
https://github.com/d6t/d6tflow#example-output

## Template for scalable ML projects

A d6tflow code template for real-life projects is available at 
https://github.com/d6t/d6tflow-template

* Multiple task inputs and outputs
* Parameter inheritance
* Modularized tasks, run and viz


## Accelerate data engineer to data scientist hand-off

To quickly share workflow output files, you can use [d6tpipe](https://github.com/d6t/d6tpipe). See [Sharing Workflows and Outputs](https://d6tflow.readthedocs.io/en/latest/collaborate.html).

```python
import d6tflow.pipe

d6tflow.pipe.init(api, 'pipe-name') # save flow output 
pipe = d6tflow.pipes.get_pipe()
pipe.pull()

class Task2(d6tflow.tasks.TaskPqPandas):

    def requires(self):
        return Task1() # define dependency

    def run(self):
        data = self.input().load() # load data from data engineer

```

Alternatively you can save outputs in a database using [d6tflow premium](https://pipe.databolt.tech/gui/request-premium/).

```python
d6tflow2.db.init('postgresql+psycopg2://usr:pwd@localhost/db', 'schema_name')

class Task1(d6tflow2.tasks.TaskSQLPandas):

    def run(self):
        df = pd.DataFrame()
        self.save(df)


```

Finally, the data scientist can inherit from tasks the data engineer has written to quickly load source data.

```python
import tasks_factors # import tasks written by data engineer
import utils

class Task1(tasks_factors.Task1):
    external = True # rely on data engineer to run

    def run(self):
        data = self.input().load() # load data from data engineer
```

## Bonus: centralize (local) data science files

## Bonus: keeping credentials safe

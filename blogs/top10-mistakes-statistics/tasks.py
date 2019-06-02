import d6tflow, luigi

import sklearn.datasets
import sklearn.linear_model
import sklearn.ensemble

import pandas as pd
import numpy as np
import scipy.stats

import cfg

def train2model(df1,df2,m1,m2):
    m1.fit(df1.iloc[:, :-1], df1.iloc[:, -1])
    m2.fit(df2.iloc[:, :-1], df2.iloc[:, -1])
    return m1, m2

class DataRegression(d6tflow.tasks.TaskPqPandas):
    random_state = luigi.IntParameter(default=0)
    noise = luigi.IntParameter(default=10)
    def run(self):
        r1 = sklearn.datasets.make_regression(n_samples=cfg.nobs, n_features=2, n_informative=1, coef=True, noise=self.noise, random_state=self.random_state)
        df = pd.DataFrame(r1[0])
        df['y'] = scipy.stats.zscore(r1[1])
        df.columns = ['x1','x2','y']
        self.save(df)

class DataOutliers(d6tflow.tasks.TaskPqPandas):
    def requires(self):
        return DataRegression()

    def run(self):
        df1 = self.input().load()
        df2 = pd.DataFrame({'x1': np.repeat(2, cfg.nobs), 'x2': np.repeat(0, cfg.nobs), 'y': np.repeat(-2, cfg.nobs)})
        df2 = pd.concat([df1, df2])
        self.save(df2)

class Model2(d6tflow.tasks.TaskPickle):
    persist = ['m1','m2']
    def save2(self, m1, m2):
        self.save({'m1': m1, 'm2': m2})

class ModelOutliers(Model2):
    def requires(self):
        return DataRegression(), DataOutliers()

    def run(self):
        df1, df2 = self.inputLoad()
        m1 = sklearn.linear_model.LinearRegression()
        m2 = sklearn.linear_model.LinearRegression()
        m1, m2 = train2model(df1, df2, m1, m2)
        self.save2(m1,m2)

class DataTS(d6tflow.tasks.TaskPqPandas):

    def requires(self):
        return DataRegression()

    def run(self):
        self.save(self.input().load().sort_values('y'))

class ModelTS(Model2):
    def requires(self):
        return DataTS()

    def run(self):
        df1 = self.inputLoad()
        m1 = sklearn.linear_model.LinearRegression()
        m2 = sklearn.ensemble.RandomForestRegressor(n_estimators=10, random_state=0)
        m1, m2 = train2model(df1, df1, m1, m2)
        self.save2(m1,m2)

class OLSvsRF(ModelTS):
    def requires(self):
        return DataRegression()

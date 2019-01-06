# Databolt python libraries

## Accelerate data engineering

DataBolt is a collection of python-based products and libraries to reduce the time it takes to get your data ready for evaluation and analysis.

It is designed for data scientists and data engineers who want to reduce frictions in data pipelines and analysis.

It covers the early stages of the data engineering/data science workflow:  
* **sync data**: quickly pull/push data from/to remotes data repos and share with others
* **ingest data**: quickly ingest messy CSV and XLS files. Export to clean pandas, SQL, parquet
* **join data**: quickly combine multiple datasets even if they don't perfectly match using fuzzy joins
* **manage data workflows**: manage workflow of data tasks with dependencies optimized for data science

The libraries are modularized so you can use them individually but they work well together to improve your entire data workflow.


## [Sync Data](https://github.com/d6t/d6tpipe)

Quickly exchange data, for example between data vendors and consumers, data engineers and data scientists, teachers and students or desktop and laptop. In just a few lines of code, you can push and pull data to/from remote data repos in a simple and unified framework. 

It's like git for data! But better because you can include it in your data science code. This way you can separate data from code: code in git repo, data in a data repo.

### Features include

* Quickly create private and public data repos
* Push/pull data to/from data repos
* Add read parameters so others can quickly ingest

Learn more at [https://github.com/d6t/d6tpipe](https://github.com/d6t/d6tpipe)


## [Ingest Data](https://github.com/d6t/d6tstack)

Quickly ingest raw files. Works for XLS, CSV, TXT which can be exported to CSV, Parquet, SQL and Pandas. d6tstack solves many performance and other problems typically encountered when ingesting raw files.

### Features include

* Fast pd.to_sql() for postgres and mysql
* Quickly check and fix data schema changes eg added/missing/renamed columns
* Export messy Excel files to clean CSV

Learn more at [https://github.com/d6t/d6tstack](https://github.com/d6t/d6tstack)


## [Combine Data](https://github.com/d6t/d6tjoin)

Easily join different datasets even if they don't perfectly match without writing custom code. Does best match joins on strings, dates and numbers. For example you can quickly join similar but not identical stock tickers, addresses, names and dates without manual processing.

### Features include

* Pre join diagnostics to identify mismatched join keys
* Best match fuzzy joins that finds the top1 most similar value
* Best match substring joins

Learn more at [https://github.com/d6t/d6tjoin](https://github.com/d6t/d6tjoin)


## [Manage data workflows](https://github.com/d6t/d6tflow)

Easilly manage data workflows including complex dependencies and parameters. It is built on top of workflow manager [luigi](https://github.com/spotify/luigi) but unlike luigi it is optimized for a data science workflow. It integrates pandas and dask as dataframes and parquet as storage among others. It is compatiable with [d6tpipe](https://github.com/d6t/d6tpipe) for easily sharing data in your workflow.

### Features include

* Manage data workflows made up of individual tasks with dependencies
* Easily load and save dataframes in each task
* Supports Pandas, Dask, Parquet, CSV, json and pickle

Learn more at [https://github.com/d6t/d6tflow](https://github.com/d6t/d6tflow)


## [Blog](http://blog.databolt.tech)

We encourage you to join the Databolt blog to get updates and tips+tricks [http://blog.databolt.tech](http://blog.databolt.tech)


## [About](https://www.databolt.tech)

[https://www.databolt.tech](https://www.databolt.tech)

For questions or comments contact: support-at-databolt.tech

## [Alternative Investment Data Standards](https://github.com/d6t/altdata-standards)

Proposal to establish open standards to improve data exchange between alternative investment data vendors and consumers.

[https://github.com/d6t/altdata-standards](https://github.com/d6t/altdata-standards)

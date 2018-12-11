# Databolt python libraries

## Accelerate data engineering

DataBolt is a collection of python-based products and libraries to reduce the time it takes to get your data ready for evaluation and analysis.

It is designed for data scientists and data engineers who appreciate open data exchange and want to reduce frictions in data pipelines.

It covers the early stages of the data engineering/data science workflow:  
* sync data: quickly pull/push data from/to a source, directly in python with just a few lines of code
* ingest data: quickly ingest raw files to a database, parquet or pandas with better performance and features than other loaders
* join data: quickly combine multiple datasets even if they don't perfectly match


## [Sync Data](https://github.com/d6t/d6tpipe)

Quickly exchange data, for example between data vendors and consumers, data engineers and data scientists, teachers and students or desktop and laptop. In just a few lines of code, you can push and pull data to/from S3 and ftp in a simple and unified framework. 

It's like git for data! But better because you can include it in your data science code.

### Features include

* Push/pull data to/from s3/ftp
* Schedule regular sync tasks
* Manage access permissions
* Include DDL so others can quickly ingest 

[https://github.com/d6t/d6tpipe](https://github.com/d6t/d6tpipe)


## [Ingest Data](https://github.com/d6t/d6tstack)

Quickly ingest raw files. Works for XLS, CSV, TXT which can be exported to CSV, Parquet, SQL and Pandas. d6tstack solves many performance and other problems typically encountered when ingesting raw files.

### Features include

* Ingest multiple raw files to clean CSV, Parquet, SQL and Pandas
* Fast pd.to_sql() for postgres and mysql
* Out of core functionality to process large files
* Quickly check for potential data schema changes
* Fix added/missing columns
* Fix renamed columns
* Check Excel tabs for consistency across files
* Excel to CSV converter (incl multi-sheet support)

[https://github.com/d6t/d6tstack](https://github.com/d6t/d6tstack)


## [Combine Data](https://github.com/d6t/d6tjoin)

Easily join different datasets even if they don't perfectly match without writing custom code. Does best match joins on strings, dates and numbers. For example you can quickly join similar but not identical stock tickers, addresses, names and dates without manual processing.

### Features include
Enhances `pd.merge()` function with:
* Pre join diagnostics to identify mismatched join keys
* Best match joins that finds the top1 most similar value
	* Quickly join stock identifiers, addresses, names without manual processing
	* Ability to customize similarity functions, set max difference and other advanced features

[https://github.com/d6t/d6tjoin](https://github.com/d6t/d6tjoin)


## [Blog](http://blog.databolt.tech)

[http://blog.databolt.tech](http://blog.databolt.tech)


## [About](https://www.databolt.tech)

[https://www.databolt.tech](https://www.databolt.tech)

Contact: support-at-databolt.tech

## [Alternative Investment Data Standards](https://github.com/d6t/altdata-standards)

Proposal to establish open standards to improve data exchange between alternative investment data vendors and consumers.

[https://github.com/d6t/altdata-standards](https://github.com/d6t/altdata-standards)

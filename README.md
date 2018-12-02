# Databolt python libraries

## Accelerate data engineering

DataBolt is a collection of python-based products and libraries to reduce the time it takes to get your data ready for evaluation and analysis.

It is designed for data scientists and data engineers who appreciate open data exchange and want to reduce frictions in data pipelines.


## [Ingest Data](https://github.com/d6t/d6tstack)

Automatically combine multiple files into one by stacking them together. Works for XLS, CSV, TXT which can be exported to CSV, Parquet, SQL and Pandas.

Vendors often send large datasets in multiple files. Often there are missing and misaligned columns between files that have to be manually cleaned. With d6tstack you can quickly ingest them.

### Features include

* Quickly check columns for consistency across files
* Fix added/missing columns
* Fix renamed columns
* Check Excel tabs for consistency across files
* Excel to CSV converter (incl multi-sheet support)
* Export CSV, Parquet, SQL and Pandas
* Out of core functionality to process large files

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


## [Sync Data](https://github.com/d6t/d6tpipe)

Quickly exchange data, for example between data vendors and consumers, data engineers and data scientists, teachers and students or desktop and laptop. In just a few lines of code, you can push and pull data to/from S3 and ftp in a simple and unified framework. 

It's like git for data! But better because you can include it in your data science code.

### Features include

* Push/pull data to/from s3/ftp
* Schedule regular sync tasks
* Manage access permissions
* Include DDL so others can quickly ingest 

[https://github.com/d6t/d6tpipe](https://github.com/d6t/d6tpipe)


## [Blog](http://blog.databolt.tech)

[http://blog.databolt.tech](http://blog.databolt.tech)


## [About](https://www.databolt.tech)

[https://www.databolt.tech](https://www.databolt.tech)

Contact: support-at-databolt.tech

## [Alternative Investment Data Standards](https://github.com/d6t/altdata-standards)

Proposal to establish open standards to improve data exchange between alternative investment data vendors and consumers.

[https://github.com/d6t/altdata-standards](https://github.com/d6t/altdata-standards)

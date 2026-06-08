# Overview

This repository will hold exercises related to the use of ORM engines to abstract SQL manipulations.
It will focus on the "old classic" direct channel (MySQLclient) and one of the most used ORM (SQLAlchemy) to compare and show the benefits of the added abstraction.

# Project informations

<details>
<summary>Embed from https://intranet.hbtn.io/projects/2193 </summary>

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don&#39;t ask me how to pronounce it...) an Object Relational Mapper (ORM). 

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &quot;What can I do with my objects&quot; and not &quot;How this object is stored? where? when?&quot;. You won&#39;t write any SQL queries only Python code. Last thing, your code won&#39;t be &quot;storage type&quot; dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```
conn = MySQLdb.connect(host=&quot;localhost&quot;, port=3306, user=&quot;root&quot;, passwd=&quot;root&quot;, db=&quot;my_db&quot;, charset=&quot;utf8&quot;)
cur = conn.cursor()
cur.execute(&quot;SELECT * FROM states ORDER BY id ASC&quot;) # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
````

With an ORM:

```
engine = create_engine(&#39;mysql+mysqldb://{}:{}@localhost/{}&#39;.format(&quot;root&quot;, &quot;root&quot;, &quot;my_db&quot;), pool_pre_ping=True)
Base.metadata.create_all(engine)
    
session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print(&quot;{}: {}&quot;.format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right? 

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&#39;t read the entire documentation before starting, just jump on it if you don&#39;t get something. 

## Resources

**Read or watch**:

- [Object-relational mappers](/rltoken/tCytNeWUzuWhAn9APwtp9A) 
- [mysqlclient/MySQLdb documentation](/rltoken/V8KJv3QCReECPZ0V-kXRwg) (*please don&#39;t pay attention to `_mysql`*)
- [MySQLdb tutorial](/rltoken/j_7jU3C9Jsa0o53pgfwxOQ) 
- [SQLAlchemy tutorial](/rltoken/7y1s8FDE_0S-uhBtCgt5-A) 
- [SQLAlchemy](/rltoken/j6kxlUETdjiFwiu0k_JI6Q) 
- [mysqlclient/MySQLdb](/rltoken/vzsiR8tCdY3_OWsMH33jUA) 
- [Introduction to SQLAlchemy](/rltoken/7m6F57mBASM7A2r_GcIeMA) 
- [Flask SQLAlchemy](/rltoken/riV6WcWo1MGRpF3WSmv4Zw) 
- [10 common stumbling blocks for SQLAlchemy newbies](/rltoken/uRrjdEkHmjrVenCqjwJRWQ) 
- [Python SQLAlchemy Cheatsheet](/rltoken/B2luGwQGH5WjiAMglCu1pg) 
- [SQLAlchemy ORM Tutorial for Python Developers](/rltoken/2BoGpuT2vAaoeuC3SN_wPA) (*__Warning:__ This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL*)
- [SQLAlchemy Tutorial](/rltoken/DrwY56jSHCOADKEbSOBa0A)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/zAH3PxVw_N-4dQ45aCW8yw), __without the help of Google__:

### General

- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script 
- What ORM means
- How to map a Python Class to a MySQL table

## More Info

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &#39;help;&#39; or &#39;\h&#39; for help. Type &#39;\c&#39; to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
```


### Install `MySQLdb` module version `2.0.x`

For installing `MySQLdb`, you need to have `MySQL` installed.

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==2.0.3
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, &#39;final&#39;, 0)
```

### Install `SQLAlchemy` module version `1.4.x`

```
$ sudo pip3 install SQLAlchemy==1.4.22
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
&#39;1.4.22&#39;
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&#39;@@SESSION.GTID_EXECUTED&#39; is deprecated and will be re
moved in a future release.&quot;)                                                                                                                    
  cursor.execute(statement, parameters)  
```
	
You can ignore it.


</details>

# General Rules
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39; `)
- All your classes should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39; `)
- All your functions (inside and outside a class) should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39; ` and `python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39; `)
- A documentation is not a simple word, it&#39;s a real sentence explaining what&#39;s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

# Exercises

| Task name                                            | Filename                                       |
|------------------------------------------------------|------------------------------------------------|
| 00. Get all states                                   | 0-select_states.py                             |
| 01. Filter states                                    | 1-filter_states.py                             |
| 02. Filter states by user input                      | task_02_csv.py                                 |
| 03. SQL Injection...                                 | 3-my_safe_filter_states.py                     |
| 04. Cities by states                                 | 4-cities_by_state.py                           |
| 05. All cities by state                              | 5-filter_cities.py                             |
| 06. First state model                                | model_state.py                                 |
| 07. All states via SQLAlchemy                        | 7-model_state_fetch_all.py                     |
| 08. First state                                      | 8-model_state_fetch_first.py                   |
| 09. Contains `a`                                     | 9-model_state_filter_a.py                      |
| 10. Get a state                                      | 10-model_state_my_get.py                       |
| 11. Add a new state                                  | 11-model_state_insert.py                       |
| 12. Update a state                                   | 12-model_state_update_id_2.py                  |
| 13. Delete states                                    | 13-model_state_delete_a.py                     |
| 14. Cities in state                                  | model_city.py, 14-model_city_fetch_by_state.py      |


# Resources

The following are recommended resources and tools

## General ORM Documentation

- https://www.fullstackpython.com/object-relational-mappers-orms.html

## MySQL Python client driver

- https://mysqlclient.readthedocs.io/
- https://www.mikusa.com/python-mysql-docs/index.html
- https://github.com/PyMySQL/mysqlclient

## SQL Alchemy (Python based ORM)
- https://docs.sqlalchemy.org/en/13/orm/tutorial.html
- https://docs.sqlalchemy.org/en/13/
- https://www.youtube.com/watch?v=woKYyhLCcnU
- https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html
- https://www.pythonsheets.com/notes/database/python-sqlalchemy.html
- https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
- https://overiq.com/sqlalchemy-101/





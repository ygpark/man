# node.js - SQLITE 예제

# Inserting Data Into an SQLite Table from a Node.js Application

Summary: in this tutorial, you will learn how to insert one or more row into an SQLite table from a Node.js application.

To insert data into an SQLite table from a Node.js application, you follow these steps:

1. Open a database connection.
2. Execute an INSERT statement.
3. Close the database connection.

For the demonstration, we will create a new database named sample.db in the db folder.

When you open a database connection in the default mode, the database is created if it does not exist.

```javascript
let db = new sqlite3.Database('./db/sample.db');
```

In the sample.db database, we create a table called langs for storing the programming languages:

```javascript
db.run('CREATE TABLE langs(name text)');
```

You can run the program to create the sample.db database and langs table as follows:

```javascript
const sqlite3 = require('sqlite3').verbose();
 
let db = new sqlite3.Database('../db/sample.db');
 
db.run('CREATE TABLE langs(name text)');
 
db.close();
```

Now, we are ready to insert data into the `langs` table.





## Insert one row into a table

To execute an `INSERT` statement, you use the run() method of the Database object:

```javascript
db.run(sql, params, function(err){
  // 
});
```

The `run()` method executes an `INSERT` statement with specified parameters and calls a callback afterwards.

If an error occurred, you can find the detailed information in the `err` argument of the callback function.

In case the statement is executed successfully, the `this` object of the callback function will contain two properties:

- `lastID` property stores the value of the last inserted row ID.
- `changes` property stores the rows affected by the query.

The following `insert.js` program illustrates how to insert a row into the langs table:


```javascript
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./db/sample.db');

// insert one row into the langs table
db.run(`INSERT INTO langs(name) VALUES(?)`, ['C'], function(err) {
if (err) {
    return console.log(err.message);
}
// get the last insert id
console.log(`A row has been inserted with rowid ${this.lastID}`);
});

// close the database connection
db.close();
```



```
>node insert.js
A row has been inserted with rowid 1
```



## Insert multiple rows into a table at a time

To insert multiple rows at a time into a table, you use the following form of the `INSERT` statement:

```sql
INSERT INTO table_name(column_name)
VALUES(value_1), (value_2), (value_3),...
```

To simulate this in the Node.js application, we first need to construct the `INSERT`statement with multiple placeholders:

```sql
INSERT INTO table_name(column_name)
VALUES(?), (?), (?),...
```

```javascript
let languages = ['C++', 'Python', 'Java', 'C#', 'Go'];
```

```javascript
let placeholders = languages.map((language) => '(?)').join(',');
let sql = 'INSERT INTO langs(name) VALUES ' + placeholders;
```

The following `insert-many.js` program illustrates how to insert multiple rows into the langs table:

```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database connection
let db = new sqlite3.Database('../db/sample.db');
 
let languages = ['C++', 'Python', 'Java', 'C#', 'Go'];
 
// construct the insert statement with multiple placeholders
// based on the number of rows
let placeholders = languages.map((language) => '(?)').join(',');
let sql = 'INSERT INTO langs(name) VALUES ' + placeholders;
 
// output the INSERT statement
console.log(sql);
 
db.run(sql, languages, function(err) {
  if (err) {
    return console.error(err.message);
  }
  console.log(`Rows inserted ${this.changes}`);
});
 
// close the database connection
db.close();
```

```
> node insert-many.js
INSERT INTO langs(name) VALUES (?),(?),(?),(?),(?)
Rows inserted 5
```

It inserted 5 rows into the langs table which is what we expected.

In this tutorial, you have learned how to insert one or more rows into an SQLite table from a Node.js application.
# node.js - SQLITE 예제

## Deleting Data in SQLite Database from a Node.js Application

Summary: in this tutorial, you will learn how to delete data in the SQLite database from a Node.js application.

To delete data in the SQLite database from a Node.js application, you use the following steps:

1. Open a database connection.
1. Execute a DELETE statement.
1. Close the database connection.

For the demonstration, we will use the langs table in the sample.db database that we created in the previous tutorial.

# Deleting data example

To delete data from a table, you use the DELETE statement as follows:

```sql
DELETE FROM table_name
WHERE column_name = value;
```

To execute the DELETE statement from a Node.js application, you call the run() method of the Database object as follows:

```js
db.run(sql, params, function(err) {
  // 
});
```

The `run()` method allows you to execute a `DELETE` statement with specified parameters and calls a callback function afterwards.

If there was any error during the execution of `DELETE` statement, the err argument of the callback function will provide the detail. In case the `DELETE` statement executed successfully, the `this` object of the callback function will contain the `changes` property that stores the number of rows deleted.

The following `delete.js` program illustrates how to delete a row from the `langs` table:


```js
const sqlite3 = require('sqlite3').verbose();
 
// open a database connection
let db = new sqlite3.Database('./db/sample.db', (err) => {
  if (err) {
    console.error(err.message);
  }
});
 
let id = 1;
// delete a row based on id
db.run(`DELETE FROM langs WHERE rowid=?`, id, function(err) {
  if (err) {
    return console.error(err.message);
  }
  console.log(`Row(s) deleted ${this.changes}`);
});
 
// close the database connection
db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
});
```

Let’s test the delete.js program.

```
>node delete.js
Row(s) deleted: 1
```

The output showed that one row has been deleted successfully.

In this tutorial, you have learned how to delete data in the SQLite database from a Node.js application.
# node.js - SQLITE 예제

## Updating Data in SQLite Database from a Node.js Application

Summary: this tutorial shows you how to update data in the SQLite database from a Node.js application.

To update data in the SQLite database from a Node.js application, you use these steps:

1. Open a database connection.
1. Execute an `UPDATE` statement.
1. Close the database connection.

For the demonstration, we will use the langs table in the sample.db database that we created in the previous tutorial.



## Updating data example

To update data in a table, you use the UPDATE statement as follows:

```sql
UPDATE table_name
SET column_name = value_1
WHERE id = id_value;
```

To execute the UPDATE statement in the Node.js application, you call the run() method of the Database object:

```js
db.run(sql, params, function(err){
  // 
});
```

The `run()` method executes an UPDATE statement with specified parameters and calls a callback afterwards.

The err argument of the callback stores the error detail in case the execution has any problem e.g., syntax error, locking, etc.

If the UPDATE statement is executed successfully, the this object of the callback function will contain the changes property that stores the number of rows updated.

The following `update.js` program illustrates how to update a row in the `langs` table from `C` to `Ansi C`:

```js
const sqlite3 = require('sqlite3').verbose();
 
// open a database connection
let db = new sqlite3.Database('./db/sample.db');
 
//
let data = ['Ansi C', 'C'];
let sql = `UPDATE langs
            SET name = ?
            WHERE name = ?`;
 
db.run(sql, data, function(err) {
  if (err) {
    return console.error(err.message);
  }
  console.log(`Row(s) updated: ${this.changes}`);
 
});
 
// close the database connection
db.close();
```

Let’s test the update.js program.

```
>node update.js
Row(s) updated: 1
```

The output showed that one row has been updated which is correct.

In this tutorial, you have learned how to update data in the SQLite database from a Node.js application.